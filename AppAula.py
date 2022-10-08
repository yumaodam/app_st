import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.write("# Aplicativo Yuma")

'''
## 1. Imprimir sem o write
    1. Primeiro elemento da lista
    2. Segundo elemento

## 2. Mostrando uma tabela 
'''

separador = st.selectbox(
    'Selecione o separador de dados',
    (';', ',', ' '))

st.write('You selected:', separador)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as string:
    dataframe = pd.read_csv(uploaded_file, sep = separador)
    st.write(dataframe)

'''
## 3. Gerando um histograma de valores aleatórios
'''
intervalo = int(st.text_input('Digite o número de intervalos', '3'))


fig, ax = plt.subplots(1,1)
ax.hist(np.random.normal(20,2,100), bins = intervalo)
fig.set_size_inches(2,2)
fig
plt.show()

'''
## 4. Usando slider
'''
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

df = pd.DataFrame(([(-25.49, -49.20)]),columns=['lat', 'lon'])
st.map(df)
