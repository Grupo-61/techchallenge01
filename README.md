# Tech Challenge - Fase 1 - API Vitivinicultura Embrapa 1970-2024

# ![logo61](docs/imagens/logo61.png) 
  # Sobre o Projeto

**Tech Challenge** é um projeto que reúne os conhecimentos adquiridos em todas as disciplinas da fase. Nesta etapa, o desafio proposto foi o seguinte:

> 📢 **Problema:** Você foi contratado(a) para uma consultoria e seu trabalho envolve analisar os dados de vitivinicultura da Embrapa, os quais estão disponíveis no site [Embrapa Viticultura](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01).

A proposta do projeto é criar uma **API pública** para consulta nos dados disponíveis no site da Embrapa nas respectivas abas:

- Produção
- Processamento
- Comercialização
- Importação
- Exportação

**Link do site:** [Embrapa Vitivinicultura](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01)

A API desenvolvida será utilizada para alimentar uma base de dados que servirá para um modelo de **Machine Learning**.

## 📌 Objetivos

- Criar uma Rest API em Python** que faça a consulta nos dados disponíveis no site da Embrapa.
- Documentar a API para facilitar o uso e compreensão.
- Recomendações (não obrigatórias):** Adotar um método de autenticação, como **JWT**.
- Elaborar um plano para o deploy da API, incluindo:
  - **Arquitetura do projeto:** Desde a ingestão até a alimentação do modelo de Machine Learning (não é necessário criar o modelo de ML nesta fase).
  - Escolher um cenário relevante onde a API será utilizada.
- Criar um **MVP (Minimum Viable Product):**
  - Realizar o deploy com um link acessível e compartilhável.
  - Disponibilizar o código em um repositório no **GitHub**.


## 📂 Estrutura do projeto

```
.
└── TECHCHALENGE01/
    ├── api/
    └── dados/
       └── dados_offline/
          └── comercializacao/
          └── exportacao/
          └── importacao/
          └── processamento/
          └── producao/
        ├── src/
        └── autenticacao/
            |- __init__.py
            |- decoradores.py
            |- manipulador_jwt.py
            |- rotas_autenticacao.py
        └── flask_api/
            |- __init__.py
            |- rotas_api.py
        └── scraper/
            |- __init__.py
            |- obtem_dados_offline.py
            |- urls.py
            |- webscraping.py
        └── scraper/
            |- test_api.py
            |- test_scraper.py
    |- __init__.py
    |- app.py
    |- index.py
    |- requirements.txt

    ├── collection_insomnia/
    |   - Insomnia_2025-04-03.yaml
    └── docs/
        └── arquitetura/
            |-Projeto61.pdf
            |-Projeto61.drawio 
        └── imagens/
            |- logo61.png 

    |- gitignore
    |- estrutura.txt
    |- note.txt
    |- pytest.ini
    |- README.md
    |- vercel.json    
```


## 🔩 Arquitetura da solução

## 🛠️ Instalação do projeto local

Clonando o projeto localmente

``` bash
$ git clone https://github.com/Grupo-61/techchallenge01.git
```

Criando um ambiente virtual

``` bash
$ python -m venv venv
```

Ativando o ambiente virtual

``` bash
$ source venv/Scripts/activate 
```

Instalação das depêndências

``` bash
$ pip install -r api/requirements.txt
```

Executando o servidor Flask a partir do diretório raiz do projeto:

``` bash
$ cd api
$ flask run 
```

Ou executar com o debug ativado:

``` bash
$ cd api
$ flask run --debug
```

Testando as consultas localmente via navegador

Link: `http://127.0.0.1:5000/comercializacao/ano=2016`


### 📋 Como testar localmente com o Vercel:
- Instalar Node.js `https://nodejs.org/pt`

1. Instale o Vercel CLI:
```bash
$ npm install -g vercel
```

2. Login no Vercel
```bash
$ vercel login
```

2. Execute o projeto localmente:
```bash
$ vercel dev
```

3. Acesse via navegador:

`http://localhost:3000/`

### Depêndencias

- Flask
- Flasgger
- Flask-JWT-Extended
- Beautifulsoup4
- Pytest

## ⚙️ Configuração e implantação 
 ### Vercel
     - O arquivo vercel.json configura o Vercel para rodar o arquivo app.py como ponto de entrada da aplicação, expondo as rotas Flask para acesso externo via URL gerada pelo Vercel. Assim, ao fazer deploy, a API fica acessível publicamente pelo endereço fornecido pela Vercel

 ### Testes Unitário
    - Com as bibliotecas `pytest` e `unittest` instaladas
    - Executar o seguinte comando no terminal na raiz do projeto
    - Incluir cenários de testes

```bash
$ cd api
$ python -m pytest
```

## Autenticação


## 📜 Swagger



## 🌐 Insominia

Dentro do diretório `collection_insomnia` está disponível o arquivo `Insomnia_2025-05-20.yaml` que é uma `collection do insomnia` contendo as configurações das chamadas à API local e pública, respectivamente na configuração de ambientes `Local Flask` e `Produção Vercel`. 

Para utilizar a collection é necessário importar o arquivo para o Insomnia. Após configurado é possível acessar os seguintes `endpoints`:

- Login: `/auth/login`
- Produção: `/producao/ano=<ano>`
- Processamento: `/processamento/ano=<ano>`
- Comercialização: `/comercializacao/ano=<ano>`
- Importação: `/importacao/ano=<ano>`
- Exportação: `/exportacao/ano=<ano>`
- Swagger Docs: `/apidocs`


## ✒️ Autores

- [Agusto Omena](https://github.com/AugustoOmena)
- [Ana Paula de Almeida](https://github.com/Ana9873P)
- [Bruno Gabriel](https://github.com/brunogabrieldeoliveira)
- [Pedro Ulisses](https://github.com/ordepzero)
- [Walmir Duque](https://github.com/WALMIRDUQUE)
      

## 📄 Licença
Este projeto está licenciado sob a Licença MIT.  
Consulte o arquivo [license](docs/license/license.txt)  para mais detalhes.