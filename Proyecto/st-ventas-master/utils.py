from pathlib import Path
import pandas as pd
import streamlit as st

DATA_FILE = Path(__file__).resolve().parent / "data" / "ventas_prediccion.csv"

@st.cache_data
def _read_csv(path: str, modified_time: float) -> pd.DataFrame:
    return pd.read_csv(path, low_memory=False)

def load_data() -> pd.DataFrame:
    if "df_ventas" not in st.session_state:
        if not DATA_FILE.exists():
            st.error(f"No se encontró el archivo: {DATA_FILE}")
            st.stop()
        st.session_state.df_ventas = _read_csv(str(DATA_FILE), DATA_FILE.stat().st_mtime)
    return st.session_state.df_ventas

def save_data(data: pd.DataFrame) -> None:
    data.to_csv(DATA_FILE, index=False, encoding="utf-8-sig")
    st.session_state.df_ventas = data.copy()
    _read_csv.clear()

def get_options(data: pd.DataFrame, column: str) -> list[str]:
    if column not in data.columns:
        return []
    values = data[column].dropna().astype(str).str.strip()
    return sorted(v for v in values.unique() if v and v.lower() != "nan")

def safe_text(value) -> str:
    return "" if pd.isna(value) else str(value)

def safe_number(value) -> float:
    number = pd.to_numeric(value, errors="coerce")
    return 0.0 if pd.isna(number) else float(number)

def format_money(value) -> str:
    return "—" if pd.isna(value) else f"${value:,.0f}".replace(",", ".")
