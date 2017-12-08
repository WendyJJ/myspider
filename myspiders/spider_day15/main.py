from scrapy import cmdline
import os
os.chdir('spider_day15/spiders')
# cmdline.execute('scrapy crawl wuyi'.split())



# cmdline.execute('scrapy runspider lagou.py'.split())
cmdline.execute('scrapy runspider wuyi.py'.split())