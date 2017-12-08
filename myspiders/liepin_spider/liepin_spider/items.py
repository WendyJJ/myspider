# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LiepinSpiderItem(scrapy.Item):
    url = scrapy.Field()
    pname = scrapy.Field()  # 职业名
    location = scrapy.Field()  # 地址
    company = scrapy.Field()  # 公司
    ptype = scrapy.Field()  # 公司类型
    welfare = scrapy.Field()  # 福利
    smoney = scrapy.Field()  # 最小
    emoney = scrapy.Field()  # 最大
    year = scrapy.Field() #经验年限
    age = scrapy.Field() #年龄
    degree = scrapy.Field()  # 学历
    time_pub = scrapy.Field()  # 发布时间
    desc_job = scrapy.Field()  # 描述
    crawl_time = scrapy.Field()  # 抓取时间
    webname = scrapy.Field()  # 网站名称