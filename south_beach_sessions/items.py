# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst


class DefaultItemLoader(ItemLoader):
    default_input_processor = MapCompose(lambda s: s.strip().replace('\n', '').encode('utf-8'))
    default_output_processor = TakeFirst()

class SouthBeachSessionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    guid = scrapy.Field()
    pubDate = scrapy.Field()
    pass

class SouthBeachSessionLoader(DefaultItemLoader):
    default_item_class = SouthBeachSessionItem



