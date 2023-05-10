from crawler import Crawler

class O_Povo (object):
    def __init__(self):
     #Visitando o site
        crawler = Crawler()
        crawler.get_url('https://www.opovo.com.br/noticias')

     #Localização das ultimas noticias no HTML do site
        xpath ='/html/body/div[7]/div/div/div/div/a'
        e_list = crawler.get_elements(xpath, wait_time= 10)

     #Colocando as noticias em uma lista, com titulo e link
        noticias = [[]]
        for element in e_list:
            titulo = element.text
        #Tirando as categorias e \n antes do titulo
            barra_n = int(titulo.index("\n"))
            titulo = titulo[barra_n+1::]
        #tirando o subtitulo e amais
            barra_n = int(titulo.index("\n"))
            titulo = titulo[:barra_n:]
            url = element.get_attribute('href')
            linha = ['O Povo', titulo, url]
            noticias.append(linha)
        #for row in noticias:
            #print(row)
        noticias.remove([])

        self.noticias = noticias