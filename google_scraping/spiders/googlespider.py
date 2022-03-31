import scrapy
from google_scraping.items import GoogleScrapingItem
from scrapy.loader import ItemLoader
from scrapy_splash import SplashRequest
from scrapy_scrapingbee import ScrapingBeeSpider, ScrapingBeeRequest


# class GoogleSpider(ScrapingBeeSpider):
class GoogleSpider(scrapy.Spider):
    name = 'google'

    start_urls = ['https://www.google.com/maps/search/hotel+murten/@46.9175604,7.1284949,12z/data=!3m1!4b1']


    def parse(self, response):
        pass

