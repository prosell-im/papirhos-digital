import os 
import csv

import extractidatos

BASE = os.path.dirname(__file__)

REIMPRESIONES_CSV = os.path.join(
    BASE,
    "catalogo_qr",
    "reimpresiones.csv"
)


def cargar_reimpresiones():
    reimpresiones_por_edicion = {}

    if not os.path.exists(REIMPRESIONES_CSV):
        return reimpresiones_por_edicion

    with open(REIMPRESIONES_CSV, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            id_edicion = (fila.get("id_edicion") or "").strip()

            if not id_edicion:
                continue

            reimpresion = {
                "id_reimpresion": (fila.get("id_reimpresion") or "").strip(),
                "reimpresion": (fila.get("reimpresion") or "").strip(),
                "anio": (fila.get("anio") or "").strip(),
            }

            reimpresiones_por_edicion.setdefault(
                id_edicion,
                []
            ).append(reimpresion)

    return reimpresiones_por_edicion

def gjsn(filas_libro):
    # Recibe todas las filas correspondientes a un mismo libro.
    # Cada fila puede representar una edición diferente.

    if not filas_libro:
        return {}

    reimpresiones_por_edicion = cargar_reimpresiones()

    # Los datos generales del libro son iguales en todas sus ediciones,
    # así que usamos la primera fila como referencia.
    r = filas_libro[0]

    (
        autores,
        anio,
        _id,
        titulo,
        coleccion,
        serie,
        tomo,
        editorial,
        edicion,
        isbn_col,
        isbn_libro,
        estado,
        resumen,
        _
    ) = extractidatos.extractidatos(r)

    autores = [
        " ".join(autor[0]) + " " + " ".join(autor[1])
        for autor in autores
    ]

    # Información específica de cada edición
    ediciones = []

    for fila in filas_libro:
        id_edicion = (fila.get("id_edicion") or "").strip()


        ediciones.append({
            "id_edicion": id_edicion,
            "edicion": (fila.get("edicion") or "").strip(),
            "anio": (fila.get("anio") or "").strip(),
            "isbn_libro": (fila.get("isbn_libro") or "").strip(),
            "editorial": (fila.get("editorial") or "").strip(),
            "reimpresiones": reimpresiones_por_edicion.get(id_edicion, []),
        })

    return {
        "id": _id,
        "titulo": titulo,
        "autores": autores,
        "coleccion": coleccion,
        "serie": serie,
        "tomo": tomo,
        "isbn_col": isbn_col,
        "resumen": resumen,
        "estado": estado,

        # Compatibilidad temporal con el frontend actual
        "anio": anio,
        "editorial": editorial,
        "edicion": edicion,
        "isbn_libro": isbn_libro,

        # Nueva estructura
        "ediciones": ediciones,
    }

