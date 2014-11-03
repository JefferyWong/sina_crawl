import scrapy
import re

from sina.items import SinaItem
from scrapy.http import Request

class SinaSpider(scrapy.Spider):
	"""docstring for SinaSpider"""
	name = "sina"
	allowed_domains = ["sina.com.cn"]
	start_urls = [
		"http://www.sina.com.cn/",
	]

	def parse(self, response):
		for sel in response.css('ul li a'):
			item = SinaItem()
			item['a'] = sel.xpath('text()').extract()
			item['b'] = sel.css('b').xpath('text()').extract()
			item['span'] = sel.css('span').xpath('text()').extract()
			item['i'] = sel.css('i').xpath('text()').extract()
			urls = sel.xpath('//a/@href').extract()
			for url in urls:
				if re.match(r'^https?:/{2}\w.+$', url):
					yield Request(url)
			yield item
		for sel in response.css('p'):
			item = SinaItem()
			item['p'] = sel.xpath('text()').extract()
			item['span'] = sel.css('p span').xpath('text()').extract()
			item['strong'] = sel.css('p strong').xpath('text()').extract()
			yield item
