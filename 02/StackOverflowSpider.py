#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-11 22:24:32
# @Author  : Zeus (meteorshield@gmail.com)
# @Link    : http://www.zeusw.com
# @Version : $Id$

"""
    运行：
        scrapy runspider StackOverflowSpider.py -o stackoverflow.csv
"""
import scrapy

class StackOverflowSpider(scrapy.Spider):

    name = 'stackoverflow'
    start_urls = ['http://stackoverflow.com/questions?sort=votes']

    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            print(full_url, '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield {
            'title': response.css('h1 a::text').extract()[0],
            'votes': response.css('.vote span::text').extract()[0],
            'body': response.css('.question .post-text::text').extract()[0],
            'tags': response.css('.question .post-taglist a::text').extract(),
            'link': response.url,
        }