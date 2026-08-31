def escribe_bibtex(
    id_edicion,
    id_libro,
    titulo,
    autores,
    anio,
    editorial,
    edicion,
    isbn_libro
):
    # Cada edición debe tener una clave BibTeX única.
    clave = id_edicion if id_edicion else id_libro

    campos = []

    if titulo:
        campos.append(f"title = {{{titulo}}}")

    if autores:
        campos.append(f"author = {{{' and '.join(autores)}}}")

    if anio:
        campos.append(f"year = {{{anio}}}")

    if editorial:
        campos.append(f"publisher = {{{editorial}}}")

    if edicion:
        campos.append(f"edition = {{{edicion}}}")

    if isbn_libro:
        campos.append(f"isbn = {{{isbn_libro}}}")

    campos.append("address = {México}")

    contenido = ",\n".join(campos)

    return f"""@BOOK{{{clave},
{contenido}
}}"""