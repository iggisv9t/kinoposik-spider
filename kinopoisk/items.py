# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MovieItem(scrapy.Item):
    '''Movie scraped info'''
    movie_id = scrapy.Field()
    name = scrapy.Field()
    like = scrapy.Field()
    genre = scrapy.Field()
    date = scrapy.Field()
    country = scrapy.Field()
    director = scrapy.Field()
