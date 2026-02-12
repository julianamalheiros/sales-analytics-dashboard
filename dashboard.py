import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

# Função para conectar ao MySQL
def get_data_from_mysql():
    config = {
        'user': 'root',
        'password': 'euamorepolho1*', 
        'host': 'localhost',
        'database': 'loja_dados'
    }
    conn = mysql.connector.connect(**config)
    query = "SELECT * FROM vendas"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.title("📊 Dashboard de Vendas em Tempo Real")

try:
    df = get_data_from_mysql()
    
    st.sidebar.header("Filtros")
    cidade = st.sidebar.multiselect(
        "Selecione a Cidade:",
        options=df["cidade"].unique(),
        default=df["cidade"].unique()
    )
    
    df_selection = df.query("cidade == @cidade")

    total_vendas = int(df_selection["valor_total"].sum())
    media_vendas = round(df_selection["valor_total"].mean(), 2)
    qtd_transacoes = len(df_selection)

    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Faturamento Total", f"R$ {total_vendas:,}")
    col2.metric("📈 Ticket Médio", f"R$ {media_vendas:,}")
    col3.metric("🛒 Qtd. Vendas", f"{qtd_transacoes}")

    st.markdown("---")

    col_graf1, col_graf2 = st.columns(2)

    with col_graf1:
        vendas_produto = df_selection.groupby("produto")["valor_total"].sum().reset_index()
        fig_produto = px.bar(vendas_produto, x="valor_total", y="produto", orientation="h", title="Top Produtos")
        st.plotly_chart(fig_produto, use_container_width=True)

    with col_graf2:
        vendas_categoria = df_selection.groupby("categoria")["valor_total"].sum().reset_index()
        fig_categoria = px.pie(vendas_categoria, values="valor_total", names="categoria", title="Por Categoria")
        st.plotly_chart(fig_categoria, use_container_width=True)

except Exception as e:
    st.error(f"Erro: {e}")