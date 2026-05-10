# 1. Brazilian E-Commerce Project

- [1. Brazilian E-Commerce Project](#1-brazilian-e-commerce-project)
  - [1.1. Conjunto de Dados](#11-conjunto-de-dados)
    - [1.1.1. Esquema de dados](#111-esquema-de-dados)
  - [1.2. ConfiguraÃ§Ã£o do Ambiente Local](#12-configuraãão-do-ambiente-local)
    - [1.2.1. Configurando o Poetry](#121-configurando-o-poetry)
  - [1.3. Estrutura do Projeto](#13-estrutura-do-projeto)
    - [1.3.1. Principais notebooks](#131-principais-notebooks)
  - [1.4. Ferramentas de Qualidade e Automação](#14-ferramentas-de-qualidade-e-automação)
    - [1.4.1. Makefile (Automação de Tarefas)](#141-makefile-automação-de-tarefas)
    - [1.4.2. Pre-commit (Padronização e Linting)](#142-pre-commit-padronização-e-linting)
    - [1.4.3. Testes Unitários (`pytest`)](#143-testes-unitários-pytest)
    - [1.4.4. Documentação Automática (`pdoc`)](#144-documentação-automática-pdoc)

Este projeto tem o objetivo de realizar uma anÃ¡lise exploratÃ³ria com esse conjunto de dados pÃºblicos de E-commerce Brasileiro.
As anÃ¡lises e modelagens de dados serÃ£o realizadas utilizando Python e bibliotecas como `Pandas`, `Matplotlib` e `Scikit-Learn`.
Por fim, o objetivo principal Ã© preparar as features e construir um **`Modelo de Machine Learning`** preditivo para os dados.

Para desenvolvimento desse projeto foi realizado o download do conjunto de dados no formato CSV no Link: [Kaggle - Brazilian E-commerce Data](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/data).

Os dados originais podem ser manipulados localmente para desenvolvimento de habilidades com ferramentas de dados e modelagem.

## 1.1. Conjunto de Dados

Este Ã© um conjunto de dados pÃºblicos de comÃ©rcio eletrÃ´nico brasileiro de pedidos feitos na [Olist Store](https://www.olist.com/). O conjunto de dados conta com informaÃ§Ãµes de 100 mil pedidos de 2016 a 2018 feitos em vÃ¡rios marketplaces no Brasil. Seus recursos permitem visualizar um pedido em vÃ¡rias dimensÃµes: desde o status do pedido, preÃ§o, desempenho de pagamento e frete atÃ© a localizaÃ§Ã£o do cliente, atributos do produto e, finalmente, avaliaÃ§Ãµes escritas pelos clientes.

O Olist conecta pequenas empresas de todo o Brasil aos canais sem complicaÃ§Ãµes e com um Ãºnico contrato. Esses comerciantes podem vender seus produtos por meio da Olist Store e enviÃ¡-los diretamente aos clientes usando os parceiros logÃ­sticos do Olist.

Depois que um cliente compra o produto na Olist Store, um vendedor Ã© notificado para atender a esse pedido. Assim que o cliente recebe o produto, ou a data estimada de entrega Ã© devida, o cliente recebe uma pesquisa de satisfaÃ§Ã£o por e-mail onde pode dar uma nota para a experiÃªncia de compra e anotar alguns comentÃ¡rios.

**Ponto de atenÃ§Ã£o:** Um pedido pode ter vÃ¡rios itens.
Cada item pode ser atendido por um vendedor distinto.
Todos os textos que identificam lojas e parceiros foram substituÃ­dos pelos nomes das grandes casas de Game of Thrones.

### 1.1.1. Esquema de dados

Os dados sÃ£o divididos em vÃ¡rios conjuntos de dados para melhor compreensÃ£o e organizaÃ§Ã£o.
Esquema dos dados:
![Esquema de Dados](docs/archive/Esquema_dados.png)

## 1.2. ConfiguraÃ§Ã£o do Ambiente Local

Para trabalhar neste projeto, utilizaremos o **Poetry** para gerenciamento de dependÃªncias.

### 1.2.1. Configurando o Poetry

O arquivo **`pyproject.toml`** jÃ¡ estÃ¡ definido no repositÃ³rio. Para instalar as dependÃªncias e o pacote local `src`, siga os passos:

1. **Instalar dependÃªncias com Poetry:**

   ```bash
   poetry install
   ```

   Isso instalarÃ¡ todas as bibliotecas necessÃ¡rias e configurarÃ¡ o mÃ³dulo `src` para uso.

2. **Ativar o ambiente virtual:**

   ```bash
   poetry shell
   ```

3. **Configurar o Kernel do Jupyter (opcional):**

   ```bash
   python -m ipykernel install --user --name=brazilian_e_commerce --display-name "Python (brazilian_e_commerce)"
   ```

   Com isso, vocÃª poderÃ¡ selecionar este kernel nos seus notebooks do Jupyter ou VSCode.

## 1.3. Estrutura do Projeto

```text
brazilian_e-commerce_project/
├── data/
│   ├── external/       # Dados de fontes externas (APIs, web scraping, etc)
│   ├── interim/        # Dados transformados intermediários
│   ├── processed/      # Conjuntos de dados finais para modelagem
│   └── raw/            # Dados originais, imutáveis (dump do SQL/CSV original)
├── docs/               # Documentação do projeto e referências do dataset
├── models/             # Modelos treinados serializados (.pkl, .joblib, .onnx)
├── notebooks/          # Experimentos e análises (Jupyter Notebooks)
│   ├── 00_eda/         # Exploratory Data Analysis
│   ├── 01_version/     # version 1 de modelagem
│   └── 02_version/     # version 2 de modelagem
├── src/                # Código fonte modular e reutilizável
│   ├── __init__.py
│   ├── data/           # Scripts para baixar ou gerar dados (Ingestão)
│   ├── features/       # Scripts para transformar dados brutos em features
│   ├── models/         # Scripts para treinar modelos e fazer predições
│   └── visualization/  # Scripts para criar visualizações consistentes
├── tests/              # Testes unitários para o código em src/
├── config/             # Arquivos de configuração (YAML, .env)
├── .gitignore
├── Makefile            # Automação de tarefas (run_eda, train_model, etc)
├── pyproject.toml      # Gerenciamento de dependências (Poetry)
└── README.md
```

### 1.3.1. Principais notebooks

Atualmente, o projeto conta com os seguintes notebooks principais organizados por etapa:

- **`notebooks/00_eda/`**:
  - `01_exploracao.ipynb`: AnÃ¡lise exploratÃ³ria inicial dos dados.
  - `analise_exploratoria.ipynb`: Notebook com visualizaÃ§Ãµes detalhadas e descoberta de padrÃµes no dataset de E-commerce.

- **`notebooks/01_version/`**:
  - `0_data_prep_db.ipynb`: Notebook utilizado para o processo de preparaÃ§Ã£o e limpeza de dados para modelagem (versÃ£o inicial).

- **`notebooks/02_version/`**:
  - *(Reservado para futuras iteraÃ§Ãµes e melhorias de modelagem).*

## 1.4. Ferramentas de Qualidade e Automação

O projeto conta com ferramentas configuradas para padronizar o código, automatizar tarefas comuns e manter a qualidade do repositório.

### 1.4.1. Makefile (Automação de Tarefas)

O arquivo `Makefile` localizado na raiz do projeto concentra comandos úteis que podem ser executados rapidamente. Os principais são:

- **`make test`**: Executa todos os testes unitários da pasta `tests/`.
- **`make docs`**: Gera a documentação automática do projeto e salva na pasta `docs/`.
- **`make docs-serve`**: Inicia um servidor local na porta 8080 para visualizar a documentação no navegador.
- **`make clean`**: Limpa arquivos temporários do Python (`__pycache__`, `.pytest_cache`, `.pyc`).
- **`make pre-commit`**: Executa a rotina de pre-commit manualmente em todos os arquivos.

### 1.4.2. Pre-commit (Padronização e Linting)

Foi configurado o **pre-commit** junto com o formatador **Ruff**. Sempre que você tentar fazer um commit, o sistema fará a formatação do código, remoção de espaços em branco e validações automáticas.
Para ativar o pre-commit no repositório local, execute o comando uma única vez:

```bash
poetry run pre-commit install
```

### 1.4.3. Testes Unitários (`pytest`)

A pasta `tests/` deve espelhar a arquitetura da pasta `src/`. Para rodar os testes unitários de suas funções, utilize o atalho:

```bash
make test
```

O arquivo **`pytest.ini`** na raiz do projeto concentra as configurações base da suíte de testes. Ele serve para:

- Definir a pasta padrão de testes (`testpaths = tests`), garantindo que o pytest encontre os testes automaticamente.
- Especificar opções de formatação do output (`addopts = -ra -q`), para uma saída de erros mais clara e compacta no terminal.

### 1.4.4. Documentação Automática (`pdoc`)

Para gerar e visualizar a documentação automática do código-fonte (baseada nas docstrings das suas funções na pasta `src/`), utilize o atalho:

```bash
make docs
```

A documentação será gerada em HTML dentro da pasta `docs/`.
