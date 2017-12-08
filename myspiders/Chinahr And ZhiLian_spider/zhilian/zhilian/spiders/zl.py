# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from zhilian.items import ZhilianItem
import json,os,re,datetime
from scrapy_redis.spiders import RedisCrawlSpider


class ZlSpider(RedisCrawlSpider):
    name = 'zl'
    allowed_domains = ['zhaopin.com']
    # start_urls = ['http://www.zhaopin.com/']
    redis_key = 'zl:urls'

    rules = (
        Rule(LinkExtractor(allow=r'www.zhaopin.com/\w+/$'), follow=True),  #城市页面
        Rule(LinkExtractor(allow=r'jobs.zhaopin.com/\w+/$'), follow=True),  # 列表页
        Rule(LinkExtractor(allow=r'jobs.zhaopin.com/(.*).htm'), callback='parse_item', follow=True),#列表页
    )

    money_pattern = re.compile(r'(\d+)-(\d+)')
    num_pattern = re.compile(r'\d+')
    def parse_item(self, response):
        item = ZhilianItem()
        url = response.url
        #职位名称
        pname = response.xpath('//div[@class="fixed-inner-box"]//h1/text()').extract()[0]
        #公司名称
        company = response.xpath('//div[@class="fixed-inner-box"]//a/text()').extract()[0]
        #福利
        welfare = response.xpath('//div[@class="welfare-tab-box"]/span/text()').extract()[0:]
        welfare = ','.join(welfare)

        lis = response.xpath('//div[@class="terminalpage-left"]/ul/li')
        money = lis[0].xpath('./strong/text()').extract()[0]
        smoney,emoney= self.parse_money(money)
        #地址
        location = response.xpath('//div[@class="tab-inner-cont"]/h2/text()').extract()[0].strip()

        #发布时间
        time_pub = lis[2].xpath('./strong/span/text()').extract()[0]

        #经验
        exprience = lis[4].xpath('./strong/text()').extract()[0]
        syear,eyear = self.process_year(exprience)

        #学历
        degree = lis[5].xpath('./strong/text()').extract()[0]

        #需求人数
        person_num = lis[6].xpath('./strong/text()').extract()[0].strip()

        #描述
        desc_job = response.xpath('//div[@class="tab-inner-cont"][1]/p/text()').extract()[0:]
        desc_job = ','.join(desc_job)



        item['url'] = url
        item['pname'] = pname
        item['smoney'] = int(smoney)
        item['emoney'] = int(emoney)
        item['location'] = location
        item['syear'] = int(syear)
        item['eyear'] = int(eyear)
        item['degree'] = degree
        item['ptype'] = ''
        item['tags'] = ''
        item['time_pub'] = time_pub
        item['person_num'] = person_num
        item['welfare'] = welfare
        item['desc_job'] = desc_job
        item['company'] = company
        item['webname'] = '智联招聘'
        item['crawl_time'] = datetime.datetime.now().strftime('%Y-%m-%d')

        yield item


    def process_year(self,year):
        if '-' in year:
            res = self.num_pattern.findall(year)
            syear = res[0]
            eyear = res[1]
        elif '以上' in year:
            res = self.num_pattern.search(year)
            syear = res.group()
            eyear = res.group()
        else:
            syear = 0
            eyear = 0
        return syear,eyear

    def parse_money(self,value):
        if '-' in value:
            res = self.money_pattern.findall(value)
            smoney = res[0][0]
            emoney = res[0][1]
            return smoney,emoney
        else:
            smoney = 0
            emoney = 0
            return smoney,emoney
