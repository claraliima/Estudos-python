# importar tudo do módulo função (* = tudo)
from funcoes import * 

#escolher questao
questao = input("Opções: Questao1, Questao2, Questao3, Questao4 e Questao5! Digite qual questão quer ter acesso:")
if questao=="Questao1":
  resultado = input_questao1()
  print(resultado)  

elif questao=="Questao2":
  elemento = 1, 2, 1 # sem funcao de input, pois sao entradas fixas
  print(classificar_dados(elemento))

elif questao=="Questao3":
  resultado = input_questao3() 
  print(resultado)  

elif questao=="Questao4":
  resultado = input_questao4()
  print(resultado)  

elif questao=="Questao5": # sem funcao de input, pois sao entradas fixas
  lista = [
    { "item": "Teclado", "valor": 150 , "quant": 2},
    { "item": "Mouse","valor": 200 , "quant": 1}
  ]

  tupla = (resumo_vendas(lista))
  print(tupla)