from diarioDoPoder import Diario_do_Poder
from conjur import Conjur
from diario_nordeste import Diario_do_Nordeste
from cn7 import CN7
from focus import Focus
from folhadSpaulo import Folha_de_Sao_Paulo
from jota import Jota
from migalhas import Migalhas
from opovo import O_Povo
import xlsxwriter
import csv

if __name__ == '__main__':
    noticias = [['Site','Notícia','Link']]

    cn7 = CN7()
    for row in cn7.noticias:
        print(row)
    noticias.extend(cn7.noticias)

    conjur = Conjur()
    for row in conjur.noticias:
        print(row)
    noticias.extend(conjur.noticias)

    diario_do_nordeste = Diario_do_Nordeste()
    for row in diario_do_nordeste.noticias:
        print(row)
    noticias.extend(diario_do_nordeste.noticias)

    diarioDoPoder = Diario_do_Poder()
    for row in diarioDoPoder.noticias:
        print(row)
    noticias.extend(diarioDoPoder.noticias)

    focus = Focus()
    for row in focus.noticias:
        print(row)
    noticias.extend(focus.noticias)

    folha = Folha_de_Sao_Paulo()
    for row in folha.noticias:
        print(row)
    noticias.extend(folha.noticias)

    jota = Jota()
    for row in jota.noticias:
        print(row)
    noticias.extend(jota.noticias)

    migalhas = Migalhas()
    for row in migalhas.noticias:
        print(row)
    noticias.extend(migalhas.noticias)

    opovo = O_Povo()
    for row in opovo.noticias:
        print(row)
    noticias.extend(opovo.noticias)




#Create XLSX

    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('noticias.xlsx')
    worksheet = workbook.add_worksheet()

    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0

    # Iterate over the data and write it out row by row.
    for site, title, link in noticias:
        worksheet.write(row, col, site)
        worksheet.write(row, col + 1, title)
        worksheet.write(row, col + 2, link)
        row += 1

    workbook.close()

#Create CSV
    """with open('noticias.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(noticias)"""