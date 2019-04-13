# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from Tools import Const

class Job51Pipeline(object):
    def __init__(self):
        self.connection = pymongo.MongoClient()
        self.db = self.connection['51job岗位信息']
        self.collection = self.db["python岗位技能点"]
    def process_item(self, item, spider):

        data = dict(item)
        self.collection.insert(data)
