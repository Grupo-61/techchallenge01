# Tech Challenge - Fase 1 - API Vitivinicultura Embrapa 1970-2024

# ![logo61](docs/imagens/logo61.png) 
  # Sobre o Projeto 61

**Tech Challenge** é um projeto que reúne os conhecimentos adquiridos em todas as disciplinas da fase. Nesta etapa, o desafio proposto foi o seguinte:

> 📢 **Problema:** Você foi contratado(a) para uma consultoria e seu trabalho envolve analisar os dados de vitivinicultura da Embrapa, os quais estão disponíveis no site [Embrapa Viticultura](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01).

A proposta do projeto é criar uma **API pública** para consulta nos dados disponíveis no site da Embrapa nas respectivas abas:

- Produção
- Processamento
- Comercialização
- Importação
- Exportação

**Link do site:** [Embrapa Vitivinicultura](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01)

API desenvolvida será utilizada para alimentar uma base de dados que, futuramente, servirá para um modelo de **Machine Learning**.

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
    └── data/
       └── data_offline/
          └── comercializacao/
              |- producao.csv
          └── exportacao/
              |- espumantes.csv
              |- suco_uva.csv
              |- uvas_frescas.csv
              |- vinhos_mesa.csv
          └── importacao/
              |- espumantes.csv
              |- suco_uva.csv
              |- uvas_frescas.csv
              |- vinhos_mesa.csv
          └── processamento/
              |- americanas_hibridas.csv
              |- sem_classificacao.csv
              |- uvas_mesa.csv
              |- viniferas.csv
          └── producao/
              |- producao.csv

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
            |- trata_dados.py
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
    |   - collection_insomnia/Insomnia_2025-04-03.yaml
    └── docs/
        └── arquitetura/
        └── imagens/

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


### 📋 Como testar localmente com o Vercel:

1. Instale o Vercel CLI:
   ```bash
   npm install -g vercel

2. Execute o projeto localmente:
   ```bash
    vercel dev

3. Acesse:
   ```bash
    http://localhost:3000/api


## ⚙️ Configuração e implantação 
 ### Vercel
     - Detalhar os passos para implantar no Vercel

 ### Testes Unitário
    - Com as bibliotecas `pytest` e `unittest` instaladas
    - Executar o seguinte comando no terminal na raiz do projeto
    - Incluir cenários de testes

```bash
python -m pytest
```

## 📜 Swagger


## 🌐 Insominia


## ✒️ Autores
      


## 📄 Licença
