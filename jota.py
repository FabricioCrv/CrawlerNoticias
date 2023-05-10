from crawler import Crawler

class Jota (object):
    def __init__(self):
    #Visitando o site
        crawler = Crawler()
        crawler.get_url('https://www.jota.info/')

    #Localização das ultimas noticias no HTML do site
        xpath ='//*[@id="last_news"]/section/div/article/div/h3/a'
        e_list = crawler.get_elements(xpath, wait_time= 10)

    #Colocando as noticias em uma lista, com titulo e link
        noticias = [[]]
        for element in e_list:
            titulo = element.text
            url = element.get_attribute('href')
            linha = ['Jota', titulo, url]
            noticias.append(linha)
        """for row in noticias:
            print(row)"""


    #Localizando as noticias de categorias 'poder', 'tributos' e 'saude'
        xpath2 = '//*[@id="second"]/div/ul/li/a'
        e_list2 = crawler.get_elements(xpath2, wait_time= 10)


        for element in e_list2:
            titulo = element.text
            barra_n = int(titulo.index("\n"))
            titulo = titulo[barra_n + 1::]
            url = element.get_attribute('href')
            linha = ['Jota', titulo, url]
            noticias.append(linha)
        #for row in noticias:
            #print(row)
        noticias.remove([])

        self.noticias = noticias