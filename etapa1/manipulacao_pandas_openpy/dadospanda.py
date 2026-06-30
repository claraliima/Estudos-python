import pandas as pd # pd = apelido para chamar ao longo do código funções/métodos da biblioteca pandas
 
import os

PASTA = "arquivos"
CAMINHO_ARQUIVO = os.path.join(PASTA, "biblioteca_pandas.xlsx")

def inicializar_diretorio():
    
    # Função para criar diretório caso não exista com nome da var PASTA
    if not os.path.exists(PASTA): 
        os.makedirs(PASTA)

def salvar_no_arquivo(lista_dados):
    inicializar_diretorio()
    df = pd.DataFrame(lista_dados) # Var 'df' recebe = Transformação de  lista_dados em um dataframe(tabela, semelhante a planilha Excel), cada item vira uma linha no dataframe
    
    df.to_excel(CAMINHO_ARQUIVO, index=False, engine='openpyxl') # Salva o dataframe em um arquivo xlsx(Excel) com nome 'CAMINHO_ARQUIVO'. 'index=False' parâmetro que signfica que o índice do dataframe não será add como coluna no Excel. 'engine='openpyxl' parâmetro que significa que a escrita do xlsx será delegada para a biblioteca openpyxl

def carregar_do_arquivo():
    if os.path.exists(CAMINHO_ARQUIVO):
        
        df = pd.read_excel(CAMINHO_ARQUIVO, engine='openpyxl') #Lê o arquivo excel com nome 'CAMINHO_ARQUIVO' que tem como escrita openpyxl
        
        return df.fillna('').to_dict(orient='records') # 'df.fillna('')' substitui valores null por strings vazias. 'to_dict(orient='records')' converte o dataframe para uma lista de dicionários onde cada linha da tabela vira um dicionário e as colunas são as chaves
    
    return [] # Retorna uma lista vazia caso o 'CAMINHO_ARQUIVO' não exista, ou seja, não tem o que carregar do arquivo