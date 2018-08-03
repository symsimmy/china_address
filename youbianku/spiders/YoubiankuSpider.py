from scrapy import Request
from scrapy.spiders import Spider
from youbianku.items import YoubiankuItem


class YoubinakuSpider(Spider):
    name = 'youbianku'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://www.youbianku.cn/postcode'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = YoubiankuItem()
        tds = response.xpath('//span/a')
        for td in tds:
            item['code'] = td.xpath('.//text()').extract()[0]
            item['href'] = td.xpath('.//@href').extract()[0]
            yield item

        next_url = response.xpath('//li[@class="pager-next"]/a/@href').extract()
        print(next_url)

        if next_url:
            next_url = 'https://www.youbianku.cn' + next_url[0]
            yield Request(next_url, headers=self.headers)
