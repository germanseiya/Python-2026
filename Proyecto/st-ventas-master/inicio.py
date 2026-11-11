import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards

st.title("¡Hola, Streamlit!")
st.write("Esta es mi primera aplicación con Streamlit.")


# Crear tres columnas para las métricas principales
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Ingresos", value="$5,000", delta="10%")
with col2:
    st.metric(label="Gastos", value="$2,000", delta="-5%", delta_color="inverse")
with col3:
    st.metric(label="Usuarios Activos", value="1,200", delta="150")

style_metric_cards()