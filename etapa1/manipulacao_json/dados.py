import json
import os 

#No documento csv entre os nomes das colunas não pode haver acentos, espaços ou caracteres especiais, pois isso pode causar problemas na leitura e escrita do arquivo.
campos = ['nome', 'tipo', 'ano_lancamento', 'classificacao']

caminho = 'biblioteca.json'

def inicializar_diretorio():
    if not os.path.exists(caminho):
        os.makedirs(caminho)
        
        
def salvar_no_arquivo(lista_dados):
    inicializar_diretorio()
    with open(caminho, "w", encoding="utf-8", newline="") as arquivo:        
        #json.dump pega um objeto Python e escreve no arquivo
        json.dump(lista_dados, arquivo, ensure_ascii=False, indent=4)

        #Sem 'indent', o JSON fica comprimido numa linha só (difícil de ler):
        #Por padrão, Python converte caracteres especiais para código Unicode, com 'ensure_ascii=False', mantém os caracteres normais:
        
def carregar_do_arquivo():
    if os.path.exists(caminho):
        
        #Lista que receberá os dicionários de cada linha do documento, ou seja, cada jogo e suas respectivas informações
        biblioteca_aux = [] 
        with open(caminho, "r", encoding="utf-8") as arquivo:
            biblioteca_aux = json.load(arquivo) # Carrega o JSON e já retorna como objeto Python (lista, dicionário, etc.)
        return biblioteca_aux # Retorna os dados carregados
    return []