# -*- coding: utf-8 -*-
import urllib2
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector.unified import Selector

from south_beach_sessions.items import SouthBeachSessionLoader


class SbsSpider(CrawlSpider):
    name = 'sbs'
    allowed_domains = ['espn.go.com']
    start_urls = ['http://espn.go.com/espnradio/story/_/id/11756027/south-beach-sessions']

    rules = (
        Rule(LinkExtractor(allow=r'\/espnradio\/play\?id=[0-9]+',
                           restrict_xpaths='//*[@id="content"]/div[3]/div[1]/div[3]/div[2]/div/table//tr/td[3]/center/a'),
             callback='parse_session', follow=True),
    )

    def parse_session(self, response):
        url = urllib2.unquote(response.url)

        sel = Selector(response)
        sbs = SouthBeachSessionLoader(selector=sel)

        sbs.add_xpath('title', '//*[@id="mem"]/div[3]/div[2]/h2/text()')
        sbs.add_xpath('description', '//*[@id="mem"]/div[3]/div[2]/p[1]/text()')
        sbs.add_xpath('link', '//*[@id="mem"]/div[3]/div[2]/p[2]/a/@href')
        sbs.add_value('guid', url)

        yield sbs.load_item()



