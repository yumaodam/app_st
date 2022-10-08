import streamlit as st
import pandas as pd

st.write("# Gráfico interativo")

if "lista" not in st.session_state:
    st.session_state["lista"] = []

#Usuário digita um número
numero_digitado = st.number_input('Insert a number')

#Qaundo o botão é pressionado
if st.button('Adiciona número') == True:
    st.session_state["lista"].append(numero_digitado)

#Plota o gráfico
st.line_chart(st.session_state["lista"])
st.session_state