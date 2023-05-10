from crawler import Crawler
import re

class Migalhas (object):
    def __init__(self):
        crawler = Crawler()
        crawler.get_url("https://www.migalhas.com.br/quentes")

        xpath = '//*[@class="colunas"]/article/app-base-asset/app-no-v18/a'
        e_list = crawler.get_elements(xpath, wait_time= 10)

        noticias = [[]]
        for element in e_list:
            extraction = element.text

        #Tirando o \n do começo e final e a data
            titulo = extraction[11:-2]

        #Para retirar o \n e o subtitulo na sequencia
            barra_n = int(titulo.index("\n"))
            titulo = titulo[:barra_n:]

            url = element.get_attribute('href')
            linha = ['Migalhas', titulo, url]
            noticias.append(linha)
        #for row in noticias:
            #print(row)
        noticias.remove([])

        self.noticias = noticias