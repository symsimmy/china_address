from scrapy import Request
from scrapy.spiders import Spider
from youbianku.items import AddressItem
import pandas as pd


class AddressSpider(Spider):
    name = 'youbianku_address'
    allowed_domains = ['www.youbianku.cn']

    def start_requests(self):
        # href = "/postcode/200011-0"
        df = pd.read_csv('./youbianku.csv')
        df2 = df[df['code'] >= 529030]
        for href in df2['href']:
            url = 'https://www.youbianku.cn' + href
            yield Request(url)

    def parse(self, response):
        # # 命令行调试代码
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)

        item = AddressItem()
        fieldset = response.xpath('.//fieldset//ul')

        item['province'] = ''
        province = fieldset.xpath('.//li//span[@itemprop="addressRegion"]/a/text()').extract()
        if len(province) > 0:
            item['province'] = province[0]

        locality_list = fieldset.xpath('.//li//span[@itemprop="addressLocality"]/a/text()').extract()
        locality_size = len(locality_list)
        item['city'] = ''
        item['district'] = ''
        item['area'] = ''
        if locality_size > 0:
            item['city'] = locality_list[0]
        if locality_size > 1:
            item['district'] = locality_list[1]
        if locality_size > 2:
            item['area'] = locality_list[2]

        item['postcode'] = ''
        postcode = fieldset.xpath('.//li//span[@itemprop="postalCode"]//a/text()').extract()
        if len(province) > 0:
            item['province'] = province[0]

        more_link_url = response.xpath('.//fieldset//div[@class="more-link"]/a/@href').extract()
        if more_link_url:
            if '/' in more_link_url[0]:
                more_url = 'https://www.youbianku.cn' + more_link_url[0]
                yield Request(url=more_url, meta={'item': item}, callback=self.parse_address, dont_filter=True)

    def parse_address(self, response):
        # # 命令行调试代码
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)

        item = response.meta['item']
        address_list = response.xpath('.//div[@class="view-content"]//tbody//td[@class="views-field views-field-title"]'
                                      '//a/text()').extract()

        postcode = response.xpath(
            './/div[@class="view-content"]//tbody//td[@class="views-field views-field-field-postcode"]'
            '//a/text()').extract()

        if postcode:
            item['postcode'] = postcode[0]

        address_size = len(address_list)

        for address in address_list:
            item['address'] = address
            yield item

        next_url = response.xpath('.//li[@class="pager-next last"]/a/@href').extract()

        if next_url:
            next_url = 'https://www.youbianku.cn' + next_url[0]
            yield Request(url=next_url)
