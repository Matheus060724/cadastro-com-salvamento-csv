from cadastro import banco_dados
import csv

with open('dados.csv', 'a', newline='') as arquivo:
    escritor_csv = csv.writer(arquivo)
    for linha in banco_dados:
        escritor_csv.writerow(linha)
