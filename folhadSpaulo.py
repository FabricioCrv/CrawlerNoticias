from crawler import Crawler

class Folha_de_Sao_Paulo (object):
    def __init__(self):

        crawler = Crawler()
        crawler.get_url('https://www1.folha.uol.com.br/ultimas-noticias/#top')

    #noticia de destaque
        xpath_1 ='//*[@id="conteudo"]/div[1]/div[1]/div/div/div[1]/div/div/ol/li/div[2]/a'
        e_list_1 = crawler.get_elements(xpath_1, wait_time= 10)


        noticias = [[]]
        for element in e_list_1:
            titulo = element.text
            barra_n = int(titulo.index("\n"))
            titulo = titulo[:barra_n:]
            url = element.get_attribute('href')
            linha = ['Folha de São Paulo', titulo, url]
            noticias.append(linha)
        #print da noticia de destaque
        """for row in noticias:
            print(row)"""

    #Ultimas noticias
        xpath_2 ='//*[@id="conteudo"]/div[1]/div[2]/div/div/div[1]/div/div/div/ol/li/div[2]/div[2]/a'
        e_list_2 = crawler.get_elements(xpath_2, wait_time= 10)


        for element in e_list_2:
            if element.text != "":
                titulo = element.text
                barra_n = int(titulo.index("\n"))
                titulo = titulo[:barra_n:]
                url = element.get_attribute('href')
                linha = ['Folha de São Paulo', titulo, url]
                noticias.append(linha)
        #for row in noticias:
            #print(row)
        noticias.remove([])

        self.noticias = noticias