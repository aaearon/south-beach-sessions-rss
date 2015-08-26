# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from datetime import datetime
import pytz

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst


class DefaultItemLoader(ItemLoader):
    default_input_processor = MapCompose(lambda s: s.strip().replace('\n', '').encode('utf-8'))
    default_output_processor = TakeFirst()


class SouthBeachSessionItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    guid = scrapy.Field()
    pubDate = scrapy.Field()
    pass


def string_to_date_to_string(string):
    # This can probably be done more elegantly

    try:
        # Jan. 01, 2015
        date = datetime.strptime(string, "%b. %d, %Y")
    except ValueError:
        # January 01, 2015
        date = datetime.strptime(string, "%B %d, %Y")

    tz = pytz.timezone("UTC")
    return tz.localize(date).strftime("%Y-%m-%d %H:%M:%S %Z")


class SouthBeachSessionLoader(DefaultItemLoader):
    default_item_class = SouthBeachSessionItem

    pubDate_in = MapCompose(string_to_date_to_string)
