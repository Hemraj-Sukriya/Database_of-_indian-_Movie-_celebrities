import scrapy
from ..items import IndianmoviecelebritiesItem


class BollywoodSpider(scrapy.Spider):
    name = 'celebrities'
    start_urls = [
        'https://www.imdb.com/list/ls068010962/'
    ]

    def parse(self, response):
        items = IndianmoviecelebritiesItem()
        all_celebrities = response.css('div.mode-detail')



        for celebrity in all_celebrities:



          celebrity_image_link = celebrity.css('img::attr(src)').extract_first()
          celebrity_role = celebrity.css('p.text-small').css('::text').extract_first()
          celebrity_detail = celebrity.css('.text-small+ p').css('::text').extract_first()
          celebrity_name = celebrity.css('.lister-item-header a').css('::text').extract_first()

          items['celebrity_detail'] = celebrity_detail

          items['celebrity_name'] = celebrity_name
          items['celebrity_role'] = celebrity_role.strip()
          items['celebrity_image_link'] = celebrity_image_link


          yield items
