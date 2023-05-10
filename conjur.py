from crawler import Crawler

class Conjur (object):
    def __init__(self):
        #Visitando o site
        crawler = Crawler()
        crawler.get_url('https://www.conjur.com.br/')

     #Localização das ultimas noticias no HTML do site
        xpath ='//*[@id="more"]/section/ul[1]/li/a'
        e_list = crawler.get_elements(xpath, wait_time= 10)

     #Colocando as noticias em uma lista, com titulo e link
        noticias = [[]]
        for element in e_list:
            titulo = element.text
            url = element.get_attribute('href')
            linha = ['Conjur', titulo, url]
            noticias.append(linha)
        noticias.remove([])

        self.noticias = noticias