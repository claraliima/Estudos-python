#Questao1 -> função básica de funcionalidade/operacional
def super_calculadora(operacao, *args):
    resultado=0
    if not args:
      resultado = 0
    if operacao == "soma":
        for n in args:
            resultado+=n
    if operacao == "mult":
        resultado = 1
        for n in args:
            resultado *= n
    if operacao == "sub":
        for n in args:
            if n == args[0]:
                resultado = args[0]
            else:
                resultado = resultado - n
    if operacao == "div":
      if args == 0:
        resultado= "Erro!"
      else:
        for n in args:
            if n == args[0]:
                resultado = args[0]
            else:
                resultado /= n
    return resultado

# funcao p/ receber parametros, mandar para funcao operacional e por fim retornar o valor da função operacional
def input_questao1():
    operacao = str(input("Digite a operação que deseja (soma, sub, mult ou div): "))
    nums = input("Digite os números que deseja e os separe por espaço: ").split()
    numeros_raw = [float(x) for x in nums]
    return super_calculadora(operacao, *numeros_raw)

#Questao2 -> função básica de funcionalidade/operacional
# sem funcao de input, pois sao entradas fixas
def classificar_dados(elemento):
    tipo_nome = type(elemento)
    retorno = 0
    soma = 0
    if tipo_nome == list:
        retorno = elemento[0], elemento[-1]
    elif tipo_nome == set:
        retorno = len(elemento)
    elif tipo_nome == tuple:
        for ele in elemento:
            i = 0
            i<len(elemento)
            i+=1
            soma += ele
        retorno = soma
    return retorno

#Questao3 -> função básica de funcionalidade/operacional
def filtrar_estoque(limite, **kwargs):
    aprovados = {}
    for chave, valor in kwargs.items():
        if valor >= limite:
            aprovados.update({chave: valor})
    return aprovados

# funcao p/ receber parametros, mandar para funcao operacional e por fim retornar o valor da função operacional
def input_questao3():
    limite = float(input("Digite um valor mínimo: " ))
    return filtrar_estoque(limite, mouse = 20, vidro = 120)

#Questao4 -> função básica de funcionalidade/operacional
SISTEMA_ATIVO = True
def validar_acesso(usuario, senha, nivel_priori = 1):
    if SISTEMA_ATIVO == True and (usuario == "admin" or nivel_priori>5):
      return True
    else:
      return False

# funcao p/ receber parametros, mandar para funcao operacional e por fim retornar o valor da função operacional
def input_questao4():
    user = input("Digite seu tipo de user: ")
    nivel_priori = float(input("Digite seu nível de prioridade: "))
    return validar_acesso(user, nivel_priori)

#Questao5 -> função básica de funcionalidade/operacional
# sem funcao de input, pois sao entradas fixas
def resumo_vendas(lista):
    maior_valor = 0
    nome_do_item_mais_caro = ""
    valor_total_geral = 0
    for dicionario in lista :
        valor_total_geral += dicionario["valor"] * dicionario["quant"]
        if dicionario["valor"] > maior_valor :
            maior_valor = dicionario["valor"]
            nome_do_item_mais_caro = dicionario["item"]
    return valor_total_geral, nome_do_item_mais_caro

