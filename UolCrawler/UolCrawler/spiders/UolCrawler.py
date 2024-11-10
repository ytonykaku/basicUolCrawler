import scrapy

class NoticiasSpider(scrapy.Spider):
    name = 'noticias'
    start_urls = ['https://noticias.uol.com.br']

    def parse(self, response):
        # Seleciona cada componente de notícia
        for noticia in response.css('div.thumbnails-item'):
            # Extrai o título dentro do h3 com a classe 'thumb-title'
            titulo = noticia.css('h3.thumb-title::text').get()
            # Extrai o link da manchete
            link = noticia.css('a::attr(href)').get()
            
            yield {
                'manchete': titulo,
                'link': link
            }
