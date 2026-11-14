from datetime import datetime

import pandas as pd
import streamlit as st

from datos_ventas import (
    ARCHIVO_EDITADO,
    actualizar_registro,
    aplicar_estilos,
    cargar_crudo,
    cargar_ventas,
    guardar_crudo,
    valor_crudo,
)

st.set_page_config(page_title="Editar venta", page_icon="✏️", layout="wide")
aplicar_estilos()

TEXTO = ["FORMA_PAGO", "UNIDAD", "ORIENTACION", "TIPOLOGIA", "MotivoDesistimiento", "BancoHipotecario"]
NUMERO = ["PISO", "METROS", "PrecioLista", "Descuento"]
FECHAS = ["FECHARESERVA", "FECHAPROMESA", "FECHAESCRITURACION"]

st.title("Editar venta")
st.caption(
    f"Los cambios se guardan en `{ARCHIVO_EDITADO.name}`. "
    "El archivo original no se modifica."
)

todas = cargar_ventas()
if todas.empty:
    st.warning("No hay registros disponibles.")
    st.stop()

if "mensaje_guardado" in st.session_state:
    st.success(st.session_state.pop("mensaje_guardado"))

proyecto = st.selectbox("Proyecto", ["Todos"] + sorted(todas["PROYECTO"].dropna().unique()))
df = todas if proyecto == "Todos" else todas[todas["PROYECTO"] == proyecto]

def etiqueta(indice: int) -> str:
    fila = df.loc[indice]
    return (
        f"Línea {indice + 2} · Cotización {fila['NRO_COTIZACION']:.0f} · "
        f"{fila['PROYECTO']} · {fila['UNIDAD']} · {fila['estadoproducto']}"
    )

indice = st.selectbox("Venta a editar", df.index, format_func=etiqueta)
registro = df.loc[indice]

with st.form(f"form-{indice}"):
    st.subheader("Estado y características")
    estados = sorted(todas["estadoproducto"].dropna().unique())
    valores = {}
    columnas = st.columns(3)
    valores["estadoproducto"] = columnas[0].selectbox(
        "Estado",
        estados,
        index=estados.index(registro["estadoproducto"]) if registro["estadoproducto"] in estados else 0,
        key=f"{indice}-estadoproducto",
    )
    for i, col in enumerate(TEXTO):
        valores[col] = columnas[(i + 1) % 3].text_input(
            col, value="" if pd.isna(registro[col]) else registro[col], key=f"{indice}-{col}"
        )
    for i, col in enumerate(NUMERO):
        valor = registro[col]
        valores[col] = columnas[i % 3].number_input(
            col, value=None if pd.isna(valor) else float(valor), key=f"{indice}-{col}"
        )

    st.subheader("Fechas (AAAA-MM-DD, vacío para eliminar)")
    columnas_fecha = st.columns(3)
    for i, col in enumerate(FECHAS):
        valor = registro[col]
        valores[col] = columnas_fecha[i].text_input(
            col, value="" if pd.isna(valor) else valor.strftime("%Y-%m-%d"), key=f"{indice}-{col}"
        )

    guardar = st.form_submit_button("Guardar cambios", type="primary")

if guardar:
    errores = []
    nuevos = {}
    for col in FECHAS:
        texto = valores[col].strip()
        if not texto:
            nuevos[col] = pd.NaT
            continue
        try:
            nuevos[col] = pd.Timestamp(datetime.strptime(texto, "%Y-%m-%d"))
        except ValueError:
            errores.append(f"{col}: usa el formato AAAA-MM-DD.")

    if errores:
        for error in errores:
            st.error(error)
    else:
        cambios = {}
        for col in TEXTO + NUMERO + ["estadoproducto"] + FECHAS:
            nuevo = nuevos.get(col, valores.get(col))
            if valor_crudo(nuevo) != valor_crudo(registro[col]):
                cambios[col] = valor_crudo(nuevo)

        if not cambios:
            st.info("No hay cambios para guardar.")
        else:
            crudo = cargar_crudo()
            guardar_crudo(actualizar_registro(crudo, indice, cambios), ARCHIVO_EDITADO)
            st.session_state["mensaje_guardado"] = (
                f"Venta actualizada. Campos modificados: {', '.join(cambios)}."
            )
            st.rerun()
