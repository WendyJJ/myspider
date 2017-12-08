# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from spider_ganji.items import GanjiItem
from scrapy_redis.spiders import RedisCrawlSpider
import re
import datetime

class GanjiSpider(RedisCrawlSpider):
    name = 'ganji'
    allowed_domains = ['ganji.com']
    # start_urls = ['http://www.ganji.com/zhaopin/']
    redis_key = 'ganjispider:urls'

    rules = (
        Rule(LinkExtractor(allow=r'http://.*ganji.com/zp.*/\d+x.htm'), callback='parse_item', follow=True),
    )
    num_pattern = re.compile(r'\d+')
    def parse_item(self, response):
        item = GanjiItem()
        url = response.url
        if response.css('h1.f24::text') != []:
            #职位名称
            pname = response.css('h1.f24::text').extract()[0]
        if response.css('em.salary::text') != []:
            money = response.css('em.salary::text').extract()[0]
            if '-' in money:
                res = self.num_pattern.findall(money)
                smoney = res[0]
                emoney = res[1]
            else:
                smoney = 0
                emoney = 0

        #工作城市
        info_f = response.xpath('//div//ul[@class="clearfix pos-relat"]//li//em/text()')
        #学历
        if len(info_f) == 2:
            degree = ''
        else:
            degree = info_f.extract()[2]
        #年限
        years = info_f.extract()[3]
        #最大,最小
        syear, eyear = self.process_year(years)
        #需求人数
        person_num = info_f.extract()[5].replace('人','')
        #工作地址
        location = response.css('li.fl.w-auto em a::text').extract()[0]
        #福利
        if response.css('div.d-welf-items ul.clearfix li::text').extract() != []:
            welfare = response.css('div.d-welf-items ul.clearfix li::text').extract()
            welfare = ','.join(welfare)
        else:
            welfare = '无'

        # 工作详情
        desc = response.css('div.deta-Corp::text').extract()
        desc_job = (', '.join(desc)).replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '')

        # 工作所在地
        address = response.css('dl.detail-contact dd::text').extract()[-2]
        location = location + address

        # 公司名称
        company = response.css('div.ad-firm-logo a::text').extract()[0].strip()

        # 发布日期
        time_pub = response.css('p.data-sty.mb-5 span::text').extract()[0].replace('更新时间：', '')

        # 爬取时间
        crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')
        # 爬取网站
        webname = '赶集网'


        item['url'] = url
        item['pname'] = pname
        item['location'] = location
        item['company'] = company
        item['ptype'] = ''
        item['tags'] = ''
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

    def process_year(self,years):
        if '-' in years:
            res = self.num_pattern.findall(years)
            syear = res[0]
            eyear = res[1]
        elif '以内' in years:
            res = self.num_pattern.search(years)
            syear = res.group()
            eyear = res.group()
        elif '不限' in years:
            syear = 0
            eyear = 0
        else:
            syear = 0
            eyear = 0
        return syear,eyear



