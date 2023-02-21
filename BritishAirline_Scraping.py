# import scrapy library
import scrapy


# Create class
class BritishAirlineReview(scrapy.Spider):

    name = 'BritishAirlineReview'
    start_urls = ['https://www.airlinequality.com/airline-reviews/british-airways', ]

    def parse(self, response):
        for review in response.css('article[itemprop=review]'):
            yield {'name': review.css('h3.text_sub_header>span>span::text').getall(),
                   'country': review.css('h3.text_sub_header::text').getall(),
                   'posting_date': review.css('h3.text_sub_header>time::text').getall(),
                   'review_headline': review.css('h2::text').getall(),
                   'reviews': review.css('div.tc_mobile>div.text_content::text').getall(),
                   'rating': review.css('div[itemprop=reviewRating]>span::text').getall(),
                   'travel-detailed': review.css('table.review-ratings>tr:nth-last-child(12)>td:nth-child(2)::text').getall(),
                   'seat_comfort': review.css('table.review-ratings>tr:nth-last-child(7)>td.review-rating-stars>span.star.fill::text').getall(),
                   'cabin_staff_service': review.css('table.review-ratings>tr:nth-last-child(6)>td.review-rating-stars>span.star.fill::text').getall(),
                   'food & beverages': review.css('table.review-ratings>tr:nth-last-child(5)>td.review-rating-stars>span.star.fill::text').getall(),
                   'ground_services': review.css('table.review-ratings>tr:nth-last-child(4)>td.review-rating-stars>span.star.fill::text').getall(),
                   'wifi & connectivity': review.css('table.review-ratings>tr:nth-last-child(3)>td.review-rating-stars>span.star.fill::text').getall(),
                   'value_for_money': review.css('table.review-ratings>tr:nth-last-child(2)>td.review-rating-stars>span.star.fill::text').getall(), }

        # to handling pagination
        next_page = response.css('div.col-content>article>ul>li:nth-last-child(1) a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
