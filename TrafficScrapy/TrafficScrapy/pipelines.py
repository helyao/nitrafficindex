# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from .basefunc import GetTimeStamp

class TrafficscrapyPipeline(object):

    def __init__(self, connect, table_info):
        self.connect = connect
        self.cursor = connect.cursor()
        self.table_info = table_info

    # Get Mysql Connection from settings.py
    @classmethod
    def from_settings(cls, settings):
        connect = pymysql.connect(host=settings['MYSQL_HOST'], port=settings['MYSQL_PORT'],
                                  user=settings['MYSQL_USER'], passwd=settings['MYSQL_PASSWD'],
                                  db=settings)
        table_info = settings['MYSQL_TABLE_INFO'] + '_' + GetTimeStamp()
        return cls(connect, table_info)

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
