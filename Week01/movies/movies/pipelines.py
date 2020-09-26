# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd


class MoviesPipeline:
    def process_item(self, item, spider):
        title = item['title']
        movie_type = item['movie_type']
        movie_date = item['movie_date']

        output_list = [title, movie_type, movie_date]
        
        movie1 = pd.DataFrame(data=output_list)
        # mode = 'a+' 进行追加写入
        # movie1.to_csv('./movies.csv', encoding='gbk',mode='a+', index=False, header=False)
        movie1.to_csv('./movies.csv', encoding='utf-8',mode='a+', index=False, header=False)

        return item
