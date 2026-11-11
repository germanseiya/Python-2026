import pandas as pd
import streamlit as st
from utils import load_data

st.title("🔎 Explorador y exportación")
df = load_data()
search = st.text_input("Buscar por operación, RUT, proyecto o unidad")
view = df.copy()
if search.strip():
    mask = pd.Series(False, index=view.index)
    for col in ["idoperacion", "RutCliente", "Proyecto", "Unidad", "ID_unidad_cubit"]:
        if col in view:
            mask |= view[col].astype(str).str.contains(search.strip(), case=False, na=False, regex=False)
    view = view[mask]
st.caption(f"{len(view):,} registros encontrados")
st.dataframe(view, use_container_width=True, hide_index=True)
st.download_button("⬇️ Descargar CSV actualizado", data=df.to_csv(index=False).encode("utf-8-sig"),
                   file_name="ventas_departamentos_actualizado.csv", mime="text/csv")
st.warning("La aplicación guarda cambios en el CSV local. Mantén un respaldo y no publiques datos personales o comerciales.")
