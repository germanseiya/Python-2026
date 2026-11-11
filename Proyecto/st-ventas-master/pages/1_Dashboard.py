import pandas as pd
import streamlit as st
from utils import load_data, save_data, safe_text, safe_number

st.title("🏠 Edición de departamentos")
df = load_data()
if "idoperacion" not in df:
    st.error("El CSV no contiene la columna idoperacion.")
    st.stop()
st.write("Selecciona un registro. La posición de fila se utiliza porque idoperacion puede repetirse.")
labels = [f"Fila {i} · Op. {safe_text(r.get('idoperacion'))} · {safe_text(r.get('Proyecto'))} · Unidad {safe_text(r.get('Unidad'))}" for i, r in df.iterrows()]
selected = st.selectbox("Registro que deseas editar", labels)
row_index = labels.index(selected)
row = df.iloc[row_index]
with st.form("form_editar_departamento"):
    a, b, c = st.columns(3)
    proyecto = a.text_input("Proyecto", safe_text(row.get("Proyecto")))
    etapa = b.text_input("Etapa", safe_text(row.get("Etapa")))
    unidad = c.text_input("Unidad", safe_text(row.get("Unidad")))
    d, e, f = st.columns(3)
    id_cubit = d.text_input("ID unidad Cubit", safe_text(row.get("ID_unidad_cubit")))
    precio_lista = e.number_input("Precio lista actual", min_value=0.0, value=safe_number(row.get("PRECIO_LISTA_ACTUAL")), step=100000.0)
    precio_venta = f.number_input("Precio de venta", min_value=0.0, value=safe_number(row.get("PRECIO_VENTA")), step=100000.0)
    statuses = ["No especificada", "En comercialización", "Reservada", "Vendida", "Escriturada"]
    current = safe_text(row.get("EtapaComercial"))
    status_index = statuses.index(current) if current in statuses else 0
    g, h = st.columns(2)
    status = g.selectbox("Etapa comercial", statuses, index=status_index)
    active_value = row.get("UnidadActiva", True)
    active = h.checkbox("Unidad activa para comercialización", value=bool(active_value) if pd.notna(active_value) else True)
    confirm = st.checkbox("Confirmo que deseo actualizar este registro.")
    submitted = st.form_submit_button("Guardar cambios", type="primary")
if submitted:
    if not confirm:
        st.warning("Debes confirmar la actualización.")
    else:
        updated = df.copy()
        changes = {"Proyecto": proyecto, "Etapa": etapa, "Unidad": unidad, "ID_unidad_cubit": id_cubit,
                   "PRECIO_LISTA_ACTUAL": precio_lista, "PRECIO_VENTA": precio_venta,
                   "EtapaComercial": status, "UnidadActiva": active}
        for col, value in changes.items():
            updated.loc[updated.index[row_index], col] = value
        save_data(updated)
        st.success("Registro actualizado correctamente.")
        st.rerun()
st.subheader("Registro seleccionado")
st.dataframe(df.iloc[[row_index]], use_container_width=True)
