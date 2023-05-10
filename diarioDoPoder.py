from crawler import Crawler

class Diario_do_Poder(object):
    def __init__(self):
     #Visitando o site
        crawler = Crawler()
        crawler.get_url('https://diariodopoder.com.br/')

     #Localização as ultimas noticias da pagina inicial no HTML do site
        xpath ='//*[@id="ddp-main"]/div/div/div/div/div/div/div/article/a'
        e_list = crawler.get_elements(xpath, wait_time= 10)

     #Colocando as noticias em uma lista, com titulo e link
        noticias = [[]]
        for element in e_list:
            titulo = element.text
        # Tirando as categorias e \n antes do titulo
            barra_n = int(titulo.index("\n"))
            titulo = titulo[barra_n+1::]
        # tirando o subtitulo e amais
            url = element.get_attribute('href')
            linha = ['Diário do Poder', titulo, url]
            noticias.append(linha)
        noticias.remove([])

        self.noticias = noticias
