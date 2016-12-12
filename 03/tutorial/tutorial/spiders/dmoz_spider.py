# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem


"""
    创建项目
        scrapy startproject tutorial
    创建默认模板的爬虫
        scrapy genspider dmoz_spider dmoz.org
    运行爬虫
        scrapy crawl oschina_spider

"""
class OschinaSpiderSpider(scrapy.Spider):
    name = "dmoz_spider"
    allowed_domains = ["oschina.net"]
    start_urls = (
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
    )

    def parse(self, response):
        # filename = response.url.split('/')[-2] + ".html"
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        divs = response.xpath('//*[@id="site-list-content"]/div[1]/div[3]')
        for div in divs:
            item = TutorialItem()
            item['title'] = div.xpath('a/div/text()').extract()
            item['desc'] = div.xpath('//*[@id="site-list-content"]/div[1]/div[3]/div/text()').extract()
            item['link'] = div.xpath('a/@href').extract()
            yield item
