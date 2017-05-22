# -*- coding: utf-8 -*-
import datetime
import sys
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from scrapy.http import Request
from allitebooks.items import TaiwanebookItem
from allitebooks.pipelines import TaiwanebookPipeline

if sys.version_info[0] > 2:
    from urllib.parse import urljoin
else:
    from urlparse import urljoin


class TaiwanebookSpider(scrapy.Spider):
    name = "taiwanebook"
    allowed_domains = ["taiwanebook.ncl.edu.tw"]
    start_urls = ['http://taiwanebook.ncl.edu.tw/zh-tw/']

    def parse(self, response):
        """
        Get some pages and yield requests
        :param response:
        :return: request url
        """
        urls = response.css(
            'div.row>div.container>div.column>a::attr(href)').extract()
        for url in urls:
            yield Request(url, callback=self.parse_detail)

    def parse_pages(self, response):
        """
        Get page URLs and yield Requests
        :param response:
        :return: request url
        """
        urls = response.css('select#select>option::attr(value)').extract()
        for url in set(urls):
            self.log(url)
            yield Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        """
        Get item URLs and yield Requests
        :param response:
        :return: request url
        """
        urls = response.css('div.content>a.header::attr(href)').extract()
        for url in urls:
            # Remove duplicate links
            sqlDb = TaiwanebookPipeline()
            isExist = sqlDb.search_url('taiwanebook', url)
            if not isExist:
                yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        """
        This function parses a property page.
        :param response:
        :return: item
        """
        login_num = response.url.split('/')[-1]
        download = "pdfjs_dual/web/viewer.html?file=/ebkFiles/{login_num}/{login_num}.PDF&r2l=true".format(
            login_num=login_num)
        # Create the loader using response
        l = ItemLoader(item=TaiwanebookItem(), response=response)
        # Load primary fields using css expressions
        l.add_css('title', 'div.image>a>div.image>img::attr(alt)',
                  MapCompose(str.strip), Join())
        l.add_css('cover', 'div.image>a>div.image>img::attr(src)',
                  MapCompose(str.strip), Join())
        l.add_css('info', 'div.twelve>div.ui>div.row')
        l.add_value('download',
                    urljoin("http://taiwanebook.ncl.edu.tw", download))

        # Housekeeping fields
        l.add_value('url', response.url)
        l.add_value('spider', self.name)
        l.add_value('date', datetime.datetime.now())
        yield l.load_item()
