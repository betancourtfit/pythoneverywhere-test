from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    
    gemini = ChatGoogleGenerativeAI(model="gemini-pro")

    # Construir el prompt como un string
    prompt = f"Tengo un {animal_type} y quiero un buen nombre para él, es de color {pet_color}. sugiéreme 5 nombres"

    # Invocar el modelo directamente con el string del prompt
    response = gemini.invoke(prompt)
    pet_name = response.content

    # Asumiendo que la respuesta es un string, adaptar según sea necesario
    return pet_name
