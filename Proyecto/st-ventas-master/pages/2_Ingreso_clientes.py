import pandas as pd
import streamlit as st
from utils import load_data, get_options, format_money

st.title("📊 Dashboard de ventas y cotizaciones")
df = load_data()
work = df.copy()
for col in ["FechaCotizacion", "FECHA_RESERVA", "FechaReserva", "FechaFirmaPromesa", "FechaFirmaEscrituraCliente"]:
    if col in work:
        work[col] = pd.to_datetime(work[col], errors="coerce")
for col in ["PRECIO_VENTA", "PRECIO_TOTAL", "PRECIO_LISTA_ACTUAL", "PRECIO_LISTA_DIA_VENTA", "DESCUENTOS"]:
    if col in work:
        work[col] = pd.to_numeric(work[col], errors="coerce")

st.caption(f"{len(work):,} registros · {work.shape[1]} columnas")
st.info("El CSV no contiene un estado comercial explícito (cotización, reserva, venta o escrituración). Los indicadores se basan en fechas registradas y operaciones distintas; no representan necesariamente estados comerciales definitivos.")

st.subheader("Filtros")
c1, c2, c3 = st.columns(3)
projects = get_options(work, "Proyecto")
selected_projects = c1.multiselect("Proyecto", projects, default=projects)
groups = get_options(work, "GRUPO_LLEGADA")
selected_groups = c2.multiselect("Grupo de llegada", groups)
years = sorted(work["FechaCotizacion"].dropna().dt.year.unique().tolist()) if "FechaCotizacion" in work else []
selected_years = c3.multiselect("Año de cotización", years, default=years)
filtered = work.copy()
if "Proyecto" in filtered and selected_projects:
    filtered = filtered[filtered["Proyecto"].astype(str).isin(selected_projects)]
if "GRUPO_LLEGADA" in filtered and selected_groups:
    filtered = filtered[filtered["GRUPO_LLEGADA"].astype(str).isin(selected_groups)]
if "FechaCotizacion" in filtered and selected_years:
    filtered = filtered[filtered["FechaCotizacion"].dt.year.isin(selected_years)]

ops = filtered["idoperacion"].nunique() if "idoperacion" in filtered else 0
quotes = int(filtered["FechaCotizacion"].notna().sum()) if "FechaCotizacion" in filtered else 0
deeds = int(filtered["FechaFirmaEscrituraCliente"].notna().sum()) if "FechaFirmaEscrituraCliente" in filtered else 0
k1, k2, k3, k4 = st.columns(4)
k1.metric("Registros", f"{len(filtered):,}")
k2.metric("Operaciones distintas", f"{ops:,}")
k3.metric("Con fecha de cotización", f"{quotes:,}")
k4.metric("Con fecha de escritura", f"{deeds:,}")
m1, m2 = st.columns(2)
m1.metric("Precio de venta promedio", format_money(filtered["PRECIO_VENTA"].mean()) if "PRECIO_VENTA" in filtered else "—")
m2.metric("Descuento promedio", format_money(filtered["DESCUENTOS"].mean()) if "DESCUENTOS" in filtered else "—")
left, right = st.columns(2)
with left:
    st.subheader("Registros por proyecto")
    if "Proyecto" in filtered:
        st.bar_chart(filtered["Proyecto"].fillna("Sin dato").value_counts().head(15))
with right:
    st.subheader("Registros por grupo de llegada")
    if "GRUPO_LLEGADA" in filtered:
        st.bar_chart(filtered["GRUPO_LLEGADA"].fillna("Sin dato").value_counts().head(12))
if "FechaCotizacion" in filtered:
    st.subheader("Evolución mensual de cotizaciones registradas")
    monthly = filtered.dropna(subset=["FechaCotizacion"]).assign(Mes=lambda x: x["FechaCotizacion"].dt.to_period("M").astype(str)).groupby("Mes").size()
    if not monthly.empty:
        st.line_chart(monthly)
show_cols = [c for c in ["idoperacion", "Proyecto", "Etapa", "Unidad", "FechaCotizacion", "PRECIO_VENTA", "GRUPO_LLEGADA", "MEDIO_LLEGADA"] if c in filtered]
st.subheader("Detalle de registros")
st.dataframe(filtered[show_cols], use_container_width=True, hide_index=True)
