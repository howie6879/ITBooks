# -*- coding: utf-8 -*-
import datetime
import sys
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from scrapy.http import Request
from allitebooks.items import AllitebooksItem
from allitebooks.pipelines import AllitebooksPipeline

if sys.version_info[0] > 2:
    from urllib.parse import urljoin
else:
    from urlparse import urljoin


class AllitebooksSpider(scrapy.Spider):
    name = "allitebooks"
    allowed_domains = ["allitebooks.com"]
    start_urls = ('http://www.allitebooks.com', )

    def parse(self, response):
        """
        Get the next pages and yield requests
        :param response:
        :return: request url
        """
        pages = response.css('.pagination>a::text').extract()[-1]
        for page in range(int(pages)):
            # Generate a list of urls
            url = urljoin(response.url, '/page/' + str(page + 1))
            yield Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        """
        Get item URLs and yield Requests
        :param response:
        :return: request url
        """
        urls = response.css(
            'article>div.entry-body>header>.entry-title>a::attr(href)'
        ).extract()
        for url in urls:
            # Remove duplicate links
            sqlDb = AllitebooksPipeline()
            isExist = sqlDb.search_url('allitebooks', url)
            if not isExist:
                yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        """
        This function parses a property page.
        :param response:
        :return: item
        """
        # Create the loader using response
        l = ItemLoader(item=AllitebooksItem(), response=response)
        # Load primary fields using css expressions
        l.add_css('title', '.single-title::text', MapCompose(str.strip))
        l.add_css('cover', '.entry-body-thumbnail>a>img::attr(src)')
        book_details = response.css('.book-detail>dl>dd::text').extract()
        author_list = response.css(
            '.book-detail>dl>dd:nth-child(2)>a::text').extract()
        category_list = response.css(
            '.book-detail>dl>dd:nth-child(16)>a::text').extract()
        author = ','.join(author_list)
        category = ','.join(category_list)
        book_details = book_details[len(author_list):(-len(category_list))]
        l.add_value('author', author, MapCompose(str.strip))
        l.add_value('category', category, MapCompose(str.strip))
        item_name = "isbn year pages language file_size file_format".split()
        for index, value in enumerate(item_name):
            l.add_value(value, book_details[index], MapCompose(str.strip))
        l.add_css('description', '.entry-content')
        l.add_css('download', 'span.download-links>a::attr(href)',
                  MapCompose(str.strip), TakeFirst())
        # Housekeeping fields
        l.add_value('url', response.url)
        l.add_value('spider', self.name)
        l.add_value('date', datetime.datetime.now())
        yield l.load_item()
