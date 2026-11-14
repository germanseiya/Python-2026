import folium
import streamlit as st
from streamlit_folium import st_folium

from datos_ventas import aplicar_estilos, cargar_ventas, formato_miles

st.set_page_config(page_title="Geomapa", page_icon="🗺️", layout="wide")
aplicar_estilos()

st.title("Geomapa de proyectos")
df = cargar_ventas().dropna(subset=["PROYECTO", "latitud", "longitud"])

proyectos = (
    df.groupby("PROYECTO")
    .agg(
        latitud=("latitud", "first"),
        longitud=("longitud", "first"),
        cotizaciones=("NRO_COTIZACION", "size"),
        ventas=("ES_VENTA", "sum"),
        precio_lista=("PrecioLista", "mean"),
    )
    .reset_index()
)

seleccion = st.multiselect("Proyectos a mostrar", sorted(proyectos["PROYECTO"]))
if not seleccion:
    st.info("Selecciona uno o más proyectos para verlos en el mapa.")
    st.stop()

visibles = proyectos[proyectos["PROYECTO"].isin(seleccion)]

mapa = folium.Map(location=[visibles["latitud"].mean(), visibles["longitud"].mean()], zoom_start=11)
for _, fila in visibles.iterrows():
    folium.Marker(
        location=[fila["latitud"], fila["longitud"]],
        tooltip=fila["PROYECTO"],
        popup=(
            f"<b>{fila['PROYECTO']}</b><br>"
            f"Cotizaciones: {formato_miles(fila['cotizaciones'])}<br>"
            f"Ventas: {formato_miles(fila['ventas'])}"
        ),
    ).add_to(mapa)

if len(visibles) > 1:
    mapa.fit_bounds(
        [[visibles["latitud"].min(), visibles["longitud"].min()],
         [visibles["latitud"].max(), visibles["longitud"].max()]]
    )

st_folium(mapa, height=520, use_container_width=True, returned_objects=[])

st.subheader("Resumen de proyectos seleccionados")
st.dataframe(
    visibles.rename(columns={
        "PROYECTO": "Proyecto",
        "latitud": "Latitud",
        "longitud": "Longitud",
        "cotizaciones": "Cotizaciones",
        "ventas": "Ventas",
        "precio_lista": "Precio lista promedio",
    }),
    hide_index=True,
    use_container_width=True,
)
