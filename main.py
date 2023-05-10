from diarioDoPoder import Diario_do_Poder
from conjur import Conjur
from diario_nordeste import Diario_do_Nordeste
from cn7 import CN7
from focus import Focus
from folhadSpaulo import Folha_de_Sao_Paulo
from jota import Jota
from migalhas import Migalhas
from opovo import O_Povo
import requests

if __name__ == '__main__':

    token = "6015589290:AAEEc7rQchPSqH3R5mZea5f1XvMivRt1vHA"
    chat_id = -952045960

    cn7 = CN7()
    for row in cn7.noticias:
        print(row)
        message = row
        url_get = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        response = requests.get(url_get)

    conjur = Conjur()
    for row in conjur.noticias:
        print(row)
        message = row
        url_get = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        response = requests.get(url_get)

    diario_do_nordeste = Diario_do_Nordeste()
    for row in diario_do_nordeste.noticias:
        print(row)
        message = row
        url_get = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        response = requests.get(url_get)

    diarioDoPoder = Diario_do_Poder()
    for row in diarioDoPoder.noticias:
        print(row)
        message = row
        url_get = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        response = requests.get(url_get)

    focus = Focus()
    for row in focus.noticias:
        print(row)
        message = row
        url_get = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        response = requests.get(url_get)

    folha = Folha_de_Sao_Paulo()
    for row in folha.noticias:
        print(row)
        message = row
        url_get = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        response = requests.get(url_get)
        
    jota = Jota()
    for row in jota.noticias:
        print(row)
        message = row
        url_get = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        response = requests.get(url_get)
      
    migalhas = Migalhas()
    for row in migalhas.noticias:
        print(row)
        message = row
        url_get = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        response = requests.get(url_get)
   
    opovo = O_Povo()
    for row in opovo.noticias:
        print(row)
        message = row
        url_get = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        response = requests.get(url_get)




