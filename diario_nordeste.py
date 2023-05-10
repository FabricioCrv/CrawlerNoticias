from crawler import Crawler

class Diario_do_Nordeste (object):
    def __init__(self):
    #1a pagina
        crawler = Crawler()
        crawler.get_url('https://diariodonordeste.verdesmares.com.br/ultima-hora?page=1')

        xpath = '//*[@id="main-content"]/div/div/div/main/div/div/div/div[2]/h2/a'
        e_list= crawler.get_elements(xpath, wait_time=10)

        noticias = [[]]
        for element in e_list:
            titulo = element.text
            url = element.get_attribute('href')
            linha = ['Diário do Nordeste', titulo, url]
            noticias.append(linha)
    #Print da primeira pagina
        """for row in noticias:
            print(row)"""

    #2a pagina
        """crawler = Crawler()
        crawler.get_url('https://diariodonordeste.verdesmares.com.br/ultima-hora?page=2')

        xpath_2 = '//*[@id="main-content"]/div/div/div/main/div/div/div/div[2]/h2/a'
        e_list_2= crawler.get_elements(xpath_2, wait_time=10)

        for element in e_list_2:
            titulo = element.text
            url = element.get_attribute('href')
            linha = ['Diário do Nordeste', titulo, url]
            noticias.append(linha)
        #for row in noticias:
            #print(row)"""

        noticias.remove([])

        self.noticias = noticias

