# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YoubiankuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 邮政编码
    code = scrapy.Field()
    # 链接
    href = scrapy.Field()
    pass


class AddressItem(scrapy.Item):
    # 省份
    province = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 区县
    district = scrapy.Field()
    # 地区
    area = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 邮政编码
    postcode = scrapy.Field()
