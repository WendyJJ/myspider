from scrapy import cmdline
import os
os.chdir('zhilian/zhilian/spiders')

cmdline.execute('scrapy runspider zl.py'.split())
# cmdline.execute('scrapy crawl zl'.split())