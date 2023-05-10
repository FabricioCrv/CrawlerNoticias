from crawler import Crawler

class CN7 (object):
    def __init__(self):
        crawler = Crawler()
    #Pagina 1
        crawler.get_url('https://cn7.com.br/ultimas-noticias/page/1')

        xpath_URL_1 = '//*[@class="list-latest-news"]/ul/li/article/a'
        e_list_URL_1 = crawler.get_elements(xpath_URL_1, wait_time=10)

        noticias_URL_1 = []
        for element in e_list_URL_1:
            URL = element.get_attribute('href')
            noticias_URL_1.append(URL)
        #print da URL
        """for row in noticias_URL_1:
            print(row)"""

        xpath_titulo_1 = '//*[@class="list-latest-news"]/ul/li/article/article/article[2]/a'
        e_list_titulo_1 = crawler.get_elements(xpath_titulo_1, wait_time=10)

        noticias_titulo_1 = []

        for element in e_list_titulo_1:
            titulo = element.text
            noticias_titulo_1.append(titulo)
        #print do titulo
        """for row in noticias_titulo_1:
            print(row)"""

        noticias = [[]]
        index = 0
        #print da pagina 1
        for element in noticias_URL_1:
            linha = ['CN7', noticias_titulo_1[index], noticias_URL_1[index]]
            noticias.append(linha)
            index = index + 1

    #Pagina 2
        crawler.get_url('https://cn7.com.br/ultimas-noticias/page/2')

        xpath_URL_2 = '//*[@class="list-latest-news"]/ul/li/article/a'
        e_list_URL_2 = crawler.get_elements(xpath_URL_2, wait_time=10)

        noticias_URL_2 = []
        for element in e_list_URL_2:
            URL = element.get_attribute('href')
            noticias_URL_2.append(URL)
        #print da URL
        """for row in noticias_URL:
            print(row)"""

        xpath_titulo_2 = '//*[@class="list-latest-news"]/ul/li/article/article/article[2]/a'
        e_list_titulo_2 = crawler.get_elements(xpath_titulo_2, wait_time=10)

        noticias_titulo_2 = []

        for element in e_list_titulo_2:
            titulo = element.text
            noticias_titulo_2.append(titulo)
        #print do titulo
        """for row in noticias_titulo:
            print(row)"""
        index = 0
        for element in noticias_URL_2:
            linha = ['CN7', noticias_titulo_2[index], noticias_URL_2[index]]
            noticias.append(linha)
            #print(linha)
            index = index + 1

        noticias.remove([])

        self.noticias = noticias