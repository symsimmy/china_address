

# 中文地址库
该爬虫主要通过scrapy和IPProxy，抓取邮编库上所有的中文地址信息和对应的邮编和三级地址信息。

### 使用方法
数据的抓取分为两部分

1. 一部分是邮编和对应的抓取页面的url，存储为postcode.csv
2. 另一部分是所有的地址信息，存储为address.csv

使用方法
1.获取项目
```
git clone https://github.com/symsimmy/china_address.git
```
2.进入项目目录
```
cd youbianku
```

3.获取邮编和邮编页面的url
```
scrapy crawl youbianku -o postcode.csv -t csv
```
4.抓取地址信息
```
scrapy crawl youbianku_address -o address.csv -t csv
```

### 注意事项
1.更换ip池里面的ip
修改settings.py里面的IPPOOL字段,更换为你使用IPProxy抓取的代理IP即可

