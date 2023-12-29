import langchain_helper as lch
import streamlit as st

st.title("Generador de nombres para mascotas")
st.markdown("Este es un generador de nombres para mascotas. Escriba el tipo de animal que tiene y presione el botón 'Generar nombres'.")

animal_type = st.sidebar.selectbox("¿cual es tu mascota?",("gato","perro","cabra","vaca","hamster","conejo","pato","loro","pez","tortuga","serpiente","rana","caballo","oveja","cerdo","gallo","pavo","burro","gallina","pavo"))

if animal_type == "gato":
    pet_color = st.sidebar.text_area(label="¿De qué color es tu gato?", max_chars=15)
if animal_type == "perro":
    pet_color = st.sidebar.text_area(label="¿De qué color es tu perro?", max_chars=15)
    
if pet_color:
    pet_name = lch.generate_pet_name(animal_type, pet_color)
    st.text(pet_name)

