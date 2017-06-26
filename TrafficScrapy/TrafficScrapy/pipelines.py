# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from .config import UserConfig

class TrafficscrapyPipeline(object):

    def __init__(self):
        self.connect = pymysql.connect(host=UserConfig['mysql_host'], port=UserConfig['mysql_port'],
                                       user=UserConfig['mysql_user'], passwd=UserConfig['mysql_passwd'],
                                       db=UserConfig['mysql_database'])
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        sql = 'INSERT INTO tra_info(`id`, `name`, `startName`, `endName`, `time`, `roadGrade`, `avgspeed`, ' \
              '`sIndex`, `cIndex`, `bIndex`, `dir`, `rticLonlats`, `rticId`, `vkt`) ' \
              'VALUES("{id}", "{name}", "{startName}", "{endName}", "{time}", {roadGrade}, {avgspeed}, {sIndex}, {cIndex}, ' \
              '{bIndex}, "{dir}", "{rticLonlats}", "{rticId}", "{vkt}")' \
              ''.format(id=item['id'], name=item['name'], startName=item['startName'], endName=item['endName'],
                        time=item['time'], roadGrade=item['roadGrade'], avgspeed=item['avgspeed'], sIndex=item['sIndex'],
                        cIndex=item['cIndex'], bIndex=item['bIndex'], dir=item['dir'], rticLonlats=item['rticLonlats'],
                        rticId=item['rticId'], vkt=item['vkt'])
        self.cursor.execute(sql)
        return item
