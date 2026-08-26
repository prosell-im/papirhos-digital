import pandas as pd
from pathlib import Path


BASE = Path(__file__).resolve().parent

AUTORES_CSV = BASE / "autores.csv"
LIBROS_CSV = BASE / "libros.csv"
LIBROS_AUTORES_CSV = BASE / "libros_autores.csv"
EDICIONES_CSV = BASE / "ediciones.csv"


def leer_csv(ruta):
    if not ruta.exists():
        print(f"ERROR: No existe el archivo {ruta.name}")
        return None

    return pd.read_csv(ruta, dtype=str).fillna("")


def revisar_columnas(df, columnas_esperadas, nombre_archivo):
    errores = []

    columnas_actuales = set(df.columns)
    columnas_esperadas = set(columnas_esperadas)

    faltantes = columnas_esperadas - columnas_actuales
    extras = columnas_actuales - columnas_esperadas

    if faltantes:
        errores.append(
            f"{nombre_archivo}: faltan columnas: {', '.join(sorted(faltantes))}"
        )

    if extras:
        errores.append(
            f"{nombre_archivo}: columnas no esperadas: {', '.join(sorted(extras))}"
        )

    return errores


def revisar_ids_unicos(df, columna, nombre_archivo):
    errores = []

    if columna not in df.columns:
        return errores

    vacios = df[df[columna].str.strip() == ""]
    if not vacios.empty:
        errores.append(
            f"{nombre_archivo}: hay {len(vacios)} registros sin {columna}"
        )

    duplicados = df[df[columna].duplicated(keep=False) & (df[columna].str.strip() != "")]
    if not duplicados.empty:
        ids = sorted(duplicados[columna].unique())
        errores.append(
            f"{nombre_archivo}: IDs duplicados en {columna}: {', '.join(ids)}"
        )

    return errores


def revisar_relaciones(libros, autores, libros_autores, ediciones):
    errores = []

    ids_libros = set(libros["id_libro"].str.strip())
    ids_autores = set(autores["id_autor"].str.strip())

    relaciones_libros = set(libros_autores["id_libro"].str.strip())
    relaciones_autores = set(libros_autores["id_autor"].str.strip())

    libros_inexistentes = sorted(relaciones_libros - ids_libros - {""})
    if libros_inexistentes:
        errores.append(
            "libros_autores.csv: hay id_libro que no existen en libros.csv: "
            + ", ".join(libros_inexistentes)
        )

    autores_inexistentes = sorted(relaciones_autores - ids_autores - {""})
    if autores_inexistentes:
        errores.append(
            "libros_autores.csv: hay id_autor que no existen en autores.csv: "
            + ", ".join(autores_inexistentes)
        )

    libros_con_edicion = set(ediciones["id_libro"].str.strip())
    ediciones_inexistentes = sorted(libros_con_edicion - ids_libros - {""})
    if ediciones_inexistentes:
        errores.append(
            "ediciones.csv: hay id_libro que no existen en libros.csv: "
            + ", ".join(ediciones_inexistentes)
        )

    relaciones_repetidas = libros_autores[
        libros_autores.duplicated(subset=["id_libro", "id_autor"], keep=False)
    ]

    if not relaciones_repetidas.empty:
        pares = (
            relaciones_repetidas[["id_libro", "id_autor"]]
            .drop_duplicates()
            .apply(lambda fila: f"{fila['id_libro']} - {fila['id_autor']}", axis=1)
            .tolist()
        )

        errores.append(
            "libros_autores.csv: relaciones repetidas: "
            + ", ".join(pares)
        )

    return errores


def revisar_datos_faltantes_ediciones(ediciones):
    advertencias = []

    campos = [
        "edicion",
        "anio",
        "isbn_libro",
        "editorial",
    ]

    for _, fila in ediciones.iterrows():
        id_edicion = fila.get("id_edicion", "").strip()
        id_libro = fila.get("id_libro", "").strip()

        faltantes = [
            campo
            for campo in campos
            if str(fila.get(campo, "")).strip() == ""
        ]

        if faltantes:
            advertencias.append(
                f"{id_edicion or '(sin id_edicion)'} / {id_libro or '(sin id_libro)'}: "
                f"faltan {', '.join(faltantes)}"
            )

    return advertencias


def main():
    errores = []
    advertencias = []

    autores = leer_csv(AUTORES_CSV)
    libros = leer_csv(LIBROS_CSV)
    libros_autores = leer_csv(LIBROS_AUTORES_CSV)
    ediciones = leer_csv(EDICIONES_CSV)

    if any(df is None for df in [autores, libros, libros_autores, ediciones]):
        print("\nValidación detenida porque falta uno o más archivos.")
        return

    errores += revisar_columnas(
        autores,
        ["id_autor", "nombres", "apellidos"],
        "autores.csv",
    )

    errores += revisar_columnas(
        libros,
        [
            "id_libro",
            "titulo",
            "coleccion",
            "serie",
            "num_serie",
            "isbn_col",
            "tomo",
            "resumen",
            "estado",
        ],
        "libros.csv",
    )

    errores += revisar_columnas(
        libros_autores,
        ["id_libro", "id_autor"],
        "libros_autores.csv",
    )

    errores += revisar_columnas(
        ediciones,
        [
            "id_edicion",
            "id_libro",
            "edicion",
            "reimpresion",
            "anio",
            "isbn_libro",
            "editorial",
        ],
        "ediciones.csv",
    )

    errores += revisar_ids_unicos(autores, "id_autor", "autores.csv")
    errores += revisar_ids_unicos(libros, "id_libro", "libros.csv")
    errores += revisar_ids_unicos(ediciones, "id_edicion", "ediciones.csv")

    errores += revisar_relaciones(
        libros,
        autores,
        libros_autores,
        ediciones,
    )

    advertencias += revisar_datos_faltantes_ediciones(ediciones)

    print("\nVALIDACIÓN DE TABLAS DEL CATÁLOGO")
    print("=" * 40)

    if errores:
        print("\nERRORES:")
        for error in errores:
            print(f"- {error}")
    else:
        print("\nERRORES:")
        print("- No se encontraron errores estructurales.")

    if advertencias:
        print("\nADVERTENCIAS:")
        for advertencia in advertencias:
            print(f"- {advertencia}")
    else:
        print("\nADVERTENCIAS:")
        print("- No se encontraron datos faltantes en ediciones.")

    print("\nResumen:")
    print(f"- Autores: {len(autores)}")
    print(f"- Libros: {len(libros)}")
    print(f"- Relaciones libro-autor: {len(libros_autores)}")
    print(f"- Ediciones: {len(ediciones)}")


if __name__ == "__main__":
    main()