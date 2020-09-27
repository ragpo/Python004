# -*- coding: utf-8 -*-
import scrapy
from po_spiders.items import PoSpidersItem
from scrapy.selector import Selector

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/films?showType=3/']

    # def parse(self, response):
    #     pass
    # 打开猫眼的本地文件
    # f = open("Week01/work2/经典影片_电影大全_经典高清电影-猫眼电影.htm",'r')
    # response = f.read()
    # f.close

    def start_requests(self):
        url = f'http://maoyan.com/films?showType=3/'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        a = 0
        print('movies.extract(): ',movies.extract())
        
        for movie in movies:
            #print(movie.extract())
            item = PoSpidersItem()
            if a < 10:
                film_name = movie.xpath('./div[1]/span/text()')
                #print(film_name.extract_first())
                film_name = film_name.extract_first()
                print(film_name)
                
                film_type = movie.xpath('./div[2]/text()')
                #print(film_type.extract()[1].strip())  
                film_type = film_type.extract()[1].strip()
                print(film_type)

                film_time = movie.xpath('./div[4]/text()')
                #print(film_time.extract()[1].strip())
                film_time = film_time.extract()[1].strip()
                print(film_time)

                a+=1

                item['film_name'] = film_name
                item['film_type'] = film_type
                item['film_time'] = film_time
                yield item                
            else:
                break
        



#//div[@class="movie-item film-channel"]/div[2]/a/div/div[2]


# //*[@id="app"]/div/div[2]/div[2]/dl/dd[2]/div[1]/div[2]/a/div/div[2]
# //*[@id="app"]/div/div[2]/div[2]/dl/dd[3]/div[1]/div[3]/a/div/div[2]
#//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[1]
# //*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[1]/span
# //*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[4]/text()