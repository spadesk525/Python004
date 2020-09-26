# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from movies.items import MoviesItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

#    def parse(self, response):
#        pass


    def start_request(self):
        
        url = 'https://maoyan.com/films?showType=3'

        return scrapy.Request(url=url, callback=self.parse, dont_filter=False)


    def parse(self, response):
        print("--------------")
        print(response.url)
        print("--------------")
        i = 0
        movie_div = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for tags in movie_div:
            item = MoviesItem()
            title_element = tags.xpath('./div/span[1]/text()')
            movie_type_element = tags.xpath('./div[2]/text()') 
            movie_date_element = tags.xpath('./div[4]/text()') 
            # print(f"title:{title_element.extract()[0]}")
            # print(f"movie_type:{movie_type_element}")
            # print(f"movie_data:{movie_date_element}")
            title = title_element.extract()[0]
            movie_type = title_element.extract()[1] + self.process_data(movie_type_element.extract()[1]) 
            movie_date = title_element.extract()[3] + self.process_data(movie_date_element.extract()[1]) 
            item['title'] = title
            item['movie_type'] = movie_type
            item['movie_date'] = movie_date

            if i < 10 :
                i += 1
                yield item
            else:
                break


    def process_data(self, a_str):
        temp = a_str.replace(" ", "")
        return temp.replace("\n", "")




