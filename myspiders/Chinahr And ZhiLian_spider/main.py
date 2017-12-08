from scrapy import cmdline
import os
os.chdir('chinahr/chinahr/spiders')

cmdline.execute('scrapy runspider zh.py'.split())
# cmdline.execute('scrapy crawl zh'.split())