import plotly.express as px
import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards

from datos_ventas import (
    aplicar_estilos,
    cargar_ventas,
    conteo_top,
    filtros_sidebar,
    formato_miles,
    grafico_barras,
)

st.set_page_config(page_title="Panel de ventas", page_icon="📊", layout="wide")
aplicar_estilos()

df = filtros_sidebar(cargar_ventas())
st.title("Panel de ventas y cotizaciones")
if df.empty:
    st.warning("No hay registros con los filtros seleccionados.")
    st.stop()

cotizaciones = len(df)
ventas = int(df["ES_VENTA"].sum())
en_promesa = int((df["estadoproducto"] == "Promesa").sum())
desistidos = int((df["estadoproducto"] == "Desistido").sum())

st.subheader("Ventas")
c = st.columns(5)
c[0].metric("Cotizaciones", formato_miles(cotizaciones))
c[1].metric("Ventas (escrituradas)", formato_miles(ventas))
c[2].metric("Tasa de conversión", f"{ventas / cotizaciones:.1%}")
c[3].metric("Precio lista promedio", formato_miles(df["PrecioLista"].mean()))
c[4].metric("En promesa / desistidos", f"{formato_miles(en_promesa)} / {formato_miles(desistidos)}")

style_metric_cards()

ventas_mes = (
    df[df["ES_VENTA"] & df["FECHAESCRITURACION"].notna()]
    .assign(mes=lambda d: d["FECHAESCRITURACION"].dt.to_period("M").dt.to_timestamp())
    .groupby("mes")
    .size()
    .reset_index(name="ventas")
)
col1, col2 = st.columns(2)
col1.plotly_chart(
    px.bar(ventas_mes, x="mes", y="ventas", title="Ventas escrituradas por mes",
           labels={"mes": "", "ventas": "Ventas"}),
    use_container_width=True,
)

top_proyectos = df["PROYECTO"].value_counts().head(10).index
por_proyecto = (
    df[df["PROYECTO"].isin(top_proyectos)]
    .groupby(["PROYECTO", "estadoproducto"])
    .size()
    .reset_index(name="registros")
)
col2.plotly_chart(
    px.bar(por_proyecto, x="registros", y="PROYECTO", color="estadoproducto", orientation="h",
           barmode="stack", title="Estado por proyecto (top 10)",
           labels={"PROYECTO": "", "registros": "Registros"}),
    use_container_width=True,
)

col3, col4 = st.columns(2)
col3.plotly_chart(grafico_barras(df["FORMA_PAGO"], "Forma de pago (top 10)"), use_container_width=True)

medios = (
    df.groupby("MEDIO_LLEGADA")
    .agg(cotizaciones=("NRO_COTIZACION", "size"), ventas=("ES_VENTA", "sum"))
    .sort_values("cotizaciones", ascending=False)
    .head(10)
    .reset_index()
)
medios["conversion"] = medios["ventas"] / medios["cotizaciones"]
col4.plotly_chart(
    px.bar(medios.sort_values("conversion"), x="conversion", y="MEDIO_LLEGADA", orientation="h",
           title="Conversión por medio de llegada (top 10)",
           labels={"conversion": "Conversión", "MEDIO_LLEGADA": ""})
    .update_xaxes(tickformat=".0%"),
    use_container_width=True,
)

st.subheader("Características de los clientes")
clientes = df.dropna(subset=["Cliente"]).drop_duplicates("Cliente")
k = st.columns(4)
k[0].metric("Clientes únicos", formato_miles(len(clientes)))
k[1].metric("Edad mediana", formato_miles(clientes["Edad"].median()))
k[2].metric("Mujeres", f"{(clientes['genero'] == 'Femenino').mean():.1%}")
k[3].metric("Con hijos", f"{(clientes['Hijos'] > 0).sum() / clientes['Hijos'].notna().sum():.1%}")

col5, col6 = st.columns(2)
col5.plotly_chart(
    px.pie(conteo_top(clientes["genero"]), names="categoria", values="cantidad", title="Género"),
    use_container_width=True,
)
col6.plotly_chart(grafico_barras(clientes["EstadoCivil"], "Estado civil"), use_container_width=True)
