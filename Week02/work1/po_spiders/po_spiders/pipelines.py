# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class PoSpidersPipeline:
    def process_item(self, item, spider):
        film_name = item['film_name']
        film_type = item['film_type']
        film_time = item['film_time']
        output = f'{film_name},{film_type},{film_time}\n'
        # with open('./maoyan.csv', 'a+', encoding='utf-8') as article:
        #     article.write(output)
        conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       password = '12345678',
                       database = 'test_db',
                       charset = 'utf8mb4'
                        )
        con1 = conn.cursor()
        try:
            con1.execute("INSERT INTO moives(name,type,time) values('%s','%s','%s')" % (film_name,film_type,film_time))
            con1.close()
            conn.commit()
        except:
            conn.rollback()
        conn.close()
        return item
