# -*- coding: utf-8 -*-
from scrapy import Selector, Spider, Request

from south_beach_sessions.items import SouthBeachSessionLoader


class SbsSpider(Spider):
    name = 'sbs'
    allowed_domains = ['espn.go.com']
    start_urls = (
        'http://espn.go.com/espnradio/story/_/id/11756027/south-beach-sessions',
    )

    def parse(self, response):
        for row in response.xpath('//*[@id="content"]/div[3]/div[1]/div[3]/div[2]/div/table//tr[contains(@class, "last")]'):
            date = 'td[1]/center/text()'
            guest = 'td[2]/center/text()'
            link = 'td[3]/center/a/@href'

            sbs = SouthBeachSessionLoader(selector=row)

            sbs.add_xpath('pubDate', date)
            sbs.add_xpath('title', guest)

            yield Request(url=row.xpath(link).extract()[0],
                          callback=self.parse_session,
                          meta={'item': sbs.load_item()}, )

    def parse_session(self, response):
        sel = Selector(response)
        sbs = SouthBeachSessionLoader(item=response.meta['item'], selector=sel)

        sbs.add_xpath('description', '//*[@id="mem"]/div[3]/div[2]/p[1]/text()')
        sbs.add_xpath('link', '//*[@id="mem"]/div[3]/div[2]/p[2]/a/@href')
        sbs.add_value('guid', response.url)

        yield sbs.load_item()
