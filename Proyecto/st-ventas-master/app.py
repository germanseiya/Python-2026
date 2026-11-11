import pandas as pd
import streamlit as st
from utils import load_data, save_data, get_options

#st.set_page_config(page_title="Gestión inmobiliaria", page_icon="🏢", layout="wide")

st.title("👤 Ingreso de nuevos clientes")
df = load_data()
st.write("Completa el formulario para incorporar un nuevo cliente.")
with st.form("form_nuevo_cliente", clear_on_submit=True):
    a, b, c = st.columns(3)
    rut = a.text_input("RUT del cliente *")
    nombre = b.text_input("Nombre / razón de compra *")
    email = c.text_input("Correo electrónico")
    d, e, f = st.columns(3)
    telefono = d.text_input("Teléfono")
    proyecto = e.selectbox("Proyecto", get_options(df, "Proyecto") or ["Por definir"])
    razon = f.selectbox("Razón de compra", get_options(df, "RAZON_COMPRA") or ["No informado"])
    g, h, i = st.columns(3)
    unidad = g.selectbox("Unidad", ["Sin asignar"] + get_options(df, "Unidad"))
    grupo = h.selectbox("Grupo de llegada", get_options(df, "GRUPO_LLEGADA") or ["No informado"])
    medio = i.selectbox("Medio de llegada", get_options(df, "MEDIO_LLEGADA") or ["No informado"])
    j, k, l = st.columns(3)
    origen = j.selectbox("Origen de visita", get_options(df, "ORIGEN_VISITA") or ["No informado"])
    ingreso = k.selectbox("Tramo de ingreso", get_options(df, "INGRESO_RENTA") or ["No informado"])
    genero = l.selectbox("Género", ["No informado", "F", "M", "Otro"])
    fecha = st.date_input("Fecha de cotización")
    acepta = st.checkbox("Confirmo que los datos fueron proporcionados para fines de gestión comercial.")
    submitted = st.form_submit_button("Guardar nuevo cliente", type="primary")

if submitted:
    if not rut.strip() or not nombre.strip():
        st.error("RUT y Nombre / razón de compra son obligatorios.")
    elif not acepta:
        st.warning("Debes confirmar el uso de los datos antes de guardar.")
    else:
        record = {col: pd.NA for col in df.columns}
        if "idoperacion" in df:
            ids = pd.to_numeric(df["idoperacion"], errors="coerce")
            record["idoperacion"] = int(ids.max()) + 1 if ids.notna().any() else 1
        values = {
            "RutCliente": rut.strip(), "RAZON_COMPRA": razon, "Proyecto": proyecto,
            "Unidad": "" if unidad == "Sin asignar" else unidad,
            "GRUPO_LLEGADA": grupo, "MEDIO_LLEGADA": medio, "ORIGEN_VISITA": origen,
            "INGRESO_RENTA": ingreso, "Genero": genero, "FechaCotizacion": fecha.isoformat(),
            "NombreCliente": nombre.strip(), "EmailCliente": email.strip(), "TelefonoCliente": telefono.strip()
        }
        record.update(values)
        save_data(pd.concat([df, pd.DataFrame([record])], ignore_index=True))
        st.success(f"Cliente guardado. ID de operación: {record.get('idoperacion', 'No asignado')}.")
        st.rerun()
st.caption("Los campos marcados con * son obligatorios.")
