# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from .basefunc import GetTimeStamp
from TrafficScrapy import settings

class TrafficscrapyPipeline(object):

    # def __init__(self):
    #     self.connect = pymysql.connect(
    #         host=settings.MYSQL_HOST,
    #         port=settings.MYSQL_PORT,
    #         user=settings.MYSQL_USER,
    #         passwd=settings.MYSQL_PASSWD,
    #         db=settings.MYSQL_DATABASE
    #     )
    #     self.cursor = self.connect.cursor()
    #     self.table_info = settings.MYSQL_TABLE_INFO + '_' + GetTimeStamp()
    #     self.cursor.execute('create table {table} like {seed}'.format(table=self.table_info, seed=settings.MYSQL_TABLE_INFO))

    def process_item(self, item, spider):
        sql = 'INSERT INTO tra_info(`id`, `name`, `startName`, `endName`, `time`, `roadGrade`, `avgspeed`, ' \
              '`sIndex`, `cIndex`, `bIndex`, `dir`, `rticLonlats`, `rticId`, `vkt`) ' \
              'VALUES("{id}", "{name}", "{startName}", "{endName}", "{time}", {roadGrade}, {avgspeed}, {sIndex}, {cIndex}, ' \
              '{bIndex}, "{dir}", "{rticLonlats}", "{rticId}", "{vkt}")' \
              ''.format(id=item['id'], name=item['name'], startName=item['startName'], endName=item['endName'],
                        time=item['time'], roadGrade=item['roadGrade'], avgspeed=item['avgspeed'],
                        sIndex=item['sIndex'],
                        cIndex=item['cIndex'], bIndex=item['bIndex'], dir=item['dir'], rticLonlats=item['rticLonlats'],
                        rticId=item['rticId'], vkt=item['vkt'])
        print(sql)
        # try:
        #     sql = 'INSERT INTO tra_info(`id`, `name`, `startName`, `endName`, `time`, `roadGrade`, `avgspeed`, ' \
        #           '`sIndex`, `cIndex`, `bIndex`, `dir`, `rticLonlats`, `rticId`, `vkt`) ' \
        #           'VALUES("{id}", "{name}", "{startName}", "{endName}", "{time}", {roadGrade}, {avgspeed}, {sIndex}, {cIndex}, ' \
        #           '{bIndex}, "{dir}", "{rticLonlats}", "{rticId}", "{vkt}")' \
        #           ''.format(id=item['id'], name=item['name'], startName=item['startName'], endName=item['endName'],
        #                     time=item['time'], roadGrade=item['roadGrade'], avgspeed=item['avgspeed'], sIndex=item['sIndex'],
        #                     cIndex=item['cIndex'], bIndex=item['bIndex'], dir=item['dir'], rticLonlats=item['rticLonlats'],
        #                     rticId=item['rticId'], vkt=item['vkt'])
        #     self.cursor.execute(sql)
        #     self.connect.commit()
        # except Exception as ex:
        #     print(ex)
        return item
