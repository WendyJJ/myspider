# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
import datetime
from liepin_spider.items import LiepinSpiderItem
from scrapy_redis.spiders import RedisCrawlSpider


class LiepinSpider(RedisCrawlSpider):
    name = 'liepin'
    allowed_domains = ['liepin.com']
    # start_urls = ['https://c.liepin.com/']
    redis_key = 'LiepinSpider:urls'

    rules = (
        # Rule(LinkExtractor(),callback='parse_item',follow=False),
        Rule(LinkExtractor(allow=r'zhaopin/.*'),follow=True),
        Rule(LinkExtractor(allow=r'company/\d+/'),follow=True),
        Rule(LinkExtractor(allow=r'xycompany/\d+/'),follow=True),
        Rule(LinkExtractor(allow=r'job/\d+.*'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = LiepinSpiderItem()
        url = response.url
        pname = response.css('.title-info h1::text').extract() # 职业名
        if pname:
            pname = pname[0]
        elif response.css('.baseinfo-top span::text').extract():
            pname = response.css('.baseinfo-top span::text').extract()[0]
        else:
            pname = ''

        location = response.css('.basic-infor a::text').extract()  # 地址
        if location:
            location = location[0]
        elif response.css('.basic-infor span::text').extract():
            location = response.css('.basic-infor span::text').extract()[0].strip()
        elif response.css('.job-conditon p a::text').extract():
            location = response.css('.job-conditon p a::text').extract()[0]
        company = response.css('.title-info h3 a::text').extract()  # 公司
        if company:
            company = company[0]
        else:
            company = ''
        ptype = response.xpath('//ul[@class="new-compintro"]//a/text()').extract()  # 公司类型
        if ptype:
            ptype = ptype[0].strip()
        else:
            ptype = ''
        # print(ptype)
        welfare = response.css('.tag-list span::text').extract() # 福利
        welfare = ','.join(welfare)
        money = response.css('.job-item-title::text').extract()
        if money:
            money = money[0]
        elif response.xpath('//p[@class="salary"]/text()'):
            money = response.xpath('//p[@class="salary"]/text()').extract()[0]
        smoney,emoney = self.process_money(money)
        # smoney = response.css('.job-item-title::text').extract()[0].strip().split('-')[0]  # 最小
        # emoney = response.css('.job-item-title::text').extract()[0].strip().split('-')[1].replace('万','') # 最大
        year = response.css('.job-qualifications span::text').extract()  # 经验年限
        if year:
            year = year[1]
        elif response.xpath('//div[@class="job-conditon"]/p[2]/text()'):
            year = response.xpath('//div[@class="job-conditon"]/p[2]/text()').extract()[0]
        year = self.process_year(year)
        age = response.css('.job-qualifications span::text').extract()  # 年龄
        if age:
            if '话' or '语' in age[2]:
                age = response.css('.job-qualifications span::text').extract()[3]
            else:
                age = age[2]
        else:
            age = '0'
        # print(age)
        age = self.process_age(age)
        degree = response.css('.job-qualifications span::text').extract()  # 学历
        if degree:
            degree = degree[0]
        elif response.xpath('//div[@class="job-conditon"]/p[2]/text()').extract():
            degree = response.xpath('//div[@class="job-conditon"]/p[2]/text()').extract()[0]
        else:
            degree = ''
        time_pub = response.css('.basic-infor time::text').extract()  # 发布时间
        if time_pub:
            time_pub = time_pub[0].strip()
        else:
            time_pub = ''
        desc_job = response.xpath('//article[@class="content-word"]/text()').extract()  # 描述
        if desc_job:
            desc_job = ''.join(desc_job).strip()
        else:
            desc_job = response.xpath('//div[@class="content content-word"]/text()').extract()
            desc_job = ''.join(desc_job).strip()
        crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')  # 抓取时间
        webname =  '猎聘网'
        # print(desc_job)
        item['url'] = url
        item['pname'] = pname
        item['location'] = location
        item['company'] = company
        item['ptype'] = ptype
        item['welfare'] = welfare
        item['smoney'] = smoney
        item['emoney'] = emoney
        item['year'] = year
        item['age'] = age
        item['degree'] = degree
        item['time_pub'] = time_pub
        item['desc_job'] = desc_job
        item['crawl_time'] = crawl_time
        item['webname'] = webname
        yield item


    def process_money(self,value):
        if '-' in value:
            smoney = value.strip().split('-')[0]
            emoney = value.strip().split('-')[1].replace('万','')
            smoney = int(smoney)
            emoney = int(emoney)
        else:
            smoney = 0
            emoney = 0
        return smoney,emoney
    def process_year(self,year):
        if '年以上经验' in year:
            year = year.replace('年以上经验','')
            year = int(year)
        else:
            year = 0
        return year
    def process_age(self,age):
        if '-' in age:
            age = age.replace('岁','')
        else:
            age = 0
        return age

