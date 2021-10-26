import scrapy
from ..items import QuotextItem

# In order to run the file
# cd into the scrapy/quotext
# scrapy crawl ThisIsTheName (name of spider)
# scrapy crawl ThisIsTheName -o title.json (for json file output)


class QuoteSpider(scrapy.Spider):
    name = 'ThisIsTheName' # spider name
    start_urls = [ # urls to scrape
        'http://quotes.toscrape.com/'
    ]

    def parse(self,response):
        # number 1
        # title = respone.css('title::text').extract() # extracting the title of the first element on the scrape page
        # yield {'titletext' : title} # returns a dictionary. Scrapy uses a generator so you need to use the keyword yield

        # number 2
        # all_scrape_quotes = response.css('.quote')
        # title = all_scrape_quotes.css('span.text::text').extract()
        # tag = all_scrape_quotes.css('.author::text').extract()

        # number 3
            # command for runing scrapy crawl "ThisIsTheName" -o quotes.json
        # for quote in all_scrape_quotes:
        #     #title = quote.css('span.text::text').replace('"','').extract()
        #     title = [quote.replace('\u201c','') for quote in quote.css('span.text::text').extract()] # replacing the quote part of it
        #     tags = quote.css('.tag::text').extract() 
        #     author = quote.css('.author::text').extract()
        #     yield {
        #         'title': title,
        #         'tags': tags,
        #         'author': author
        #     }

        # number 4

        # initiate items 
        items = QuotextItem()

        # get initial response
        all_scrape_quotes = response.css('.quote')

        # Loop through all the responses
        for quote in all_scrape_quotes:
            #title = quote.css('span.text::text').replace('"','').extract()
            title = [quote.replace('\u201c','').replace('\u201d','') for quote in quote.css('span.text::text').extract()] # replacing the quote part of it
            tags = quote.css('.tag::text').extract() 
            author = quote.css('.author::text').extract()

            items['title'] = title
            items['tags'] = tags
            items['author'] = author 

            yield items
