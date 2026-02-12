# Portfólio de Análise de Vendas (End-to-End) 📊

Oi! 👋 Esse é um dos meus primeiros projetos práticos focados na minha transição de carreira para **Análise de Dados**. 

A ideia aqui foi sair um pouco da teoria e construir um **pipeline completo** do zero: desde a criação dos dados até um dashboard interativo, simulando o dia a dia real de uma empresa de varejo.

## O que eu fiz no projeto?

Basicamente, criei todo o fluxo de dados:

1.  **Geração de Dados**: Criei um script Python (`generate_data.py`) que gera vendas, produtos e clientes fictícios de forma realista.
2.  **Banco de Dados**: Modelei um banco no **MySQL** e criei um script de ETL (`etl_mysql.py`) para tratar e carregar os dados brutos lá para dentro automaticamente.
3.  **Dashboard**: Desenvolvi um site interativo com **Streamlit** (`dashboard.py`) que conecta no banco e mostra os indicadores em tempo real.

## Como rodar (se quiser testar)

Você vai precisar ter o Python e o MySQL instalados na sua máquina.

1.  Clone o repositório.
2.  Instale as bibliotecas necessárias:
    ```bash
    pip install pandas mysql-connector-python streamlit plotly
    ```
3.  Crie um Schema chamado `loja_dados` no seu MySQL.
4.  Configure suas credenciais no arquivo `etl_mysql.py` e `dashboard.py`.
5.  Rode os scripts na ordem:
    ```bash
    python generate_data.py  # Gera o CSV
    python etl_mysql.py      # Joga pro Banco
    streamlit run dashboard.py # Abre o site
    ```

## Ferramentas que usei
-   **Python** (Pandas para análise, Faker para dados)
-   **SQL** (MySQL para armazenamento e queries)
-   **Streamlit & Plotly** (Visualização de dados)
-   **Git** (Versionamento)

---
*Desenvolvido por Juliana Malheiros.* 🚀
