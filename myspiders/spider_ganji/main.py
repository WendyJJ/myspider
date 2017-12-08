from scrapy import cmdline
import os
os.chdir('spider_ganji/spiders')

# cmdline.execute('scrapy crawl ganji'.split())
cmdline.execute('scrapy runspider ganji.py'.split())