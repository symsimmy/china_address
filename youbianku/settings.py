# -*- coding: utf-8 -*-

# Scrapy settings for youbianku project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'youbianku'

SPIDER_MODULES = ['youbianku.spiders']
NEWSPIDER_MODULE = 'youbianku.spiders'

# 设置log级别
LOG_LEVEL = 'INFO'


USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

IPPOOL = [
    {'ipaddr': '219.141.153.39:80'},
    {'ipaddr': '219.141.153.5:80'},
    {'ipaddr': '219.141.153.6:80'},
    {'ipaddr': '219.141.153.35:80'},
    {'ipaddr': '219.141.153.11:80'},
    {'ipaddr': '219.141.153.43:80'},
    {'ipaddr': '118.190.95.35:9001'},
    {'ipaddr': '222.222.236.207:8060'},
    {'ipaddr': '221.193.177.45:8060'},
    {'ipaddr': '117.131.235.198:8060'},
    {'ipaddr': '39.137.69.10:80'},
    {'ipaddr': '222.222.243.124:8060'},
    {'ipaddr': '183.129.207.74:15288'},
    {'ipaddr': '183.129.207.74:14823'},
    {'ipaddr': '1.63.153.153:80'},
    {'ipaddr': '115.29.200.195:808'},
    {'ipaddr': '124.238.248.4:80'},
    {'ipaddr': '125.86.120.204:8197'},
    {'ipaddr': '49.51.193.134:1080'},
    {'ipaddr': '183.129.207.73:22877'},
    {'ipaddr': '49.51.70.42:1080'},
    {'ipaddr': '49.51.193.128:1080'},
    {'ipaddr': '39.135.35.17:80'},
    {'ipaddr': '39.135.35.18:80'},
    {'ipaddr': '39.135.35.19:80'},
    {'ipaddr': '183.189.169.207:8060'},
    {'ipaddr': '222.33.192.238:8118'},
    {'ipaddr': '39.135.35.16:80'},
    {'ipaddr': '61.137.203.99:8118'},
    {'ipaddr': '49.51.195.24:1080'},
    {'ipaddr': '121.17.18.219:8060'},
    {'ipaddr': '222.223.203.109:8060'},
    {'ipaddr': '106.8.17.14:60443'},
    {'ipaddr': '59.48.237.6:8060'},
    {'ipaddr': '221.217.54.195:9000'},
    {'ipaddr': '112.126.65.236:80'},
    {'ipaddr': '222.170.0.102:53281'},
]

DOWNLOADER_MIDDLEWARES = {
    #    'myproxies.middlewares.MyCustomDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 543,
    'youbianku.middlewares.YoubiankuSpiderMiddleware': 125
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'youbianku (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'youbianku.middlewares.YoubiankuSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'youbianku.middlewares.YoubiankuDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'youbianku.pipelines.YoubiankuPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
