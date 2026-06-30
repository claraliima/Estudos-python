from funcoes import *

def exibir_menu():
    #enquanto for verdade 
    while True:
        print("\n--- SISTEMA JOGOS MODULAR ---")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Excluir")
        print("4. Alterar")
        print("5. Ver detalhes do jogo")
        print("0. Sair")
        
        opcao = input("\nEscolha: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            exibircadastrados()
        elif opcao == "3":
            excluir()
        elif opcao == "4":
            alterar()
        elif opcao == "5":
            ver_detalhes()
        elif opcao == "0":
            print("Encerrando...")
            #se digitar 0, sai do loop e encerra o programa
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    exibir_menu()
