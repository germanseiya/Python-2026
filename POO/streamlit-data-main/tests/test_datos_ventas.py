import pandas as pd

from datos_ventas import (
    actualizar_registro,
    formatear_numero,
    guardar_crudo,
    leer_crudo,
    tipar,
)

CABECERA = "NRO_COTIZACION,estadoproducto,PrecioLista,FECHAESCRITURACION,genero,Edad,FORMA_PAGO\n"
FILA_1 = "1,Escrituracion,\"6837\",2024-03-01,M,40,Contado \n"
FILA_2 = "2,Desistido,\"65,34\",NULL,0,235,Credito\n"


def _archivo(tmp_path, contenido=CABECERA + FILA_1 + FILA_2):
    ruta = tmp_path / "ventas.csv"
    ruta.write_text(contenido, encoding="utf-8")
    return ruta


def test_tipar_convierte_decimales_fechas_y_nulos(tmp_path):
    df = tipar(leer_crudo(_archivo(tmp_path)))

    assert df.loc[0, "PrecioLista"] == 6837
    assert df.loc[1, "PrecioLista"] == 65.34
    assert pd.isna(df.loc[1, "FECHAESCRITURACION"])
    assert df.loc[0, "FORMA_PAGO"] == "Contado"
    assert df.loc[0, "genero"] == "Masculino"
    assert pd.isna(df.loc[1, "Edad"])
    assert df["ES_VENTA"].tolist() == [True, False]


def test_guardar_sin_cambios_conserva_los_valores_originales(tmp_path):
    original = _archivo(tmp_path)
    destino = tmp_path / "editado.csv"

    guardar_crudo(leer_crudo(original), destino)

    pd.testing.assert_frame_equal(leer_crudo(destino), leer_crudo(original))
    assert leer_crudo(destino).loc[0, "FORMA_PAGO"] == "Contado "


def test_edicion_persiste_y_actualiza_es_venta(tmp_path):
    crudo = leer_crudo(_archivo(tmp_path))
    editado = actualizar_registro(crudo, 1, {"estadoproducto": "Escrituracion", "PrecioLista": "65,5"})
    destino = tmp_path / "editado.csv"

    guardar_crudo(editado, destino)
    df = tipar(leer_crudo(destino))

    assert df.loc[1, "ES_VENTA"]
    assert df.loc[1, "PrecioLista"] == 65.5
    assert df.loc[0, "PrecioLista"] == 6837


def test_formatear_numero_usa_formato_del_csv():
    assert formatear_numero(6837.0) == "6837"
    assert formatear_numero(65.34) == "65,34"
