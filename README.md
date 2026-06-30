# Estudos Python

Repositório com os estudos de Python desenvolvidos durante o 3º ano do curso técnico. O conteúdo está organizado em três etapas ao longo do ano, cada uma reunindo as atividades práticas feitas em sala.

## Etapas

- **Etapa 1** — *(em construção)*
- **Etapa 2** — Atividades envolvendo POO, Flask, Jinja2 e Sqlite3
- **Etapa 3** — *(em construção)*

---

## Etapa 2

### Estrutura das pastas

#### `POO/`
Revisão de Programação Orientada a Objetos. Implementação de uma classe para instanciar três objetos de mesma espécie (animais), com no mínimo 5 atributos e 4 métodos diferentes, executando ações alternadas entre as instâncias.

#### `Flask01/`
Primeira aplicação Flask, com duas rotas básicas:
- Rota padrão (`/`), retornando "Hello World!"
- Rota `/nome`, retornando o nome completo do usuário

#### `Flask02/`
Conversão de um código de manipulação de dados em uma API Flask, com rotas para interação com uma biblioteca de livros (`arquivos/biblioteca.json`).

#### `Flask03/`
Consolidação das rotas da atividade anterior em uma única aplicação, reunindo todas as funcionalidades em um só arquivo, com templates HTML (`templates/base.html`, `templates/index.html`).

#### `Jinja2/`
Criação da página inicial da biblioteca, listando todos os livros cadastrados em formato de tabela, utilizando templates Jinja2 com estilização CSS (Bootstrap). Os títulos das colunas seguem o padrão: ISBN em maiúsculo, sem underline entre palavras e com acentuação correta.

#### `Formulário/`
Criação de um formulário para inserção de novos livros na aplicação da biblioteca e rota para alteração (edição) de um livro já cadastrado.

---

## Observações

- Cada pasta de atividade pode conter seu próprio ambiente virtual (venv) local, que não é versionado neste repositório (ver `.gitignore`).
- As dependências de cada projeto podem ser instaladas individualmente dentro de cada pasta, conforme as bibliotecas utilizadas (ex: Flask).
