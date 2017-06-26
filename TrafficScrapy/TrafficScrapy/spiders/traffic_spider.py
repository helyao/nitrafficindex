import json
import scrapy
from scrapy.http import FormRequest
from ..items import TrafficscrapyItem

CITY_CODE = '310000'
MAX_PAGE = 32

class MobikeSpider(scrapy.Spider):

    name = "traffic"

    url = 'http://www.nitrafficindex.com/traffic/getRoadIndex.do'
    body_static = {
        'areaCode': "310000",
        'roadLevel': "1,2,3,4",
        'rows': "50",
        'page': "1"
    }
    headers = {
        'Pragma': "no-cache",
        "Referer": "http://www.nitrafficindex.com/trafficIndexAnalysis.html",
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        'Accept': "application/json, text/javascript, */*",
        'Connection': "keep-alive",
        'Origin': "http://www.nitrafficindex.com",
        'Cache-Control': "no-cache",
        'X-Requested-With': "XMLHttpRequest",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4'
    }

    def __getDynamicBody(self, index):
        body = {
            'areaCode': "{}".format(CITY_CODE),
            'roadLevel': "1,2,3,4",
            'rows': "50",
            'page': "{}".format(index)
        }
        return body

    def start_requests(self):
        for item in range(1, MAX_PAGE):
            body = self.__getDynamicBody(item)
            yield FormRequest(url=self.url, formdata=body, headers=self.headers, callback=self.parse, errback=self.parse_error)

    def parse(self, response):
        results = json.loads(response.body.decode('utf-8'))
        date = results['date']
        for row in results['rows']:
            item = TrafficscrapyItem()
            item['time'] = date
            item['id'] = row['id']
            item['name'] = row['name']
            item['roadGrade'] = row['roadGrade']
            item['avgspeed'] = row['avgspeed']
            item['cIndex'] = row['cIndex']
            item['sIndex'] = row['sIndex']
            item['bIndex'] = row['bIndex']
            item['dir'] = row['dir']
            item['startName'] = row['startName']
            item['endName'] = row['endName']
            item['rticId'] = row['rticId']
            item['vkt'] = row['vkt']
            item['rticLonlats'] = row['rticLonlats']
            yield item

    def parse_error(self):
        # write error in log
        print('Error found.')


