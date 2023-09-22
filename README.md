
# Projeto Super Portfólio

Neste projeto foi desenvolvido uma API para gerenciamento de dados de perfil e projetos em um super portfólio.

📝 Habilidades trabalhadas:

* Utilizar o Django REST Framework para criar endpoints com entidades aninhadas.
* Utilizar o módulo Simple JWT para implementar autenticação no Django REST Framework.


## Instalação

1. Clone o repositório.
```bash
git clone git@github.com:Thromoto/python-spotnews.git
```
2. Entre na pasta do repositório que você acabou de clonar.

3. Crie o ambiente virtual para o projeto.
```bash
python3 -m venv .venv && source .venv/bin/activate
```
4. Atualize seu pip antes de instalar as dependências.
```bash
python3 -m pip install --upgrade pip
```
5. Instale as dependências.
```bash
python3 -m pip install -r dev-requirements.txt
```
6. Para rodar o MySQL via Docker execute os seguintes comandos na raiz do projeto:
```bash
docker build -t super-portfolio-db .
docker run -d -p 3306:3306 --name=super-portfolio-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=super_portfolio_database super-portfolio-db
```


## Stack utilizada

Python, Django, Django Rest Framework, arquitetura Model-View-Template, MYSQL, Simple JWT.