from dados import *
from funcoes import * 
from info_arquivo import *

def menu():
    while True:
        print("\n=== SIMULADOR DE INVESTIMENTOS PRO ===")
        print("1. Simular por Tempo Fixo")
        print("2. Calcular Tempo para Meta")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            resultado = periodo_fixo()
            for mes, saldo, rendimento in resultado:
                print(f"Mês: {mes}, Saldo: {saldo:.2f}, Rendimento: {rendimento:.2f}")
        elif opcao == '2':
            # Chama a função para calcular o tempo para alcançar a meta
            resultado = meta_financeira()
            for mes, saldo, rendimento in resultado:
                print(f"Mês: {mes}, Saldo: {saldo:.2f}, Rendimento: {rendimento:.2f}")
        elif opcao == '0':
            nome_arquivo = input("Digite o nome do arquivo para salvar os resultados: ")
            print(salvar_arquivo(nome_arquivo))
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()