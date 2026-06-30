from dados import *

biblioteca = carregar_do_arquivo()

def exibircadastrados():
    print("-----Sistema de Jogos-----")
    if not biblioteca:
        print("\nAcervo vazio.")
        return # como se fosse um break para a função, ou seja, se a biblioteca estiver vazia, ele exibe a mensagem e sai da função, sem executar o restante do código, assim não preciso colocar o restante do código dentro de um else, deixando a função mais limpa e fácil de ler.
    
    #Função já tem o print(), dessa forma não é necessário ter um return para exibir a biblioteca, basta chamar a função e ela já exibe os jogos cadastrados.
    print(f"\n{'Nome':<20} | {'Tipo':<20}")
    print("-" * 43)
    for linha in biblioteca:
        print(f"{linha['nome']:<20} | {linha['tipo']:<20}")
        

def cadastrar():
    print("\n--- CADASTRO CSV ---")
    nome = input("Nome: ").strip()
    
    if any(l['nome'] == nome for l in biblioteca):
        print(f"❌ Erro: O jogo '{nome}' já existe!")
        return
        # A mesma coisa que:
        # biblioteca = [
        #     {'nome': 'banco imobiliário', ...},
        #     {'nome': 'clash royale', ...}
        # ]

        # nome digitado = "clash royale"

        # any() verifica cada dicionario:
        #   'banco imobiliário' == 'clash royale' → False
        #   'clash royale'      == 'clash royale' → True  ← para aqui

        # resultado: True → entra no if → exibe erro*
    
    tipo = input("Tipo: ").strip() # .strip() remove espaços no início e no final da string.
    
    try: #tenta converter inputs para inteiro
        ano_lancamento = int(input("Ano de lançamento: ").strip())
        classificacao = int(input("Classificação: ").strip())
    except ValueError: # se não for possível exibe a mensagem
        print("❌ Erro: Ano de lançamento e classificação devem ser números!")
        return
    
    #cadastra jogo, colocando as vars nos valores das chaves do dicionario(colunas do csv)
    jogo = {
        'nome': nome,
        'tipo': tipo,
        'ano_lancamento': ano_lancamento,
        'classificacao': classificacao
    }
    
    #adiciona dicionario jogo na lista de jogos(biblioteca) e salva atualizando o arquivo csv, passando a biblioteca atualizada como argumento da função salvar_no_arquivo()
    biblioteca.append(jogo)
    salvar_no_arquivo(biblioteca)
    print("✅ Jogo cadastrado com sucesso!")



def excluir():
    print("\n" + "="*15 + " ALTERAR JOGO " + "="*15)
    nome_busca = input("Digite o nome do jogo que deseja editar: ").strip()
    jogo_encontrado = None
    
    #para cada jogo (dicionário/linha csv) na biblioteca (lista de dicionários/arquivo csv) verifica se valor é igual ao nome_busca.
    for jogo in biblioteca:
        if jogo['nome'].lower() == nome_busca.lower():
            jogo_encontrado = jogo
            break
        
    if not jogo_encontrado:
        print(f"❌ Jogo {nome_busca} não encontrado!")
        return
    
    # .remove() -> método que remove item  da lista que está dentro do ()
    biblioteca.remove(jogo_encontrado)
    #salva biblioteca atualizada, passando a biblioteca atualizada como argumento da função salvar_no_arquivo()
    salvar_no_arquivo(biblioteca)
    print("\n✅ Jogo excluído com sucesso!")
    return
    
    
def alterar():
    print("\n" + "="*15 + " ALTERAR JOGO " + "="*15)
    nome_busca = input("Digite o nome do jogo que deseja editar: ").strip()
    jogo_encontrado = None

    for jogo in biblioteca:
        if jogo['nome'].lower() == nome_busca.lower():
            jogo_encontrado = jogo
            break
        
    if not jogo_encontrado:
        print(f"❌ Jogo {nome_busca} não encontrado!")
        return
        
    print(f"\nEditando {jogo_encontrado['nome']}")
    print("1. Título | 2. Tipo | 3. Ano de Lançamento | 4. Classificação | 0. Sair")
    
    opcao = input("Escolha o campo que deseja alterar: ").strip()
    
    #alterando valores dos campos
    if opcao == '1':
        novo_nome = input("Novo título: ").strip()
        jogo_encontrado['nome'] = novo_nome
    elif opcao == '2':   
        novo_tipo = input("Novo tipo: ").strip()
        jogo_encontrado['tipo'] = novo_tipo
    elif opcao == '3':
        try: #tenta converter -> deixando dados limpos e tratados para adicionar no csv 
            novo_ano = int(input("Novo ano de lançamento: ").strip())
            jogo_encontrado['ano_lancamento'] = novo_ano
        except ValueError:
            print("❌ Erro: Ano de lançamento deve ser um número!")
            return
    elif opcao == '4':
        try:
            nova_classificacao = int(input("Nova classificação: ").strip())
            jogo_encontrado['classificacao'] = nova_classificacao
        except ValueError:
            print("❌ Erro: Classificação deve ser um número!")
            return
    elif opcao == '0':
        print("Saindo da edição.")
        return 
    else:
        print("Opção inválida!")
        return     
    
    salvar_no_arquivo(biblioteca)
    print("\n✅ Arquivo Json atualizado com sucesso!")


#mostra mais informações além de nome e tipo do jogo
def ver_detalhes():
    print("\n" + "="*15 + " DETALHES DO JOGO " + "="*15)
    nome_busca = input("Digite o nome do jogo para ver detalhes: ").strip()
    jogo_encontrado = None
    for jogo in biblioteca:
        if jogo['nome'].lower() == nome_busca.lower():
            jogo_encontrado = jogo
            break
        
    if not jogo_encontrado:
        print(f"❌ Jogo {nome_busca} não encontrado!")
        return
    
    print(f"\nTítulo: {jogo_encontrado['nome']}")
    print(f"Tipo: {jogo_encontrado['tipo']}")   
    print(f"Ano de Lançamento: {jogo_encontrado['ano_lancamento']}")
    print(f"Classificação: {jogo_encontrado['classificacao']}")