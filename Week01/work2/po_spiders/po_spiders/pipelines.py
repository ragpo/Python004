# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class PoSpidersPipeline:
    def process_item(self, item, spider):
        film_name = item['film_name']
        film_type = item['film_type']
        film_time = item['film_time']
        output = f'{film_name},{film_type},{film_time}\n'
        with open('./maoyan.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
