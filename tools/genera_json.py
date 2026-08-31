import extractidatos


def gjsn(filas_libro):
    # Recibe todas las filas correspondientes a un mismo libro.
    # Cada fila puede representar una edición diferente.

    if not filas_libro:
        return {}

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
        ediciones.append({
            "id_edicion": (fila.get("id_edicion") or "").strip(),
            "edicion": (fila.get("edicion") or "").strip(),
            "anio": (fila.get("anio") or "").strip(),
            "isbn_libro": (fila.get("isbn_libro") or "").strip(),
            "editorial": (fila.get("editorial") or "").strip(),
            "reimpresiones": []
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

