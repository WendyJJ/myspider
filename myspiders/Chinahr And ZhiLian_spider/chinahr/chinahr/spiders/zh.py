# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from chinahr.items import ChinahrItem
import re,datetime
from scrapy_redis.spiders import RedisCrawlSpider
from datetime import timedelta

class ZhSpider(RedisCrawlSpider):
    name = 'zh'
    allowed_domains = ['chinahr.com']
    # start_urls = ['http://www.chinahr.com']
    redis_key = 'zh:urls'


    rules = (
        Rule(LinkExtractor(allow=r'www.chinahr.com/\w+/jobs/\d+/'), follow=True),
        # Rule(LinkExtractor(allow=r'www.chinahr.com/sou$'), follow=True),
        Rule(LinkExtractor(allow=r'www.chinahr.com/job/\d+.html'), callback='parse_item', follow=True),
    )

    year_pattern = re.compile(r'\d+')

    def parse_item(self, response):
        item = ChinahrItem()
        url = response.url
        pname = response.xpath('//h1/span/text()').extract()[0]
        info = response.xpath('//div[@class="job_require"]/span')
        location = info[1].xpath('./text()').extract()[0]
        company = response.xpath('//h4/a/text()').extract()[0]
        tags = response.xpath('//div[@class="compny_tag"]/span/text()').extract()[0:]
        tags = ','.join(tags)
        money = info[0].xpath('./text()').extract()[0]
        if len(money)!=2:
            smoney = money.split('-')[0]
            emoney = money.split('-')[1]
        else:
            smoney = 0
            emoney = 0
        syear = info[4].xpath('./text()').extract()[0]
        syear = self.syear_parse(syear)
        degree = info[3].xpath('./text()').extract()[0]
        time_pub = response.xpath('//p[@class="updatetime"]/text()').extract()[0]
        time_pub = self.time_parse(time_pub)
        desc_job = response.xpath('//div[@class="job_intro_info"]')
        desc_job = desc_job.xpath('./text()').extract()[0:]
        desc_job =''.join( ''.join(desc_job).strip().split('\n'))
        welfare = response.xpath('//ul[@class="clear"]/li')
        welfare = welfare.xpath('./text()').extract()[0:]
        welfare = ''.join(welfare)

        item['url'] = url
        item['pname'] = pname
        item['smoney'] = int(smoney)
        item['emoney'] = int(emoney)
        item['location'] = location
        item['syear'] = int(syear)
        item['eyear'] = int(syear)
        item['degree'] = degree
        item['ptype'] = ''
        item['tags'] = tags
        item['time_pub'] = time_pub
        item['person_num'] = 0
        item['welfare'] = welfare
        item['desc_job'] = desc_job
        item['company'] = company
        item['webname'] = '中华英才'
        item['crawl_time'] = datetime.datetime.now().strftime('%Y-%m-%d')
        yield item

    def time_parse(self,value):
        if '今天' in value:
            time_pub = datetime.datetime.now().strftime('%Y-%m-%d')
        elif  '昨天' in value:
            time_pub = (datetime.datetime.now()-timedelta(day=1)).strftime('%Y-%m-%d')
        else:
            time_pub = '2017-' + value[:-2]
        return time_pub

    def syear_parse(self,value):
        res = self.year_pattern.findall(value)
        if res:
            syear = res[0]
        else:
            syear = 0
        return syear