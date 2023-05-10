from crawler import Crawler

class Focus (object):
    def __init__(self):
     #Visitando o site
        crawler = Crawler()
        crawler.get_url('https://www.focus.jor.br/')

     #Localização das ultimas noticias no HTML do site
        xpath ='//*[@id="main"]/section[4]/div/div/ul/li/div/h3/a'
        e_list = crawler.get_elements(xpath, wait_time= 10)

     #Colocando as noticias em uma lista, com titulo e link
        noticias = [[]]
        for element in e_list:
            titulo = element.text
            url = element.get_attribute('href')
            linha = ['Focus', titulo, url]
            noticias.append(linha)
        """for row in noticias:
            print(row)"""

     #noticias categoria 'Multi'
        """crawler2 = Crawler()
        crawler2.get_url('https://www.focus.jor.br/multi/')

        xpath2 = '//*[@id="main"]/section/div/div/ul/li/div/h3/a'
        e_list2 = crawler2.get_elements(xpath2, wait_time= 10)

        for element in e_list2:
            titulo = element.text
            url = element.get_attribute('href')
            linha = ['Focus', titulo, url]
            noticias.append(linha)"""
        noticias.remove([])

        self.noticias = noticias