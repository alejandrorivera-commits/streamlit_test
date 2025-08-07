import streamlit as st
import random

st.header('🪙 Lanzar una moneda')

number_of_trials = st.slider('¿Número de lanzamientos?', 1, 1000, 10)
start_button = st.button('Lanzar')

if start_button:
    resultados = [random.choice(['Cara', 'Cruz']) for _ in range(number_of_trials)]
    caras = resultados.count('Cara')
    cruces = resultados.count('Cruz')

    st.subheader('🧾 Resultados')
    st.write(f'Caras: {caras}')
    st.write(f'Cruces: {cruces}')

    st.subheader('📊 Distribución')
    st.bar_chart({'Resultados': {'Cara': caras, 'Cruz': cruces}})
