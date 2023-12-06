import streamlit as st 
import yfinance as yf
import pandas as pd




st.title("APLICATIVO FINANCEIRO") #titulo do aplictivo

tickers = ('TSLA', 'AAPL', 'MSFT', 'BTC-USD', 'ETH-USD') # Nomes da ações 

dropdown = st.multiselect('Escolha sua opção de ánalise', tickers) # Escolher as opçoes das ações

start = st.date_input('Começo', value= pd.to_datetime('2021-01-01')) # data de início 
end = st.date_input('Fim', value= pd.to_datetime('today')) # Data final 

# Função para selecionar a origem da Ação
def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret

if len(dropdown) > 0:
    #df = yf.download(dropdown, start, end)['Adj Close']
    df = relativeret(yf.download(dropdown,start,end)['Adj Close'])
    st.header('Ações selecionadas {}'.format(dropdown))
    st.line_chart(df)