- [1. Brazilian E-Commerce Project](#1-brazilian-e-commerce-project)
  - [1.1. Conjunto de Dados](#11-conjunto-de-dados)
    - [1.1.1. Esquema de dados](#111-esquema-de-dados)
  - [1.2. Configuração do Ambiente Local](#12-configuração-do-ambiente-local)
    - [1.2.1. Configurando o Poetry](#121-configurando-o-poetry)
  - [1.3. Estrutura do Projeto](#13-estrutura-do-projeto)
    - [1.3.1. Principais notebooks](#131-principais-notebooks)

# 1. Brazilian E-Commerce Project

Este projeto tem o objetivo de realizar uma análise exploratória com esse conjunto de dados públicos de E-commerce Brasileiro.
As análises e modelagens de dados serão realizadas utilizando Python e bibliotecas como `Pandas`, `Matplotlib` e `Scikit-Learn`.
Por fim, o objetivo principal é preparar as features e construir um **`Modelo de Machine Learning`** preditivo para os dados.

Para desenvolvimento desse projeto foi realizado o download do conjunto de dados no formato CSV no Link: [Kaggle - Brazilian E-commerce Data](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/data).

Os dados originais podem ser manipulados localmente para desenvolvimento de habilidades com ferramentas de dados e modelagem.

## 1.1. Conjunto de Dados

Este é um conjunto de dados públicos de comércio eletrônico brasileiro de pedidos feitos na [Olist Store](https://www.olist.com/). O conjunto de dados conta com informações de 100 mil pedidos de 2016 a 2018 feitos em vários marketplaces no Brasil. Seus recursos permitem visualizar um pedido em várias dimensões: desde o status do pedido, preço, desempenho de pagamento e frete até a localização do cliente, atributos do produto e, finalmente, avaliações escritas pelos clientes.

O Olist conecta pequenas empresas de todo o Brasil aos canais sem complicações e com um único contrato. Esses comerciantes podem vender seus produtos por meio da Olist Store e enviá-los diretamente aos clientes usando os parceiros logísticos do Olist.

Depois que um cliente compra o produto na Olist Store, um vendedor é notificado para atender a esse pedido. Assim que o cliente recebe o produto, ou a data estimada de entrega é devida, o cliente recebe uma pesquisa de satisfação por e-mail onde pode dar uma nota para a experiência de compra e anotar alguns comentários.

**Ponto de atenção:** Um pedido pode ter vários itens.
Cada item pode ser atendido por um vendedor distinto.
Todos os textos que identificam lojas e parceiros foram substituídos pelos nomes das grandes casas de Game of Thrones.

### 1.1.1. Esquema de dados

Os dados são divididos em vários conjuntos de dados para melhor compreensão e organização.
Esquema dos dados:
![Esquema de Dados](data\archive\Esquema_dados.png)

## 1.2. Configuração do Ambiente Local

Para trabalhar neste projeto, utilizaremos o **Poetry** para gerenciamento de dependências.

### 1.2.1. Configurando o Poetry

O arquivo **`pyproject.toml`** já está definido no repositório. Para instalar as dependências e o pacote local `src`, siga os passos:

1. **Instalar dependências com Poetry:**
   ```bash
   poetry install
   ```
   Isso instalará todas as bibliotecas necessárias e configurará o módulo `src` para uso.

2. **Ativar o ambiente virtual:**
   ```bash
   poetry shell
   ```

3. **Configurar o Kernel do Jupyter (opcional):**
   ```bash
   python -m ipykernel install --user --name=brazilian_e_commerce --display-name "Python (brazilian_e_commerce)"
   ```
   Com isso, você poderá selecionar este kernel nos seus notebooks do Jupyter ou VSCode.

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
│   ├── 00_eda/              # Exploratory Data Analysis
│   ├── 01_feature_modeling/ # Feature Engineering & Modeling
│   └── 02_model_development/# Machine Learning Model Training
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

