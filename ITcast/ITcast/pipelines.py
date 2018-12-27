# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.conf import settings

import pymongo

class ItcastPipeline(object):

	def __init__(self):
		port = settings['MONGODB_PORT']
		host = settings['MONGODB_HOST']
		db_name = settings['MONGODB_DBNAME']
		client = pymongo.MongoClient(host=host, port=port)
		db = client[db_name]
		self.post = db[settings["MONGODB_DOCNAME"]]

	def process_item(self, item, spider):
		content=dict(item)
		self.post.insert(content)
		return item

	'''def __init__(self):
		self.f=open("itcast_pipeline.json", "w")

	def process_item(self, item, spider):
		content=json.dumps(dict(item), ensure_ascii=False) + "\n"
		self.f.write(content.encode("utf-8"))
		return item

	def close_spider(self, spider):
		self.f.close()'''