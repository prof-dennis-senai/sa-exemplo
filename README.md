# SA Exemplo

Essa Atividade será utilziada para os estudantes que estão refazendo a UC de Teste de Sistema e não possui um projeto para testar ou não possui grupo. 

## Pré-requisitos

Certifique-se de que as seguintes ferramentas estão instaladas em sua máquina:

- Python 3.8+ ([Download Python](https://www.python.org/))
- Virtualenv (opcional, mas recomendado)
- Git ([Download Git](https://git-scm.com/))

## Configuração e Execução

### 1. Clone o repositório
```bash
git clone https://github.com/prof-dennis-senai/sa-exemplo.git
cd sa-exemplo
```

### 2. Crie e ative um ambiente virtual (Opcional)
No Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

No Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências do projeto
```bash
pip install django
```

### 4. Configure o banco de dados
Execute as migrações para configurar o banco de dados:
```bash
python manage.py migrate
```

### 5. Execute o servidor de desenvolvimento
```bash
python manage.py runserver
```

Acesse o aplicativo no navegador em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Estrutura do Projeto

```plaintext
sa-exemplo/
│
├── api/                    # Diretório de exemplo de api com Django
├── projeto_aula/           # Diretório do aplicativo principal
├── site_app/               # Diretório com a interface web
├── db.sqlite3              # Banco de dados SQLite
├── manage.py               # Arquivo principal para execução do Django
└── README.md               # Documentação do projeto
```
