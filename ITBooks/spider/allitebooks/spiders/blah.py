# -*- coding: utf-8 -*-
import datetime
import sys
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from scrapy.http import Request
from allitebooks.items import BlahItem
from allitebooks.pipelines import BlahPipeline

if sys.version_info[0] > 2:
    from urllib.parse import urljoin
else:
    from urlparse import urljoin


class BlahSpider(scrapy.Spider):
    name = "blah"
    allowed_domains = ["blah.me"]
    start_urls = ('http://www.blah.me/', )

    def parse(self, response):
        """
        Get the next pages and yield requests
        :param response:
        :return: request url
        """
        pages = response.css('ul.pagination>li>a::attr(data-page)').extract()[
            -1]
        for page in range(int(pages)):
            # Generate a list of urls
            url = urljoin(response.url, '/?p=' + str(page + 1))
            yield Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        """
        Get item URLs and yield Requests
        :param response:
        :return: request url
        """
        urls = response.css('div.ok-box>a::attr(href)').extract()
        for url in urls:
            url = urljoin(response.url.split('?p')[0], url)
            # yield Request(url, callback=self.parse_item)
            # Remove duplicate links
            sqlDb = BlahPipeline()
            isExist = sqlDb.search_url('blah', url)
            if not isExist:
                yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        """
        This function parses a property page.
        :param response:
        :return: item
        """
        # Create the loader using response
        l = ItemLoader(item=BlahItem(), response=response)
        # Load primary fields using css expressions
        l.add_css('title', 'h1[itemprop*=name]::text', MapCompose(str.strip))
        l.add_css('cover', '.ok-book-cover>img::attr(src)',
                  MapCompose(lambda s: urljoin(response.url, s)), Join())
        l.add_css(
            'author', 'a[itemprop*=author]::text',
            MapCompose(
                lambda s: s.replace('\t', '').replace('\r', '').replace('\n', '')
            ), Join())
        l.add_css('category',
                  'span.ok-book-meta-content>a[itemprop*=keywords]::text',
                  MapCompose(str.strip), Join())
        l.add_css('description', 'div[itemprop*=description]>p::text',
                  MapCompose(str.strip), Join())
        l.add_css(
            'score', 'div.ok-book-douban>a>span.ok-book-meta-content::text',
            MapCompose(
                lambda s: s.replace('\t', '').replace('\r', '').replace('\n', '')
            ), Join())
        l.add_css('download_epub', 'a[data-book-type*=epub]::attr(href)',
                  MapCompose(lambda s: urljoin('http://blah.me/', s)), Join())
        l.add_css('download_mobi', 'a[data-book-type*=mobi]::attr(href)',
                  MapCompose(lambda s: urljoin('http://blah.me/', s)), Join())
        l.add_css('download_txt', 'a[data-book-type*=txt]::attr(href)',
                  MapCompose(lambda s: urljoin('http://blah.me/', s)), Join())
        # Housekeeping fields
        l.add_value('url', response.url)
        l.add_value('spider', self.name)
        l.add_value('date', datetime.datetime.now())
        yield l.load_item()
