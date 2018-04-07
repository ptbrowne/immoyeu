# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImmoyeuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price = scrapy.Field()
    zipcode = scrapy.Field()
    livable_area = scrapy.Field()
    area = scrapy.Field()
    nb_rooms = scrapy.Field()
    nb_bedrooms = scrapy.Field()
    nb_levels = scrapy.Field()
    buildable = scrapy.Field()
    address = scrapy.Field()
    year = scrapy.Field()
    nb_garage = scrapy.Field()
    neighborhood = scrapy.Field()
    exposition = scrapy.Field()
