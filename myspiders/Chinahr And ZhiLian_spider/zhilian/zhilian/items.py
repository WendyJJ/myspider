# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    url = scrapy.Field()          #职业名
    pname = scrapy.Field()          #职业名
    location = scrapy.Field()        #地址
    company = scrapy.Field()        #公司
    ptype = scrapy.Field()          #公司类型
    tags = scrapy.Field()           #标签
    smoney = scrapy.Field()
    emoney = scrapy.Field()
    eyear = scrapy.Field()     #经验
    syear = scrapy.Field()     #经验
    degree = scrapy.Field()         #学历
    person_num = scrapy.Field()     #需求人数
    time_pub = scrapy.Field()       #发布时间
    desc_job = scrapy.Field()           #描述
    welfare = scrapy.Field()
    crawl_time = scrapy.Field()
    webname = scrapy.Field()