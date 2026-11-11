import streamlit as st

st.set_page_config(page_title="Gestión inmobiliaria", page_icon="🏢", layout="wide")
st.title("🏢 Gestión de ventas y departamentos")
st.markdown("""
Bienvenido a la aplicación de análisis y gestión comercial inmobiliaria.

Selecciona una página en el menú lateral:
- **Dashboard:** indicadores y gráficos de ventas y cotizaciones.
- **Ingreso de clientes:** registro de nuevos clientes.
- **Edición de departamentos:** modificación de registros existentes.
- **Explorador y exportación:** búsqueda y descarga de los datos.
""")
st.info("Los cambios se guardan en `ventas_prediccion.csv`. Realiza respaldos periódicos.")
