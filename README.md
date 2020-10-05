Teste Digesto
========

## Overview:
Web crawler em Python para extrair dados de CPU / VCPU, MEMORY, STORAGE / SSD DISK, BANDWIDTH / TRANSFER, PRICE [$/mo] das páginas-alvo e salvar em disco.

Páginas-alvo:
1. https://www.vultr.com/products/cloud-compute/#pricing (apenas SSD Cloud Instances)
2. https://www.digitalocean.com/pricing/ (apenas aba Standard)

NOTA: Na abstração de dados do site Vultr a última coluna retorna dados unidos de preço por mês e hora que não foram tratados.

Requirements
============

* Python 3.6
* BeautifulSoup 4

Install
=======

Se desejar, crie um ambiente virtual com Python 3.6 e execute o seguinte comando para instalar as dependências:

    pip install requirements.txt

How to
=======

O programa deve ser executado no terminal com:

    python scrape.py [OPTIONS]

A busca padrão ocorre em Vultr. Para alterar basta adicionar a opção --digital_ocean.

Opções
=======

  -h, --help : mostra mensagem de ajuda

  --print : escreve dados no terminal

  --save_csv : salva dados como arquivo csv

  --save_json : salva dados como arquivo json

  --digital_ocean : usa dados da Digital Ocean