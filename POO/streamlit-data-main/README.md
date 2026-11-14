

# Streamlit-data
Ciencia de Datos

#### Pasos para la instalación
En el terminal de VS code:

crear el entorno de Python
```bash
uv venv --pyhton 3.14
```
activar el entorno
```bash
source .venv/bin/activate  # For Linux/Mac
.venv\Scripts\activate     # For Windows
```
```bash
uv init
```
cargar las dependencias predefinidas. **Importante** use las versiones de Pandas (2.3.3) y Numpy (2.5.4) que se indican.
```bash
uv add -r requirements.txt
```
Sincronizar las fuentes
```bash
uv sync
```

## App de ventas y cotizaciones

Análisis de `data/vista-ventas-analisis.csv`, organizado con páginas automáticas de Streamlit (carpeta `pages/`):

- **Panel** (`app.py`): resumen de ventas y características de los clientes.
- **Clientes** (`pages/1_clientes.py`): dashboard de clientes.
- **Geomapa** (`pages/2_geomapa.py`): mapa de los proyectos seleccionados.
- **Editar venta** (`pages/3_editar_venta.py`): formulario para modificar una venta.

Una "venta" es un registro con `estadoproducto = Escrituracion`.

Las ediciones se guardan en `data/ventas_editadas.csv`; el archivo original no se modifica. Si ese archivo existe, las páginas lo usan en lugar del original.

Ejecutar la app:
```bash
python -m streamlit run app.py
```
o
```bash
streamlit run app.py
```
Tests:
```bash
python -m pytest tests
```

