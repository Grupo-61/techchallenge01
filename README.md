# Tech Challenge 1 (Fase 1): API Viticultura Embrapa 1970-2024

# ![logo61](docs/imagens/logo61.png) 
  # Sobre o Projeto

**Tech Challenge** é um projeto que reúne a aplicação dos conhecimentos adquiridos em todas as disciplinas de uma fase da Especialização em Machine Learning Engineering da FIAP PosTech.

Para o Tech Challenge 1, o desafio proposto foi o seguinte:

> 📢 **Problema:** Você foi contratado(a) para uma consultoria e seu trabalho envolve analisar os dados de vitivinicultura da **Embrapa Uva e Vinho** que é um centro de pesquisa da Embrapa (Empresa Brasileira de Pesquisa Agropecuária). Este centro mantém um site que disponibiliza dados sobre a Viticultura no Brasil, como produção de uvas, vinhos e sucos, além de estatísticas do setor desde 1970.

**Link do site:** [Embrapa Vitivinicultura](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01)

**Proposta do desafio:**
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

## Possíveis dores

- Falta de padronização para acesso aos dados bem como tipos de retornos e formatos mais adequados para consumo na produção de relatórios e analytics.
- Suporte e documentação insuficientes.
- Indisponibilidade de dados por instabilidade do site da Embrapa.
- Ausência de método de autenticação para acesso ados dados.

## Proposta de solução

Em face ao desafio proposto, algumas funcionalidades propostas para a API são:

- Coleta automática e atualizada de dados do site Vitibrasil da Embrapa Uva e Vinho.
- Armazenamento dos dados extraídos do site Vitibrasil para garantia de disponibilidade (fallback).
- Fornecimento de endpoints para consulta de dados de diversas fontes tais como Produção, Processamento, Comercialização, Importação e Exportação, podendo filtrar por ano.
- Cenários futuros: são propostos modelos de Machine Learning (ML) para implementação futura, para as diversas fontes de dados.

## 📂 Estrutura do projeto

```
.
└── TECHCHALLENGE01/
    ├── api/
    └── apidocs/
    └── dados/
       └── dados_offline/
            └── comercializacao/
            └── exportacao/
            └── importacao/
            └── processamento/
            └── producao/
        ├── src/
            └── autenticacao/
            └── flask_api/
            └── scraper/
            └── testes/
            └── utils/
        |- app.py
        |- requirements.txt
    ├── collection_insomnia/
    └── docs/
        └── arquitetura/
        └── imagens/
    |- README.md
    |- vercel.json    
```


## 🔩 Arquitetura da solução

A arquitetura da solução foi desenhada sob uma abordagem End-to-end e consta na pasta de documentação deste repositório. [Link para o Diagrama](https://github.com/Grupo-61/techchallenge01/blob/main/docs/arquitetura/Projeto61.pdf)


## Dependências

Para o desenvolvimento deste desafio, foram utilizadas as seguintes bibliotecas e frameworks:

- Backend:Flask
- Documentação da API: Flassger - Swagger para Flask
- Autenticação: Flask-JWT-Extended
- Modularização: além de separação em componentes, também foi usado Blueprint
- Registro de Log: Logger
- Webscraping: BeatifulSoap
- Testes unitários: Pytest e Unittest


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

Testando as consultas localmente via Insomnia a seguir.


## 🌐 Insomnia

Dentro do diretório `collection_insomnia` está disponível o arquivo `Insomnia_2025-05-20.yaml` que é uma `collection do insomnia` contendo as configurações das chamadas à API local e pública, respectivamente, na configuração de ambientes `Local Flask` e `Produção Vercel`. 

Para utilizar a collection é necessário importar o arquivo para o Insomnia. Após configurado é possível acessar os seguintes `endpoints`:

- Login: `/auth/login`
- Produção: `/producao/ano=<ano>`
- Processamento: `/processamento/ano=<ano>`
- Comercialização: `/comercializacao/ano=<ano>`
- Importação: `/importacao/ano=<ano>`
- Exportação: `/exportacao/ano=<ano>`
- Swagger Docs: `/apidocs`

Para acessar as rotas é preciso primeiramente que o usuário esteja autenticado - para isso, deve ser acessada a rota `Login` que, ao retornar o token, ele possa ser incluído na configuração do `Auth` das demais rotas da API. Uma vez o usuário autenticado, as demais rotas podem ser utlizadas para realizar consultas aos dados.


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

Link: `http://localhost:3000/apidocs`

- Na collection do `Insomnia` também tem a configuração para os endpoints apontando para o `Vercel`.


### ⚙️ Configuração e implantação do Vercel
- O arquivo vercel.json configura o Vercel para rodar o arquivo app.py como ponto de entrada da aplicação, expondo as rotas Flask para acesso externo via URL gerada pelo Vercel. Assim, ao fazer deploy, a API fica acessível publicamente pelo endereço fornecido pela Vercel.

É necessário executar o seguinte comando a partir da raiz do projeto para realizar a implantação no Vercel:

```bash
$ vercel --prod
```

## Testes Unitários
- Com as bibliotecas `pytest` e `unittest` instaladas
- Executar o seguinte comando no terminal na raiz do projeto
- 

```bash
$ cd api
$ python -m pytest
```


## 📜 Swagger
Utilizado para documentar automaticamente todas as rotas da API Flask, facilitando o uso e integração com outras aplicações. Essa documentação torna mais compreensível os parâmetros de chamada e retornos.
[Link para a Documentação](https://techchallenge01-ulissesphs-projects.vercel.app/apidocs/)


## ✒️ Autores

| Nome                            |   RM    | Link do GitHub                                      |
|---------------------------------|---------|-----------------------------------------------------|
| Ana Paula de Almeida            | 363602  | [GitHub](https://github.com/Ana9873P)               |
| Augusto do Nascimento Omena     | 363185  | [GitHub](https://github.com/AugustoOmena)           |
| Bruno Gabriel de Oliveira       | 361248  | [GitHub](https://github.com/brunogabrieldeoliveira) |
| José Walmir Gonçalves Duque     | 363196  | [GitHub](https://github.com/WALMIRDUQUE)            |
| Pedro Henrique da Costa Ulisses | 360864  | [GitHub](https://github.com/ordepzero)              |

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.  
Consulte o arquivo [license](docs/license/license.txt)  para mais detalhes.