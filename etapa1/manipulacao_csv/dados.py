#módulo de tratamento dos dados de entrada 

def dadosbasics(): #função que trata vars comuns nas duas hipóteses de investimento 
    try:
        while True:
            valor_inicial = float(input("Digite o valor inicial: "))
            aporte_mensal = float(input("Digite o aporte mensal: "))
            taxa_juros = float(input("Digite a taxa de juros: "))
            return valor_inicial, aporte_mensal, taxa_juros
    
    except Exception: # caso em que não tem var que recebe o erro, fica liberado exibir qualquer coisa, não necessariamente o erro como o python mostra           
             
        print("Algum dado foi colocado de forma inválida!")

def dadosoption1(): #função que trata var exclusiva do investimento 1
    try:
        while True:
            num_meses = int(input("Digite o número de meses: "))
            return num_meses
    
    except Exception as e: # 'Exception' classe que captura qualquer exceção se a entrada for inválida, 'e' é a var que recebe o valor do objeto exceção
        
        print(f"Entrada inválida: {e}") #erro é exibido 
        
def dadosoption2(): #função que trata var exclusiva do investimento 2
    try:
        while True:
            valor_desejo = float(input("Digite o valor final desejado: "))
            return valor_desejo
    except Exception as e:
        print(f"Entrada inválida: {e}")