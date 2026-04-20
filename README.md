# 🚀 Ignyx User API

API desenvolvida com **FastAPI** focada em arquitetura moderna, código limpo e boas práticas de backend.

> Projeto criado com objetivo de estudo, explorando conceitos reais usados em produção como async, migrations, validação com Pydantic e testes automatizados.

---

## 🧠 Stack

* ⚡ FastAPI
* 🐍 Python 3.x
* 🧩 Pydantic (schemas e validação)
* 🗄️ SQLAlchemy (ORM)
* 🔄 Alembic (migrations)
* 🧪 Pytest (testes)

---

## 🏗️ Arquitetura

Estrutura pensada para escalar:

```
app/
├── models/        # Entidades do banco (SQLAlchemy)
├── schemas/       # Schemas Pydantic (entrada/saída)
├── routers/       # Rotas da API
├── services/      # Regras de negócio
├── database/      # Configuração do DB
└── main.py        # Entrypoint
```

Separação clara de responsabilidades:

* **Model** → estrutura do banco
* **Schema** → contrato da API
* **Service** → lógica
* **Router** → camada HTTP

---

## ⚡ Conceito: Async no FastAPI

FastAPI é assíncrono por natureza.

```python
@app.get("/users")
async def get_users():
    return await service.list_users()
```

### 🧠 Por que isso importa?

Sem async:

* cada request bloqueia o servidor

Com async:

* o servidor pode atender múltiplas requisições simultaneamente

➡️ Isso é essencial para APIs escaláveis ([Medium][1])

---

## 🧩 Pydantic Schemas

Separação entre **modelo do banco** e **modelo da API**:

```python
class UserCreate(BaseModel):
    name: str
    email: str
```

```python
class UserResponse(BaseModel):
    id: int
    name: str
```

### 💡 Por quê?

* validação automática
* tipagem forte
* segurança contra dados inválidos

---

## 🔄 Migrations com Alembic

Controle de versão do banco (tipo Git do banco):

```bash
alembic revision -m "create users"
alembic upgrade head
```

### 🧠 Boas práticas

* migrations devem ser **reversíveis**
* nomes descritivos
* manter histórico limpo ([GitHub][2])

---

## 🧪 Testes com Pytest

### Exemplo:

```python
@pytest.mark.asyncio
async def test_health(client):
    response = await client.get("/health")
    assert response.status_code == 200
```

### 🔧 Fixtures

Fixtures criam dependências reutilizáveis:

```python
@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
```

### 🧠 Por que usar fixtures?

* isolamento de testes
* reaproveitamento
* setup automático

➡️ cada teste roda em ambiente limpo ([Stack Overflow][3])

---

## 🔌 Banco de Dados (Async)

Uso de SQLAlchemy assíncrono:

```python
async def get_db():
    async with async_session() as session:
        yield session
```

### 💡 Insight importante

* `yield` aqui funciona como **gerenciador de contexto**
* abre sessão → entrega → fecha automaticamente

---

## 🧠 Conceito: Annotated (FastAPI moderno)

```python
from typing import Annotated

db: Annotated[Session, Depends(get_db)]
```

### Por quê?

* melhora tipagem
* deixa dependências explícitas
* padrão moderno do FastAPI

---

## 🔥 Diferenciais do Projeto

* Arquitetura organizada e escalável
* Uso de async de ponta a ponta
* Separação clara de camadas
* Testes automatizados
* Migrations versionadas

---

## 📈 Possíveis Evoluções

* autenticação (JWT / OAuth)
* cache (Redis)
* background tasks (Celery / RQ)
* observabilidade (logs + metrics)

---

## 🧑‍💻 Autor

**Hideki Maesaka**

* Backend Developer focado em Python
* Interesse em arquitetura, performance e sistemas escaláveis

---

## ⭐ Objetivo do Projeto

Este projeto foi criado para consolidar conhecimentos em:

* APIs modernas com FastAPI
* Programação assíncrona
* Boas práticas de backend
* Testes automatizados

---

[1]: https://medium.com/%40puttt.spl/fastapi-pydantic-part-3-async-database-integration-with-sqlalchemy-alembic-ee1780081204?utm_source=chatgpt.com "FastAPI + Pydantic, Part 3: Async Database Integration with SQLAlchemy & Alembic | by Latha Narayanappa | Mar, 2026 | Medium"
[2]: https://github.com/zhanymkanov/fastapi-best-practices?utm_source=chatgpt.com "GitHub - zhanymkanov/fastapi-best-practices: FastAPI Best Practices and Conventions we used at our startup · GitHub"
[3]: https://stackoverflow.com/questions/69080122/how-to-configure-pytest-for-alembic-migrations?utm_source=chatgpt.com "python - How to configure pytest for alembic migrations - Stack Overflow"
