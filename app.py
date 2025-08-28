import streamlit as st

# Título del aplicativo
st.title("Conversor de Temperatura: Celsius a Fahrenheit 🌡️")

# Instrucciones
st.write("Ingresa una temperatura en grados Celsius para convertirla a Fahrenheit.")

# Entrada del usuario
celsius = st.number_input("Temperatura en Celsius", min_value=-273.15, step=0.1, format="%.2f")

# Conversión
fahrenheit = (celsius * 9/5) + 32

# Mostrar el resultado
st.success(f"{celsius:.2f} °C son {fahrenheit:.2f} °F")
