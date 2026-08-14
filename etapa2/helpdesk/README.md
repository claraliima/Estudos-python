# Helpdesk API

API REST para registro de chamados de suporte, desenvolvida em **Python + Flask + SQLAlchemy**,
seguindo arquitetura em camadas (Controller → Service → Repository → Model).

## Arquitetura

```
helpdesk/
├── app.py                     # ponto de entrada, cria o app Flask e registra as rotas
├── database.py                # instância única do SQLAlchemy
├── controllers/                # recebem a requisição HTTP e devolvem a resposta
│   ├── usuario_controller.py
│   └── chamado_controller.py
├── services/                   # regras de negócio e validações
│   ├── usuario_service.py
│   └── chamado_service.py
├── repositories/               # acesso ao banco via SQLAlchemy (sem regra de negócio)
│   ├── usuario_repository.py
│   └── chamado_repository.py
├── models/                     # entidades do banco de dados
│   ├── usuario.py
│   └── chamado.py
└── routes/                     # blueprints do Flask, mapeando URL -> controller
    ├── usuario.py
    └── chamado.py
```

## Como executar

1. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Linux/Mac
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute a aplicação:
   ```bash
   python app.py
   ```

4. A API estará disponível em `http://127.0.0.1:5000`.
   O banco SQLite (`banco.db`) é criado automaticamente na primeira execução, dentro da
   pasta `instance/`.

## Endpoints

### Usuários
| Método | Rota                          | Descrição                              |
|--------|-------------------------------|-----------------------------------------|
| GET    | `/usuarios`                   | Lista todos os usuários                 |
| GET    | `/usuarios/<id>`               | Busca um usuário pelo id                |
| POST   | `/usuarios`                   | Cria um usuário                         |
| PUT    | `/usuarios/<id>`               | Atualiza um usuário                     |
| DELETE | `/usuarios/<id>`               | Remove um usuário (se não tiver chamados)|
| GET    | `/usuarios/<id>/chamados`      | Lista os chamados de um usuário         |

Corpo esperado (POST/PUT):
```json
{ "nome": "Ana", "email": "ana@empresa.com", "setor": "TI" }
```

### Chamados
| Método | Rota                             | Descrição                                  |
|--------|-----------------------------------|---------------------------------------------|
| GET    | `/chamados`                       | Lista todos os chamados                      |
| GET    | `/chamados/<id>`                   | Busca um chamado pelo id                     |
| POST   | `/chamados`                       | Cria um chamado                              |
| PUT    | `/chamados/<id>`                   | Atualiza um chamado                          |
| DELETE | `/chamados/<id>`                   | Remove um chamado                            |
| PATCH  | `/chamados/<id>/iniciar`           | Altera o status para "Em atendimento"        |
| PATCH  | `/chamados/<id>/encerrar`          | Altera o status para "Encerrado"             |
| GET    | `/chamados/abertos`                | Lista apenas chamados com status "Aberto"    |
| GET    | `/chamados/prioridade/alta`        | Lista chamados com prioridade "Alta"         |
| GET    | `/estatisticas`                    | Retorna estatísticas gerais do sistema        |

Corpo esperado (POST/PUT):
```json
{
  "titulo": "Impressora não funciona",
  "descricao": "A impressora do setor financeiro não liga.",
  "prioridade": "Alta",
  "usuario_id": 1,
  "tecnico": "Carlos"
}
```

Resposta de `/estatisticas`:
```json
{
  "usuarios": 15,
  "chamados": 48,
  "abertos": 10,
  "em_atendimento": 8,
  "encerrados": 30
}
```

## Regras de negócio implementadas

**Usuários**
- Nome e e-mail obrigatórios.
- E-mail deve ser único.
- Não é possível excluir um usuário que possua chamados cadastrados.

**Chamados**
- Título obrigatório, mínimo de 5 caracteres.
- Descrição obrigatória, mínimo de 10 caracteres.
- Deve estar vinculado a um usuário existente.
- Prioridade deve ser `Baixa`, `Média` ou `Alta`.
- Status inicial sempre `Aberto`.
- Um usuário não pode ter mais de 5 chamados de prioridade `Alta` ainda não encerrados.
- Transições de status permitidas apenas: `Aberto → Em atendimento → Encerrado`
  (não é possível pular etapas nem retroceder).

## Códigos de resposta

- `200` — operação realizada com sucesso.
- `201` — recurso criado com sucesso.
- `400` — erro de validação / regra de negócio violada.
- `404` — recurso não encontrado.
