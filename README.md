#  PeoplePad

> [🇧🇷 Português](#-português) · [🇺🇸 English](#-english)

---

## 🇧🇷 Português

### Visão Geral

O **PeoplePad** é um sistema de gerenciamento de contatos desenvolvido com **Django**, que evoluiu de um projeto de estudos para uma aplicação. Com foco em segurança, organização de dados e experiência do usuário. O projeto vai muito além de um CRUD básico, incorporando funcionalidades de análise de dados.

---

### 🚀 Funcionalidades Principais

- **Autenticação Completa e Personalizada** — Sistema de login, logout e registro com validações customizadas (verificação de e-mails duplicados, requisitos de senha).
- **Gestão de Perfil** — Área dedicada para o usuário atualizar seus próprios dados cadastrais.
- **Multitenancy (Isolamento de Dados)** — Cada usuário autenticado possui sua própria base de contatos. Um usuário nunca acessa os dados de outro, garantindo privacidade e integridade.
- **Dashboard de Métricas** — Painel com estatísticas em tempo real: total de contatos, contatos com foto e distribuição por categorias, utilizando agregações do Django ORM.
- **Busca e Filtragem Avançada:**
  - Busca global (nome, telefone, e-mail)
  - Filtro por categorias dinâmicas
  - Navegação alfabética (filtro pela letra inicial do sobrenome)
- **Interoperabilidade de Dados:**
  - **Exportação:** Gera arquivos CSV dos contatos em tempo real (com data no padrão brasileiro `dd/mm/aaaa`)
  - **Importação:** Upload de arquivos CSV para carga em massa de contatos
- **Interface Amigável** — Paginação, mensagens de feedback (Django Messages) e suporte a upload de imagens.

---

### 💻 Tecnologias Utilizadas

- **Backend:** Python 3 + Django Framework
- **Banco de Dados:** SQLite (padrão, pronto para migração ao PostgreSQL)
- **Frontend:** Django Templates com filtros customizados
- **Segurança:** Django Authentication System + decorators de controle de acesso

---
---

## 🇺🇸 English

### Overview

**PeoplePad** is a Django-based contact management system that grew from a learning project into a fully featured, multi-user application (**SaaS-ready**), focused on security, data organization, and user experience. The project goes far beyond a basic CRUD, incorporating data analytics and interoperability features.

---

### 🚀 Key Features

- **Full Custom Authentication** — Login, logout, and registration system with custom validations (duplicate email checking, password requirements).
- **Profile Management** — Dedicated area for users to update their own account information.
- **Multitenancy (Data Isolation)** — Each authenticated user has their own contact database. No user can ever access another user's data, ensuring privacy and data integrity.
- **Metrics Dashboard** — Real-time statistics panel: total contacts, contacts with photos, and category distribution, using Django ORM aggregations.
- **Advanced Search & Filtering:**
  - Global search (name, phone, email)
  - Dynamic category filtering
  - Alphabetical navigation (filter by last name initial)
- **Data Interoperability:**
  - **Export:** Generates CSV files from contacts in real time
  - **Import:** Upload CSV files for bulk contact creation
- **User-Friendly Interface** — Pagination, feedback messages (Django Messages), and image upload support.

---

### 💻 Tech Stack

- **Backend:** Python 3 + Django Framework
- **Database:** SQLite (default, ready for PostgreSQL migration)
- **Frontend:** Django Templates with custom template filters
- **Security:** Django Authentication System + access control decorators

---
---

## ⚙️ Como Rodar o Projeto / Getting Started

```bash
# 1. Clone o repositório / Clone the repository

# 2. Crie e ative um ambiente virtual / Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# 3. Instale as dependências / Install dependencies
pip install -r requirements.txt

# 4. Configure o settings.py
# Vá em project/settings.py e ajuste as seguintes variáveis:
# Go to project/settings.py and set the following variables:
#
# SECRET_KEY = 'sua-chave-secreta-aqui'
# DEBUG = True
# ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# 5. Aplique as migrações / Apply migrations
python manage.py migrate

# 6. Crie um superusuário (opcional) / Create a superuser (optional)
python manage.py createsuperuser

# 7. Inicie o servidor / Start the server
python manage.py runserver
