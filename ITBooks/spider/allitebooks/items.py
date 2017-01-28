# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class AllitebooksItem(Item):
    # Primary fields
    title = Field()
    cover = Field()
    author = Field()
    # International Standard Book Number
    isbn = Field()
    year = Field()
    pages = Field()
    language = Field()
    file_size = Field()
    file_format = Field()
    category = Field()
    description = Field()
    download = Field()

    # Housekeeping fields
    url = Field()
    spider = Field()
    date = Field()


class BlahItem(AllitebooksItem):
    # Primary fields
    score = Field()
    download_epub = Field()
    download_mobi = Field()
    download_txt = Field()


class TaiwanebookItem(AllitebooksItem):
    # Primary fields
    rename = Field()
    publication = Field()
    publisher = Field()
    # Preservation organization
    pre_organization = Field()
    # Edition number
    edition_number = Field()
    # accession number
    accession_number = Field()
    source = Field()
