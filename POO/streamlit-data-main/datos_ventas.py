"""Carga, limpieza, filtrado y edición de los registros de ventas y cotizaciones."""

import csv
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

RAIZ = Path(__file__).resolve().parent
ARCHIVO_ORIGINAL = RAIZ / "data" / "vista-ventas-analisis.csv"
ARCHIVO_EDITADO = RAIZ / "data" / "ventas_editadas.csv"
ARCHIVO_CSS = RAIZ / "style" / "style.css"

ESTADO_VENTA = "Escrituracion"
NULO = "NULL"
GENEROS = {"M": "Masculino", "F": "Femenino"}

COLUMNAS_NUMERICAS = [
    "NRO_COTIZACION", "PISO", "METROS", "PrecioLista", "Descuento",
    "DIAS_COTIZACION", "DIAS_RESERVA", "DIAS_PROMESA", "DIAS_ESCRITURACION",
    "DIAS_ENTREGA", "IDPROYECTO", "ESTADOflujo", "Edad", "Hijos", "latitud", "longitud",
]
COLUMNAS_FECHA = [
    "FECHAVISITA", "FECHACOTIZACION", "FECHARESERVA", "FECHAPROMESA", "FECHARESCILIACION",
    "FECHAESCRITURACION", "FechaAgendada", "FechaEntrega", "FechaLiberacion", "Nacimiento",
]


def _nulos(serie: pd.Series) -> pd.Series:
    return serie.str.strip().mask(lambda s: s.isin([NULO, ""]))


def leer_crudo(ruta: Path) -> pd.DataFrame:
    """Lee el CSV conservando todos los valores como texto tal como están en el archivo."""
    return pd.read_csv(ruta, dtype=str, keep_default_na=False, encoding="utf-8")


def guardar_crudo(crudo: pd.DataFrame, ruta: Path) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with ruta.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(crudo.columns)
        escritor.writerows(crudo.itertuples(index=False, name=None))


def tipar(crudo: pd.DataFrame) -> pd.DataFrame:
    """Convierte el texto crudo a tipos analizables (decimales con coma, fechas, nulos)."""
    df = crudo.copy()
    texto = [c for c in crudo.columns if c not in COLUMNAS_NUMERICAS + COLUMNAS_FECHA]
    for col in texto:
        df[col] = _nulos(df[col])
    for col in [c for c in COLUMNAS_NUMERICAS if c in df.columns]:
        df[col] = pd.to_numeric(_nulos(df[col]).str.replace(",", ".", regex=False), errors="coerce")
    for col in [c for c in COLUMNAS_FECHA if c in df.columns]:
        df[col] = pd.to_datetime(_nulos(df[col]), format="%Y-%m-%d", errors="coerce")

    df["genero"] = df["genero"].map(GENEROS).fillna("Sin dato")
    # Edades fuera de un rango plausible (p. ej. valores negativos o 235) se tratan como faltantes.
    df["Edad"] = df["Edad"].where(df["Edad"].between(18, 100))
    df["ES_VENTA"] = df["estadoproducto"] == ESTADO_VENTA
    return df


@st.cache_data(show_spinner="Cargando registros...")
def _cargar_crudo(ruta: str, mtime: float) -> pd.DataFrame:
    return leer_crudo(Path(ruta))


@st.cache_data(show_spinner="Cargando registros...")
def _cargar_tipado(ruta: str, mtime: float) -> pd.DataFrame:
    return tipar(leer_crudo(Path(ruta)))


def _ruta_vigente() -> Path:
    return ARCHIVO_EDITADO if ARCHIVO_EDITADO.exists() else ARCHIVO_ORIGINAL


def cargar_crudo() -> pd.DataFrame:
    ruta = _ruta_vigente()
    return _cargar_crudo(str(ruta), ruta.stat().st_mtime)


def cargar_ventas() -> pd.DataFrame:
    ruta = _ruta_vigente()
    return _cargar_tipado(str(ruta), ruta.stat().st_mtime)


def formato_miles(valor, decimales: int = 0) -> str:
    if pd.isna(valor):
        return "—"
    texto = f"{valor:,.{decimales}f}"
    return texto.replace(",", "X").replace(".", ",").replace("X", ".")


def formatear_numero(valor: float) -> str:
    """Formato del CSV original: decimales con coma y sin ceros innecesarios."""
    numero = float(valor)
    if numero.is_integer():
        return str(int(numero))
    return repr(numero).replace(".", ",")


def valor_crudo(valor) -> str:
    if pd.isna(valor):
        return NULO
    if isinstance(valor, pd.Timestamp):
        return valor.strftime("%Y-%m-%d")
    if isinstance(valor, str):
        return valor.strip() or NULO
    return formatear_numero(valor)


def actualizar_registro(crudo: pd.DataFrame, indice: int, cambios: dict[str, str]) -> pd.DataFrame:
    nuevo = crudo.copy()
    for columna, valor in cambios.items():
        nuevo.at[indice, columna] = valor
    return nuevo


def conteo_top(serie: pd.Series, n: int | None = None) -> pd.DataFrame:
    conteo = serie.dropna().value_counts()
    if n is not None:
        conteo = conteo.head(n)
    return conteo.rename_axis("categoria").reset_index(name="cantidad")


def grafico_barras(serie: pd.Series, titulo: str, n: int = 10):
    conteo = conteo_top(serie, n).sort_values("cantidad")
    return px.bar(conteo, x="cantidad", y="categoria", orientation="h", title=titulo,
                  labels={"cantidad": "Registros", "categoria": ""})


def filtros_sidebar(df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header("Filtros")
    proyectos = st.sidebar.multiselect("Proyecto", sorted(df["PROYECTO"].dropna().unique()))
    estados = st.sidebar.multiselect("Estado", sorted(df["estadoproducto"].dropna().unique()))

    fechas = df["FECHACOTIZACION"].dropna()
    if not fechas.empty:
        rango = st.sidebar.date_input(
            "Fecha de cotización",
            value=(fechas.min().date(), fechas.max().date()),
            min_value=fechas.min().date(),
            max_value=fechas.max().date(),
        )
        if isinstance(rango, tuple) and len(rango) == 2:
            inicio, fin = (pd.Timestamp(f) for f in rango)
            df = df[df["FECHACOTIZACION"].between(inicio, fin)]

    if proyectos:
        df = df[df["PROYECTO"].isin(proyectos)]
    if estados:
        df = df[df["estadoproducto"].isin(estados)]
    return df


def aplicar_estilos() -> None:
    if ARCHIVO_CSS.exists():
        css = ARCHIVO_CSS.read_text(encoding="utf-8")
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
