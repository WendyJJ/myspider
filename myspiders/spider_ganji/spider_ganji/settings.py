# -*- coding: utf-8 -*-

# Scrapy settings for spider_ganji project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spider_ganji'

SPIDER_MODULES = ['spider_ganji.spiders']
NEWSPIDER_MODULE = 'spider_ganji.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spider_ganji (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
"Connection" : "keep-alive",
"Cache-Control" : "max-age=0",
"Upgrade-Insecure-Requests" : "1",
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Referer" : "http://bj.ganji.com/zpxingzhenghouqin/",
"Accept-Encoding" : "gzip, deflate",
"Accept-Language" : "zh-CN,zh;q=0.8",
"Cookie" : "statistics_clientid=me; GANJISESSID=597d0b224837b2e9e6ffa9a116659b06; cityDomain=bj; ganji_uuid=2343444794738927716238; bdshare_firstime=1511320246673; ganji_xuuid=c65cb9df-1c44-43f4-95b2-01749990701c.1511320246961; WantedListPageScreenType=1536; simResStatus=%2C31%2C; webimFangTips=3636063989; citydomain=bj; __utmt=1; gj_footprint=%5B%5B%22%5Cu884c%5Cu653f%5C%2F%5Cu540e%5Cu52e4%22%2C%22%5C%2Fzpxingzhenghouqin%5C%2F%22%5D%2C%5B%22%5Cu623f%5Cu5730%5Cu4ea7%5Cu6295%5Cu8d44%5Cu5206%5Cu6790%22%2C%22%5C%2Fzpfangchantzfx%5C%2F%22%5D%2C%5B%22%5Cu5feb%5Cu9012%5Cu5458%22%2C%22%5C%2Fzpkuaidi%5C%2F%22%5D%5D; zhaopin_lasthistory=zpxingzhenghouqin%7Czpxingzhenghouqin; zhaopin_historyrecords=bj%7Czpxingzhenghouqin%7C-%2Cbj%7Czpfangchantzfx%7C-%2Cbj%7Czpfdcdianzhang%7C-%2Cbj%7Czpkuaidi%7C-; Hm_lvt_655ab0c3b3fdcfa236c3971a300f3f29=1511328333; Hm_lpvt_655ab0c3b3fdcfa236c3971a300f3f29=1511341291; _gl_speed=%5B%22http%3A%2F%2Fcjump.ganji.com%2Fgjclick%3Ftarget%3DpZwY0jCfsvFJshI6UhGGshPfUiql0Z6GUhIlpAR8uv6fIg7GUBtzrjEvn1c1PH9YXaOCIAYKuAu6njEYPH0VPADvmzYYnjnksycOmhEVPWEYPhmvuyR6nAFhTH01PjTzrHEQPkDQTHc3Pjm1nWndrjEKP1TKPHDKnBnOnjDWsinVTHDzczYWsEDQPHDQn1EQn1cYnWD1THcKuvG_pgPYUARhITDdTHDKsEDVnEDVTHTKnTDVTHTKPjTOuj9Ln1cduHPhuhDLm19vmyNQnHc1nA7Bmy7BmW0Kn1EOP1E3nHmKnWcLnj0QPjTYn1cLnHmkTiYKnBnOnjDWsinVTHDzczYWsEDQTiYKsEDVTgP-UAmKpZwY0jCfsvFJshI6UhGGshPfUiqlpA7f0A-8skDzn1E1PjEYP1bYP1n3rHcLP1DvnWn3THDzni3vri3zni33n9DVTHDKrj0OuWnzn1m3m1T1uHbknTD%26v%3D2%22%2C1511341292970%5D; Hm_lvt_8da53a2eb543c124384f1841999dcbb8=1511320247; Hm_lpvt_8da53a2eb543c124384f1841999dcbb8=1511341301; lg=1; __utma=32156897.1982458239.1511320246.1511330406.1511341283.4; __utmb=32156897.4.10.1511341283; __utmc=32156897; __utmz=32156897.1511341283.4.4.utmcsr=bj.ganji.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ganji_login_act=1511341305379; xxzl_deviceid=X2ngQpIeVtKn7SCY%2F4CO0ObVvC2KGUEbJpPNIOv%2BVt35CSkAnGPwsQLF4ql8jx5%2F; _gl_tracker=%7B%22ca_source%22%3A%22www.baidu.com%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A40244453265%7D",
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'spider_ganji.middlewares.SpiderGanjiSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'spider_ganji.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'spider_ganji.pipelines.SpiderGanjiPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#url指纹过滤器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 设置爬虫是否可以中断
SCHEDULER_PERSIST = True

# 设置请求队列类型
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue" # 按优先级入队列
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"  # 按照队列模式
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack" # 按照栈进行请求的调度

# 配置redis管道文件，权重数字相对最大
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 999,  # redis管道文件，自动把数据加载到redis
}

#redis连接配置
REDIS_HOST = '192.168.160.128'
REDIS_PORT = 6379