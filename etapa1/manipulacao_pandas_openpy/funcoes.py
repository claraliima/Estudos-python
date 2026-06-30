#import module_pandas.dados as dados
import module_openpyxl.dados as dados # Escolhe qual biblioteca irá importar os dados

biblioteca = dados.carregar_do_arquivo()

def cadastrar():
    print("\n--- CADASTRO EXCEL ---")
    isbn = input("ISBN: ").strip()
    
    if any(l['isbn'] == isbn for l in biblioteca):
        print("❌ Erro: ISBN já existe!")
        return

    try:
        livro = {
            "isbn": isbn,
            "titulo": input("Título: ").strip(),
            "autor": input("Autor: ").strip(),
            "genero": input("Gênero: ").strip(),
            "ano_publicacao": int(input("Ano: ")),
            "editora": input("Editora: ").strip(),
            "paginas": int(input("Páginas: ")),
            "status": "disponivel",
            "localizacao": input("Localização: ").strip()
        }
        
        biblioteca.append(livro)
        dados.salvar_no_arquivo(biblioteca)
        print("✔ Salvo no arquivo CSV!")
    except ValueError:
        print("❌ Erro: Ano e Páginas devem ser números.")

def listar():
    if not biblioteca:
        print("\nAcervo vazio.")
        return
    
    print(f"\n{'ISBN':<15} | {'TÍTULO':<20} | {'STATUS':<10}")
    print("-" * 50)
    for l in biblioteca:
        print(f"{l['isbn']:<15} | {l['titulo'][:20]:<20} | {l['status']:<10}")

def pesquisar():
    termo = input("\nBusca (Título/ISBN): ").lower()
    resultados = [l for l in biblioteca if termo in l['titulo'].lower() or termo == l['isbn']]
    
    if resultados:
        for r in resultados:
            print(f"\n--- Detalhes: {r['titulo']} ---")
            for chave, valor in r.items():
                print(f"{chave.replace('_', ' ').title()}: {valor}")
    else:
        print("Nenhum resultado.")

def alterar_livro():
    print("\n" + "="*15 + " ALTERAR LIVRO " + "="*15)
    isbn_busca = input("Digite o ISBN do livro que deseja editar: ").strip()
    
    livro_encontrado = None
    for livro in biblioteca:
        if livro['isbn'] == isbn_busca:
            livro_encontrado = livro
            break
    
    if not livro_encontrado:
        print("❌ Livro não encontrado.")
        return

    print(f"\nEditando: {livro_encontrado['titulo']}")
    print("1. Título | 2. Autor | 3. Gênero | 4. Status | 5. Localização | 0. Sair")
    
    opcao = input("Escolha o que mudar: ")

    if opcao == "1":
        livro_encontrado['titulo'] = input("Novo Título: ").strip()
    elif opcao == "2":
        livro_encontrado['autor'] = input("Novo Autor: ").strip()
    elif opcao == "3":
        livro_encontrado['genero'] = input("Novo Gênero: ").strip()
    elif opcao == "4":
        print("Status atuais: disponivel / emprestado")
        livro_encontrado['status'] = input("Novo Status: ").strip().lower()
    elif opcao == "5":
        livro_encontrado['localizacao'] = input("Nova Localização: ").strip()
    elif opcao == "0":
        return
    else:
        print("Opção inválida.")
        return

    dados.salvar_no_arquivo(biblioteca)
    print("\n✅ Arquivo CSV atualizado com sucesso!")