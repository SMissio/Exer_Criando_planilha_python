from openpyxl import load_workbook
import os

caminho_arquivo = "C:\\Users\\SylviaMissio\\Desktop\\RPA1\\openpyxl\\InserirDados.xlsx"

plan_aberta = load_workbook(filename=caminho_arquivo)

sheet_seleciona = plan_aberta['Aluno']

dadosTabela = [
    ['Nome','Idade'],
    ['Berenice',28],
    ['Caio',32],
    ['Nicole',34],
    ['Leonardo',38],
    ['Amanda',25]
]

for linhaPlan in dadosTabela:
    sheet_seleciona.append(linhaPlan)
plan_aberta.save(filename=caminho_arquivo)

os.startfile(caminho_arquivo)