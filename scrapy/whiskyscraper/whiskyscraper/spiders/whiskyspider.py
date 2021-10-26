import scrapy


class WhiskySpider(scrapy.Spider): 
    name = 'whisky'
    start_urls = ['https://www.whiskyshop.com/catalogsearch/result/index/?q=scotch&item_availability=In+Stock'] #urls to scrap

    def parse(self, response): # use self because it's the function within this class
        for products in response.css('div.product-item-info'):
            try: 
                yield { #scrappy uses yield (I think it's a generator)
                    'name': products.css('a.product').attrib['data-name'],
                    'price':products.css('a.product').attrib['data-price'],
                    'link': products.css('a.product').attrib['href'],
                }
            except:
                yield { #scrappy uses yield (I think it's a generator)
                    'name': products.css('a.product').attrib['data-name'],
                    'price':"sold out",
                    'link': products.css('a.product').attrib['href'],
                }
        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)