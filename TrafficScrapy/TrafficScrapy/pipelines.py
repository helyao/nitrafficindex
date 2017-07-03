# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from TrafficScrapy import settings

class TrafficscrapyPipeline(object):

    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=settings.MYSQL_PORT,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            db=settings.MYSQL_DATABASE,
            use_unicode=True,
            charset="utf8"
        )
        self.cursor = self.connect.cursor()
        self.table_name = settings.MYSQL_TABLE_INFO

    def process_item(self, item, spider):
        try:
            sql = 'INSERT INTO %s(`id`, `name`, `startName`, `endName`, `time`, `roadGrade`, `avgspeed`, ' \
                  '`sIndex`, `cIndex`, `bIndex`, `dir`, `rticLonlats`, `rticId`, `vkt`) ' \
                  'VALUES("%s", "%s", "%s", "%s", "%s", %s, %s, %s, %s, %s, ' \
                  '"%s", "%s", "%s", "%s")' % (self.table_name, item['id'], item['name'], item['startName'],
                                               item['endName'], item['time'], item['roadGrade'], item['avgspeed'],
                                               item['sIndex'], item['cIndex'], item['bIndex'], item['dir'],
                                               item['rticLonlats'], item['rticId'], item['vkt'])
            # print(sql)
            self.cursor.execute(sql)
            self.connect.commit()
        except:
            pass
        return item
