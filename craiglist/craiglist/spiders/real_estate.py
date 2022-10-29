import scrapy
from ..items import CraiglistItem


class RealEstateSpider(scrapy.Spider):
    name = 'real_estate'
    allowed_domains = ['newyork.craigslist.org']
    start_urls = ['res']

    print("yoyoy")

    def parse(self, response, *args, **kwargs):
        all_ads = response.css("div.gallery-card")
        print("yoyoyx2")
        for ad in all_ads:
            print("yoyoyx3")
            # items = CraiglistItem()

            post_date_title = ad.css("a.post-title")
            # items["post_date"] = post_date_title.css("time.post-date::text").get()
            # items["title"] = post_date_title.css("span.label::text").get()
            #
            # items["link"] = ad.css("a.cl-gallery empty::attr(href)").get()
            #
            # print("yoyo", items["post_date"])
            #
            # yield items

            yield {"title":  post_date_title.get()}
            # need a middleware - a headless browser to execute JS
