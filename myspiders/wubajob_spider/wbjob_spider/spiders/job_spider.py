# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
import datetime
from wubajob_spider.wbjob_spider.items import WubajobSpiderItem
from scrapy_redis.spiders import RedisCrawlSpider


class JobSpider(RedisCrawlSpider):
    name = 'job_spider'
    allowed_domains = ['58.com']
    # start_urls = ['http://www.58.com/zhaopin/']
    redis_key = 'JobSpider:urls'

    rules = (
        Rule(LinkExtractor(allow='\w+.58.com/job/'), follow=True),
        Rule(LinkExtractor(allow=r'/\d+x.shtml.*'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = WubajobSpiderItem()
        url = response.url
        pname = response.css('.pos_title::text').extract()[0]
        location = response.css('.pos_address span::text').extract()
        location = ''.join(location)
        company = response.css('.baseInfo_link a::text').extract()[0]
        ptype = response.css('.comp_baseInfo_link::text').extract()[0]
        welfare = response.css('.pos_welfare_item::text').extract()
        welfare = ','.join(welfare)
        money = response.css('.pos_salary::text').extract()[0]
        smoney,emoney = self.process_money(money)
        year = response.css('.border_right_None::text').extract()[0]
        syear,eyear = self.process_year(year)
        degree = response.css('.pos_base_condition span::text').extract()[1]
        person_num = response.css('.pos_base_condition span::text').extract()[0]
        if '若干' in person_num:
            person_num = 100
        else:
            pattren = re.compile(r'\d+')
            person_num = pattren.search(person_num)
            person_num = person_num.group()
            person_num = int(person_num)
        time_pub = response.css('.pos_base_update span::text').extract()[0]
        if '前' in time_pub:
            time_pub1 = response.css('.pos_base_statistics span strong::text').extract()[0]
            time_pub2 = response.css('.pos_base_update span::text').extract()[0]
            time_pub = time_pub1+time_pub2
        desc_job = response.xpath('//div[@class="des"]/text()').extract()
        desc_job = ''.join(desc_job).strip()
        crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')
        webname = '58同城'

        item['url'] = url
        item['pname'] = pname
        item['location'] = location
        item['company'] = company
        item['ptype'] = ptype
        item['welfare'] = welfare
        item['smoney'] = smoney
        item['emoney'] = emoney
        item['syear'] = syear
        item['eyear'] = eyear
        item['degree'] = degree
        item['person_num'] = person_num
        item['time_pub'] = time_pub
        item['desc_job'] = desc_job
        item['crawl_time'] = crawl_time
        item['webname'] = webname

        yield item


    def process_money(self,money):
        if "-" in money:
            smoney = money.split('-')[0]
            smoney = int(smoney)
            emoney = money.split('-')[1]
            emoney = int(emoney)
        elif '以下'in money:
            smoney = int(money)
            emoney = 0
        elif '以上' in money:
            smoney = 0
            emoney = int(money)
        else:
            smoney = 0
            emoney = 0
        return smoney,emoney
    def process_year(self,year):
        if '-' in year:
            syear = year.split('-')[0]
            eyear = year.split('-')[1]
            pattern = re.compile(r'\d+')
            res = pattern.search(eyear)
            eyear = res.group()
            eyear = int(eyear)
        elif "以下" in year:
            syear = 0
            pattern = re.compile(r'\d+')
            res = pattern.search(year)
            eyear = res.group()
            eyear = int(eyear)
        elif '以上' in year:
            syear = year.replace('年以上','')
        else:
            syear = 0
            eyear = 0
        return syear,eyear
