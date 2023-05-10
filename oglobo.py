from crawler import Crawler
from selenium import webdriver as webdriver
import time
if __name__ == '__main__':
 #Visitando o site
    crawler = Crawler()
    crawler.get_url('https://oglobo.globo.com/ultimas-noticias/')




 #Localização das ultimas noticias no HTML do site
    xpath ='//*[@id="feed-placeholder"]/div/div/div/div/div/div/div/div/div/div/div/div/h2/a'
    e_list = crawler.get_elements(xpath, wait_time= 10)

 #Colocando as noticias em uma lista, com titulo e link
    noticias = [['Titulo', 'URL']]
    for element in e_list:
        titulo = element.text
        url = element.get_attribute('href')
        linha = [titulo, url]
        noticias.append(linha)
    for row in noticias:
        print(row)