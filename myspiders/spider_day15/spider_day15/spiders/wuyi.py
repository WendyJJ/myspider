# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from spider_day15.items import WuyiItem
from scrapy_redis.spiders import RedisCrawlSpider
import re
import datetime

class WuyiSpider(RedisCrawlSpider):
    name = 'wuyi'
    allowed_domains = ['51job.com']
    # start_urls = ['http://www.51job.com']
    redis_key = 'wuyispider:urls'
    rules = (
        Rule(LinkExtractor(allow=r'search.51job.com/list/.*'), follow=True),
        Rule(LinkExtractor(allow=r'http://jobs.51job.com/.*/\d+.html?.*'),callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'jobs.51job.com/.*/\d+.html?.*'),callback='parse_item',follow=False),
        # Rule(LinkExtractor(allow=r'jobs.51job.com/all/\d+.html'), callback='parse_item', follow=False),
    )
    num_pattern = re.compile(r'\d+')
    def parse_item(self, response):
        item = WuyiItem()
        url = response.url
        info_cn = response.css('div.cn')
        #职位名称
        pname = info_cn.css('h1::text').extract()
        if ' ' in pname:
            pname = ' '
        else:
            pname = info_cn.css('h1::text').extract()[0]
        #工作点
        location = info_cn.css('span::text').extract()[0]
        #公司名称
        company = info_cn.css('a::text').extract()[0]
        # 薪资
        money = info_cn.css('strong::text').extract()
        if money:
            money = money[0]
            if '万/月' in money:
                smoney = str(float(money.replace('万/月','').split('-')[0]) * 1000)
                emoney = str(float(money.replace('万/月','').split('-')[1]) * 1000)

            elif '千/月' in money:
                smoney = str(float(money.replace('千/月', '').split('-')[0]) * 1000)
                emoney = str(float(money.replace('千/月', '').split('-')[1]) * 1000)
            else:
                smoney = 0
                emoney = 0
        else:
            smoney = 0
            emoney = 0
        #公司类型
        pt = response.xpath('//p[@class="msg ltype"]/text()').extract()[0]
        pt = pt.replace('|','').split()
        ptype = pt[0]
        if len(pt)== 1:
            person_num = ''
        else:
            person_num = pt[1]
        if len(pt)== 2:
            tags = ''
        else:
            tags = pt[2]

        # 福利
        fuli = response.css('p.t2')
        fuli = fuli.css('span::text').extract()
        welfare = ''.join(fuli)
        #具体工作地址
        addr = response.css('div.bmsg')
        address = addr.css('p::text').extract()[-1].strip('\t')
        location = location + address
        #要求(经验,学历)
        requ = response.css('div.t1')
        # 经验年限
        years = requ.css('span::text').extract()[0]
        syear ,eyear = self.process_year(years)

        # 学历
        if len(requ.css('span::text').extract()) == 4:
            degree = requ.css('span::text').extract()[1]
        else:
            degree = '无需要求'
        #发布时间
        if len(requ.css('span::text').extract()) == 5:
            time_pub = requ.css('span::text').extract()[-2].strip('发布时间')
        else:
            time_pub = requ.css('span::text').extract()[-1].strip('发布时间')
        #工作岗位信息
        desc = response.css('div.bmsg::text').extract()
        desc_job = (''.join(desc)).replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '')
        #爬取时间
        crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')
        #网站名称
        webname = '51job'

        # print(pname,location,company,smoney,emoney,ptype,person_num,tags,welfare,syear,eyear,address,date_pub,degree,desc,crawl_time,webname)

        item['url'] = url
        item['pname'] = pname
        item['location'] = location
        item['company'] = company
        item['smoney'] = smoney
        item['emoney'] = emoney
        item['ptype'] = ptype
        item['person_num'] = person_num
        item['tags'] = tags
        item['welfare'] = welfare
        item['syear'] = syear
        item['eyear'] = eyear
        item['time_pub'] = time_pub
        item['degree'] = degree
        item['desc_job'] = desc_job
        item['crawl_time'] = crawl_time
        item['webname'] = webname
        yield item


    def process_year(self,years):
        if '-' in years:
            res = self.num_pattern.findall(years)
            syear = res[0]
            eyear = res[1]
        elif '以上' in years:
            res = self.num_pattern.search(years)
            syear = res.group()
            eyear = res.group()
        elif '1年' in years:
            syear = 1
            eyear = 1
        else:
            syear = 0
            eyear = 0
        return syear,eyear
