import pandas as pd
import mysql.connector
from mysql.connector import Error

def carregar_dados_mysql():
    print("--- INICIANDO PROCESSO ETL (Extract, Transform, Load) ---")
    
    # 1. Leitura do CSV (Extract)
    try:
        df = pd.read_csv('vendas_loja.csv')
        print(f"Lendo CSV: {len(df)} registros encontrados.")
    except FileNotFoundError:
        print("Erro: CSV não encontrado.")
        return

    # 2. Conexão com MySQL
    config = {
        'user': 'root',
        'password': 'euamorepolho1*',  
        'host': 'localhost',
        'database': 'loja_dados'
    }

    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            cursor = connection.cursor()
            print("Conectado ao MySQL com sucesso!")

            # 3. Criação da Tabela (Transform - Modelagem)
            cursor.execute("DROP TABLE IF EXISTS vendas;")
            
            tabela_sql = """
            CREATE TABLE vendas (
                id_venda INT PRIMARY KEY,
                data DATE,
                produto VARCHAR(100),
                categoria VARCHAR(50),
                quantidade INT,
                preco_unitario DECIMAL(10, 2),
                valor_total DECIMAL(10, 2),
                vendedor VARCHAR(50),
                cidade VARCHAR(50)
            );
            """
            cursor.execute(tabela_sql)
            print("Tabela 'vendas' criada/recriada.")

            # 4. Inserção dos Dados (Load)
            # Prepara a query de INSERT
            sql_insert = """
            INSERT INTO vendas (id_venda, data, produto, categoria, quantidade, preco_unitario, valor_total, vendedor, cidade)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            # Converte o DataFrame para uma lista de tuplas para inserir em massa
            # Tratamento para garantir tipos nativos do Python (int/float) em vez de numpy types
            dados_para_inserir = [tuple(x) for x in df.to_numpy()]
            
            cursor.executemany(sql_insert, dados_para_inserir)
            connection.commit()
            
            print(f"Sucesso! {cursor.rowcount} registros inseridos no banco de dados.")

    except Error as e:
        print(f"Erro ao conectar ou inserir no MySQL: {e}")
        
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão com MySQL encerrada.")

if __name__ == "__main__":
    carregar_dados_mysql()