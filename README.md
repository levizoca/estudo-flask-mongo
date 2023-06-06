# Avaliação Flask

Este repositório contém o arquivo usado para processamento dos dados presentes nas bases de dados da Receita Federal disponíveis neste link: <br><br>https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-jurdica---cnpj <br><br>

A base utilizada em questão foi a "Estabelecimentos9". Faça o download da mesma e extraia na pasta raiz do projeto com o nome *"K3241.K03200Y9.D30311.ESTABELE.csv"* <br><br> 

Para subir a aplicação, o MongoDB e o ElasticSearch digite o comando ```docker-compose up -d```. <br><br>

Para instalar as dependências necessárias e rodar o Jupyter Notebook digite os comandos ```pip install -r requirements.txt``` e ```jupyter notebook```. <br><br>
