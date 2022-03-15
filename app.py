import os
from PyPDF2 import PdfFileReader

diretorio = ''
qnt_paginas = 0
qnt_arquivos = 0

diretorio = input(r'Insira o diretório: ')

# a função walk percorre todos os subdiretórios, incluindo os ocultos
arquivos_listados = os.walk(diretorio)

# ele retorna pasta, subpasta e os arquivos
for diretorio, subpastas, arquivos in arquivos_listados:
    #percorrendo pelos arquivos
    for arquivo in arquivos:
        #se o arquivo for pdf, será lido pelo PyPDF2 e retonará a quantidade total de páginas.
        if arquivo.lower().endswith('.pdf'):
            pdf = PdfFileReader(open(f'{diretorio}\{arquivo}','rb'), strict=False)
            qnt_paginas += pdf.getNumPages()
            qnt_arquivos += len(arquivos)

print(f'O total de páginas é: {qnt_paginas} | de um total de {qnt_arquivos} arquivos')