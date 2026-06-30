#módulo que cria arquivo csv

#importando módulos/classes que serão utilizadas ao longo do código
from funcoes import *
import csv 
import os

campos = ['mes', 'saldo', 'rendimento'] #colunas do arquivo

def salvar_arquivo(nome_arquivo):
    nome_documento = nome_arquivo + '.csv' #nome do arquivo escolhido pelo usuário mais sua extensão
    caminho = nome_documento 
    
    # em qualque hipótese, já tendo ou não 'caminho' será ecrito ou reescrito  
    with open(caminho, "w", encoding="utf-8", newline="") as arquivo: 
    # abra o arquivo com nome 'caminho' para escrever 'w' aceitando caracteres 'encoding="utf-8"' considerando a formatação original do documento 'newline=""' e apelide tudo isso de 'arquivo'
    
        escritor = csv.writer(arquivo) #cria um objeto 'escritor' que irá ter acesso de escrever no 'arquivo' csv 
        escritor.writerow(campos) #com o objeto chama o método 'writerow' para escrever o cabeçalho com nomes das colunas = a 'campos'
        escritor.writerows(investimento) #com o objeto chama o método 'writerows' para escrever o as listas que estão dentro da lista 'investimentp[]', sendo cada linha uma lista 
        
    return "Arquivo salvo" 
    