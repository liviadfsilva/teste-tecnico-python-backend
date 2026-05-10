# 🚀 Desafio Técnico: API de Foco e Produtividade

![Python](https://img.shields.io/badge/Python-3.12.13-yellow?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-3.1.3-white?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?style=for-the-badge)
![PostgreSQL](https://img.shields.io/badge/Postgres-16-7AADFF?style=for-the-badge)

## Sobre ✨

A Log de Foco API é uma API backend para registro de sessões de produtividade, permitindo armazenar métricas como nível de foco, duração e contexto da atividade. Com base nesses dados, a aplicação gera feedbacks simples para ajudar na análise de padrões de concentração ao longo do tempo.

<br>

## Instalação 💻

1. **Clone o repositório:**

   ```sh
   git clone https://github.com/liviadfsilva/BookReviewBlogAPI.git
   cd BookReviewBlogAPI
   ```

2. **Copie o .env.example file para .env e mude as variáveis de ambiente se necessário:**

   ```sh
   cp .env.example .env
   ```

3. **Build and start the application and database with Docker**

   ```bash
    docker compose up --build
   ```
<br/>

#### A aplicação estará disponível em:
꩜ **http://localhost:5001**

<br/>

## Arquitetura ⚒️

A aplicação segue uma arquitetura em camadas:

- Controllers → responsabilidade das rotas
- Models → camada de persistência (SQLAlchemy)
- Schemas → validação e serialização de dados
- Config → gerenciamento de ambiente

</br>

## Decisões Técnicas 🧠

- Utilização de Flask com arquitetura em camadas (controllers, models, schemas)
- Uso de SQLAlchemy como ORM para abstração do banco de dados
- Flask-Migrate para controle de versionamento do schema do banco
- Docker para garantir consistência entre ambientes

</br>

## Estrutura do Projeto 🧬

```
root/
├── ai/
│   ├── README.md/
├── app/
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── registro.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── db.py
│   │   ├── registro.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── registro_schema.py
│   │
│   │
│   ├── __init__.py
│
├── migrations/
│
├── .env.example
├── .gitignore
├── config.py
├── docker-compose.yml
├── Dockerfile
├── main.py
└── requirements.txt

```

</br>

## Autora 🌸
**Lívia Silva**<br/>
Backend Developer

- GitHub: https://github.com/liviadfsilva 
- LinkedIn: https://linkedin.com/in/liviadfsilva

</br>

## 📁 Pasta de transparência de IA

Para manter transparência conforme solicitado no desafio técnico, toda a utilização de IA foi documentada em uma pasta dedicada dentro do repositório.
A IA foi utilizada como ferramenta de apoio, e todo o código gerado foi revisado e adaptado manualmente.
