import scrapy
from kinopoisk.items import MovieItem

class LikeSpider(scrapy.Spider):
    """docstring for LikeSpider."""
    name = 'like'
    allowed_domains = ['kinopoisk.ru']

    def start_requests(self):
        with open('/home/sv9t/kinopoisk/data/startlinks.txt') as fp:
            urls = [line[:-1] for line in fp]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse,
                meta={'proxy':'http://YOUR_PROXY_IP:PORT'})

    def parse(self, response):
        item = MovieItem()
        item['director'] = response\
            .xpath('//td[@itemprop="director"]//a/text()').extract_first()
        item['genre'] = response\
            .xpath('//span[@itemprop="genre"]//a/text()').extract_first()
        item['movie_id'] = response.url.split('-')[-1][:-1]
        item['date'] = response\
            .xpath('//meta[@itemprop="dateCreated"]/@content').extract_first()
        item['country'] = response\
            .xpath('//table[@class="info"]//tr[2]//a/text()').extract_first()
        item['name'] = response.xpath('//h1[@itemprop="name"]/text()').extract_first()

        yield scrapy.Request(url=response.url + 'like/',
             callback=self.parse_like,
             meta={'item':item, 'proxy':'http://YOUR_PROXY_IP:PORT'})


    def parse_like(self, response):
        old_item = response.request.meta['item']
        old_item['like'] = response.xpath('//a[@class=" b_gray i_orig"]')\
            .xpath('@href').extract()

        urls = ['https://kinopoisk.ru/' + film for film in old_item['like']]
        new_requests = []
        for url in urls:
            new_requests.append(scrapy.Request(url=url, callback=self.parse,
                meta={'proxy':'http://YOUR_PROXY_IP:PORT'}))

        return [old_item] + list(new_requests)
