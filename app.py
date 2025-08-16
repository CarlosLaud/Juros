import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as st
import seaborn as sns
import matplotlib.dates as mdates

# 📥 Função para carregar os dados
@st.cache_data
def carregar_dados(caminho):
    return pd.read_csv(caminho)


def grafico_curva_juros(df):
# Criando a figura
    plt.style.use('fivethirtyeight')
#    df['Vcto'] = pd.to_datetime(df['Vcto'], dayfirst=True, errors='coerce')
    df['Vcto'] = pd.to_datetime(df['Vcto'],  errors='coerce')
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.suptitle('Evolução da Taxa Juros por prazo', fontsize=19, fontweight='bold')
    ax.plot(df.loc[:,'Vcto'].values, df.loc[:,'CurvaFF252'].values, color='blue', linewidth=2, 
        label='Curva ajustada')
    plt.scatter(df.loc[:,'Vcto'].values, df.loc[:,'Taxa'].values, color='orange', linewidth=2,
                label='valores reais')
    
    ax.xaxis.set_major_locator(mdates.YearLocator())               # Marca 1º de janeiro de cada ano
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))       # Exibe apenas o ano


    ax.legend(loc=[.9,.9])
        
    return fig


# 🔄 Carregar dados
caminho = r"https://raw.githubusercontent.com/CarlosLaud/Juros/refs/heads/main/dados/curva.csv"

df = carregar_dados(caminho)

dataref = "12/08/2025"


# 📊 Gráfico de valor de mercado
st.subheader("💰 Curva de Juros")
fig_valor = grafico_curva_juros(df)

st.pyplot(fig_valor)

caminho1 = r"https://raw.githubusercontent.com/CarlosLaud/Juros/refs/heads/main/dados/juros.csv"

df_juros = carregar_dados(caminho1)

def grafico_juros(df_juros):
    df_juros['dat'] = pd.to_datetime(df_juros['dat'],  errors='coerce')
    plt.style.use('fivethirtyeight')
    #plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.suptitle('Evolução da Taxa Juros por prazo', fontsize=19, fontweight='bold')
    ax.plot(df_juros.loc[:,'dat'].values, df_juros.loc[:,'ano_dez'].values, color='orange', linewidth=2, 
        label='dez anos')
    l, = ax.plot(df_juros.loc[:,'dat'].values, df_juros.loc[:,'ano_um'].values, color='blue', linewidth=2,
                label='um ano')
    l1, = ax.plot(df_juros.loc[:,'dat'].values, df_juros.loc[:,'meses3'].values, color='red', linewidth=1,
                label='três meses')
    lll, =ax.plot(df_juros.loc[:,'dat'].values, df_juros.loc[:,'Média'].values, color='black', linewidth=1,
                label='Média')
    ax.xaxis.set_major_locator(mdates.YearLocator())               # Marca 1º de janeiro de cada ano
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))       # Exibe apenas o ano

    ax.legend(loc=[.9,.9])
    plt.savefig("my_plot.png", transparent=True)
    return fig

st.subheader("💰 Evolução taxa de Juros")
fig = grafico_juros(df_juros)
st.pyplot(fig)


def grafico_curva_juros1(df):

    import plotly.graph_objects as go

    # Criando a figura
    fig = go.Figure()

    # Adicionando a linha

    fig.add_trace(go.Scatter(x=df['Vcto'], y=df['CurvaFF252'], mode='lines', name='Juros',
                            line=dict(color='blue', width=2)))

    # Adicionando os pontos (scatter)
    fig.add_trace(go.Scatter(x=df['Vcto'], y=df['Taxa'], mode='markers', name='Valor', marker=dict(size=8, color='red')))

    fig.update_layout(
        autosize=False,
        width=1500,  # Define a largura do gráfico
        height=600,  # Define a altura do gráfico
        margin=dict(l=50, r=50, b=100, t=100, pad=4)
    )

    # Configurando o layout

    fig.update_layout(
        title={
            'text': f"Evolução da Taxa Juros por prazo no dia {dataref}",
            'x': 0.5,                  # centraliza (0 = esquerda, 1 = direita)
            'xanchor': 'center',       # ancora o título ao centro
            'font': {
                'size': 24             # aumenta o tamanho da fonte
            }
        },
        xaxis_title="Data",
        yaxis_title="Juros"
    )

    fig.update_layout(
        yaxis=dict(tickformat=".2%")  # Exibe os valores como percentagem
    )
    return fig

# 📊 Gráfico de valor de mercado
st.subheader("💰 Curva de Juros")
fig_valor = grafico_curva_juros1(df)
#st.plotly_chart(fig_valor)
st.plotly_chart(fig_valor, use_container_width=True)