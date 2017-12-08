# -*- coding: utf-8 -*-

# Scrapy settings for liepin_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'liepin_spider'

SPIDER_MODULES = ['liepin_spider.spiders']
NEWSPIDER_MODULE = 'liepin_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'liepin_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False #scrapy 默认的cookie关闭 ,自己的cookie生效

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    # "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # "Accept-Language" : "zh-CN,zh;q=0.9",
    # "Connection" : "keep-alive",
    "Cookie" : "WebIMToken=%7B%22imClientId%22%3A%221d6823f37ea67fff1caef7a8935abacb%22%2C%22accessToken%22%3A%221d6823f37ea67fffd1cf0da1b7d9b94eb884767fd828ddd2faba5fb1cc2a628d%22%2C%22imId%22%3A%221d6823f37ea67fffe2e4950ddd729b19%22%2C%22userId%22%3A%22db668717e87d84730c7b794cfba7bbf6%22%2C%22imUserType%22%3A%220%22%2C%22time%22%3A1511233331935%7D; gr_user_id=9cc0571d-e678-4ec8-b65f-91d6881b1b7d; __uuid=1511145036054.83; need_bind_tel=false; _uuid=D8647339FFA8441E69393EDF6E88B2E5; slide_goldcard_times20171120=4; fe_www_viewcount=4; f099f2df=263084406993eedade95a875331cc498; lt_auth=ur1ePHVUm1%2Bv4SbQgGNa5K8e3dn%2BUmWc9SxejE1ThNO%2FWKLi4PriSg%2BAprAHxBMhkE99cMULNLH%2F%0D%0AN%2Br6yHZL7EATwGmkloC2tOW40GEITd0wdf2ihf73wc6DRZ90xnEFzyVmpH5KyEzzuhErM9HuymPh%0D%0Ajoju1bSl%2B%2Fs%3D%0D%0A; UniqueKey=c2d8ec168bd97cc31a667e00ad0d9493; user_kind=0; is_lp_user=true; c_flag=6476b1669f748253f4bb3f7f6f120c56; new_user=false; login_temp=islogin; art_rand=DBFC2E6EC0A84801B5F62731B59C5DDA; verifycode=6aef7e7eb4bd43e5907719e81519f11a; iknowFlagPrivacyResume=false; _fecdn_=1; abtest=0; JSESSIONID=9C7FFDCA6196FFF60F40261D9D0EDF0E; _mscid=00000000; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1511145037,1511224099; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1511233340; gr_session_id_bf8a73282d811a1b=a96996ba-4101-46ee-b5b3-bf4a659e7b77; gr_cs1_a96996ba-4101-46ee-b5b3-bf4a659e7b77=c2d8ec168bd97cc31a667e00ad0d9493; __tlog=1511224099101.86%7C00000000%7CR000000035%7C00000000%7C00000000; __session_seq=93; __uv_seq=93; user_vip=0; user_name=%E7%8E%8B%E5%87%AF; user_photo=55557f3b28ee44a8919620ce01a.gif",
    # "Host" : "www.liepin.com",
    # "Referer" : "https://c.liepin.com/",
    # "Upgrade-Insecure-Requests" : "1",
    # "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'liepin_spider.middlewares.LiepinSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'liepin_spider.middlewares.RandomUserAgent': 1,
    # 'liepin_spider.middlewares.AuthRandomProxy': 2,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'liepin_spider.pipelines.LiepinSpiderPipeline': 300,
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

AUTH_PROXIES = [
    {'host' : '39.106.125.164:8888', 'auth' : 'root:Python13104213'}
]

# url指纹过滤器
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

# redis连接配置
REDIS_HOST = '192.168.110.128'
REDIS_PORT = 6379
