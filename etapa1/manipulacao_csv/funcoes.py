#módulo que irá executar as funções de cáculo de investimento

from dados import * #recebe dados tratados 

investimento = [] #cria lista que receberá os meses e rendimentos do investimento independente do tipo

def periodo_fixo():
    valor_inicial, aporte_mensal, taxa_juros = dadosbasics() 
    num_meses = dadosoption1()
    saldo = valor_inicial 
    for mes in range(1, (num_meses+1)): #para cada mês em uma sequência que começa do 1(incluindo) até o num_meses + 1, pois range não inclui o último
        
        entrada = saldo + aporte_mensal #o valor que entra 
        saldo = entrada * (1 +taxa_juros) #o que sai
        rendimento = entrada* taxa_juros #o quanto rendeu / quanto os juros geraram
        investimento.append([mes, saldo, rendimento]) #adiona os resultados em uma lista que estará dentro de investimento[], cada mês será uma lista
        
    return investimento
        
     
def meta_financeira():
    valor_inicial, aporte_mensal, taxa_juros = dadosbasics() 
    valor_desejo = dadosoption2()    
    saldo = valor_inicial 
    num_meses = 0
    while saldo < valor_desejo:
        entrada = saldo + aporte_mensal
        saldo = entrada * (1 +taxa_juros)
        rendimento = entrada* taxa_juros 
        investimento.append([num_meses, saldo, rendimento])
        num_meses += 1
    print(f"Você atingirá seu objetivo em {num_meses} meses.")    
    return investimento