import sqlite3
import os

PASTA = "arquivos"
CAMINHO_BD = os.path.join(PASTA, "livros.db")

def inicializar_diretorio():
    if not os.path.exists(PASTA):
        os.makedirs(PASTA)

def conectar():
    #conecta com o bd
    inicializar_diretorio()
    conexao = sqlite3.connect(CAMINHO_BD)
    return conexao

def inicializar_bd():
    conexao = conectar()
    cursor = conexao.cursor() #permite realmente a edição e manutenção das querys, simula controle remoto
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros(
            isbn TEXT PRIMARY KEY AUTOINCREMENT, 
            titulo TEXT NOT NULL, 
            autor TEXT NOT NULL,
            genero TEXT NOT NULL,
            ano_publicacao INTEGER NOT NULL,
            editora TEXT NOT NULL,
            paginas INTEGER NOT NULL,
            status TEXT NOT NULL,
            localizacao TEXT NOT NULL
        )
    """) #execute -> executa a query 
    conexao.commit() #salva o que foi feito no arquivo/bd | é necessário salvar antes de fechar a conexão
    conexao.closer() 
    
def executar_query(query, parametros=()):
    # recebe uma query(select/insert/update) "de fora" e executa
    conexao = conectar()
    cursor = conexao.cursor() # conexao gera/tem o cursor 
    cursor.execute(query, parametros) 
    #espera a query(sintaxe sql do possível CRUD) e parametros de forma que protege injections SQL
    # query = "INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)"
    # parametros = ("Dom Casmurro", "Machado de Assis", 1899)
    conexao.commit()
    resultado = cursor.fetchall() #fetchall -> Pega todas as linhas retornadas por um SELECT e devolve como uma lista de tuplas, uma tupla por linha.
    conexao.close()
    return resultado