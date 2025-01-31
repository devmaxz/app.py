import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Titels en tekst
st.title('Welkom op mijn Streamlit Website!')
st.write('Dit is een eenvoudige webapplicatie die gebruik maakt van Streamlit.')

# Gebruikersinput: tekst invoeren
naam = st.text_input('Wat is je naam?', 'Jouw naam hier')

st.write(f'Hallo, {naam}!')

# Gebruikersinput: getal invoeren
getal = st.slider('Kies een getal', 0, 100, 25)
st.write(f'Je gekozen getal is: {getal}')

# Maak een eenvoudige grafiek
st.write('Hier is een grafiek van een lineaire functie.')

x = np.linspace(0, 10, 100)
y = getal * x

plt.plot(x, y)
st.pyplot(plt)

# Data weergeven in een tabel
data = pd.DataFrame({
    'Getallen': x,
    'Functie': y
})
st.write('Bekijk de onderstaande tabel:', data)
