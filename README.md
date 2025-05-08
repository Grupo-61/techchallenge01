# Tech Challenge - Fase 1 - API Vitivinicultura Embrapa 1970-2024

## Sobre o Projeto

O **Tech Challenge** é um projeto que reúne os conhecimentos adquiridos em todas as disciplinas da fase. Nesta etapa, o desafio proposto foi o seguinte:

> **Problema:** Você foi contratado(a) para uma consultoria e seu trabalho envolve analisar os dados de vitivinicultura da Embrapa, os quais estão disponíveis no site [Embrapa Viticultura](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01).

A ideia do projeto é criar uma **API pública** para consulta nos dados disponíveis no site da Embrapa nas respectivas abas:

- Produção
- Processamento
- Comercialização
- Importação
- Exportação

**Link do site:** [Embrapa Vitivinicultura](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01)

A API desenvolvida será utilizada para alimentar uma base de dados que, futuramente, servirá para um modelo de **Machine Learning**.

## Objetivos

- **Criar uma Rest API em Python** que faça a consulta nos dados disponíveis no site da Embrapa.
- Documentar a API para facilitar o uso e compreensão.
- **Recomendações (não obrigatórias):** Adotar um método de autenticação, como **JWT**.
- Elaborar um plano para o deploy da API, incluindo:
  - **Arquitetura do projeto:** Desde a ingestão até a alimentação do modelo de Machine Learning (não é necessário criar o modelo de ML nesta fase).
  - Escolher um cenário relevante onde a API será utilizada.
- Criar um **MVP (Minimum Viable Product):**
  - Realizar o deploy com um link acessível e compartilhável.
  - Disponibilizar o código em um repositório no **GitHub**.


## Estrutura do projeto

```
.
└── TECHCHALENGE01/
    ├── collection_insomnia/
    |   - collection_insomnia\Insomnia_2025-04-03.yaml
    └── data
    └── docs
        └── imagens
    └── src
        └── autenticacao
        └── flask_api
        └── scraper
        └── testes
    |- app.py
    |- README.md
    |- requirements.txt
```

## Arquitetura da solução

## Instalação do projeto local

Clonando o projeto localmente

``` bash
$ git clone https://github.com/Grupo-61/techchalenge01.git
```

Criando um ambiente virtual

``` bash
$ python -m venv env
```

Ativando o ambiente virtual

``` bash
$ source env/Scripts/activate 
```

Instalação das depêndências

``` bash
$ pip install -r requirementes.txt
```

Executando o servidor Flask a partir do diretório raiz do projeto

``` bash
$ flask run
```

Ou executar com o debug ativado

``` bash
$ flask run --debug
```

Testando as consultas localmente via navegador

Link: http://127.0.0.1:5000/comercializacao/ano=2016


### 🌐 Como testar localmente com o Vercel:
- Instalar Node.js `https://nodejs.org/pt`

1. Instale o Vercel CLI:
   ```bash
   npm install -g vercel

2. Login no Vercel
```base


2. Execute o projeto localmente:
   ```bash
    vercel dev

3. Acesse:
   ```bash
    http://localhost:3000/api

# Depêndencias

- Flask
- Flasgger
- Flask-JWT-Extended


## Configuração e implantação no Vercel

Detalhar os passos para implantar no Vercel


## Configurando e executando Testes Unitário

- Com as bibliotecas `pytest` e `unittest` instaladas
- Executar o seguinte comando no terminal na raiz do projeto
- Incluir cenários de testes

```bash
python -m pytest
```

# Autenticação

Autenticação básica com `httpauth`


Instalação:

``` bash
$ pip install flask-httpauth
```

## Swagger


## Insominia

- configuração da autorização


## Autores


## Licença

