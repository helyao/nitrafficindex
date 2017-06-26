# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TrafficscrapyItem(scrapy.Item):
    time = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    roadGrade = scrapy.Field()
    avgspeed = scrapy.Field()
    cIndex = scrapy.Field()
    sIndex = scrapy.Field()
    bIndex = scrapy.Field()
    dir = scrapy.Field()
    startName = scrapy.Field()
    endName = scrapy.Field()
    rticId = scrapy.Field()
    vkt = scrapy.Field()
    rticLonlats = scrapy.Field()

