import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.write("#Produção Grega")

separador = st.selectbox(
    'Selecione o separador de dados',
    (';', ',', ' '))

st.write('You selected:', separador)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as string:
    dataframe = pd.read_csv(uploaded_file, sep = separador)
    st.write(dataframe)
