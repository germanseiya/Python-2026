import plotly.express as px
import streamlit as st

from datos_ventas import (
    aplicar_estilos,
    cargar_ventas,
    conteo_top,
    filtros_sidebar,
    formato_miles,
    grafico_barras,
)

st.set_page_config(page_title="Clientes", page_icon="👥", layout="wide")
aplicar_estilos()

st.title("Dashboard de clientes")
df = filtros_sidebar(cargar_ventas())
clientes = (
    df.dropna(subset=["Cliente"])
    .groupby("Cliente")
    .agg(
        edad=("Edad", "first"),
        genero=("genero", "first"),
        estado_civil=("EstadoCivil", "first"),
        ocupacion=("Ocupacion", "first"),
        nacionalidad=("Nacionalidad", "first"),
        comuna=("ComunaCliente", "first"),
        region=("Region", "first"),
        ingreso=("INGRESO", "first"),
        cotizaciones=("NRO_COTIZACION", "size"),
        ventas=("ES_VENTA", "sum"),
    )
    .reset_index()
)
if clientes.empty:
    st.warning("No hay clientes con los filtros seleccionados.")
    st.stop()

k = st.columns(5)
k[0].metric("Clientes", formato_miles(len(clientes)))
k[1].metric("Clientes con venta", formato_miles((clientes["ventas"] > 0).sum()))
k[2].metric("Edad mediana", formato_miles(clientes["edad"].median()))
k[3].metric("Mujeres", f"{(clientes['genero'] == 'Femenino').mean():.1%}")
k[4].metric("Cotizaciones por cliente", formato_miles(clientes["cotizaciones"].mean(), 1))

col1, col2 = st.columns(2)
col1.plotly_chart(
    px.histogram(clientes.dropna(subset=["edad"]), x="edad", nbins=30, title="Distribución de edad",
                 labels={"edad": "Edad", "count": "Clientes"}),
    use_container_width=True,
)
col2.plotly_chart(
    px.pie(conteo_top(clientes["genero"]), names="categoria", values="cantidad", title="Género"),
    use_container_width=True,
)

col3, col4 = st.columns(2)
col3.plotly_chart(grafico_barras(clientes["estado_civil"], "Estado civil"), use_container_width=True)
col4.plotly_chart(grafico_barras(clientes["ingreso"], "Rango de ingreso"), use_container_width=True)

col5, col6 = st.columns(2)
col5.plotly_chart(grafico_barras(clientes["comuna"], "Comuna del cliente (top 15)", 15), use_container_width=True)
col6.plotly_chart(grafico_barras(clientes["ocupacion"], "Ocupación (top 15)", 15), use_container_width=True)

col7, col8 = st.columns(2)
col7.plotly_chart(grafico_barras(clientes["nacionalidad"], "Nacionalidad (top 10)"), use_container_width=True)
col8.plotly_chart(grafico_barras(clientes["region"], "Región (top 10)"), use_container_width=True)

st.subheader("Clientes con más ventas y cotizaciones")
tabla = clientes.sort_values(["ventas", "cotizaciones"], ascending=False).head(100).copy()
tabla["cliente"] = tabla["Cliente"].str[:12] + "…"
st.dataframe(
    tabla[["cliente", "cotizaciones", "ventas", "edad", "genero", "estado_civil", "comuna", "ingreso"]],
    hide_index=True,
    use_container_width=True,
)
