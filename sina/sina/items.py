# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class SinaItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	i = Field()
	span = Field()
	a = Field()
	b = Field()
	p = Field()
	strong = Field()
	url = Field()
