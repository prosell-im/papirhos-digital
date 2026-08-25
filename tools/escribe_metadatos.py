def escribe_metadatos(
    autores,
    coleccion,
    serie,
    tomo,
    anio,
    editorial,
    edicion,
    reimpresion,
    isbn_col,
    isbn_libro
):
    auts = [
        " ".join(autor[0]) + " " + " ".join(autor[1])
        for autor in autores
    ]

    def opt(label, val):
        if val and val != "nan":
            return f"<tr><th>{label}</th><td>{val}</td></tr>"
        return ""

    filas = (
        opt("Autores", ", ".join(auts) if auts else "")
        + opt("Colección", coleccion)
        + opt("Serie", serie)
        + opt("Tomo", tomo)
        + opt("Año", anio)
        + opt("Editorial", editorial)
        + opt("Edición", edicion)
        + opt("Reimpresión", reimpresion)
        + opt("ISBN (Colección)", isbn_col)
        + opt("ISBN (Texto)", isbn_libro)
    )

    return f"""
<table>
    <tbody>
        {filas}
    </tbody>
</table>
"""