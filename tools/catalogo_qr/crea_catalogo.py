import os
import pandas as pd

# ==========================
# RUTAS DE ENTRADA / SALIDA
# ==========================

BASE = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(BASE)


AUTORES_CSV        = os.path.join(BASE, "catalogo_qr", "autores.csv")
LIBROS_AUTORES_CSV = os.path.join(BASE, "catalogo_qr", "libros_autores.csv")
LIBROS_CSV         = os.path.join(BASE, "catalogo_qr", "libros.csv")
EDICIONES_CSV      = os.path.join(BASE, "catalogo_qr", "ediciones.csv")

SALIDA_CSV         = os.path.join(PROJECT_ROOT, "data", "catalogo.csv")

# ==========================
# 1. LEER ARCHIVOS
# ==========================

autores        = pd.read_csv(AUTORES_CSV)        # columnas: id_autor, nombres, apellidos
libros_autores = pd.read_csv(LIBROS_AUTORES_CSV) # columnas: id_libro, id_autor
libros         = pd.read_csv(LIBROS_CSV)         # columnas: id_libro, titulo, coleccion, ...
ediciones      = pd.read_csv(EDICIONES_CSV)      # columnas: id_edicion, id_libro, edicion, reimpresion, anio, isbn_libro, editorial

# Asegurarnos de tener nombres de columnas coherentes

# ==========
# AUTORES
# ==========

autores["id_autor"]  = autores["id_autor"].astype(str).str.strip()
autores["nombres"]   = autores["nombres"].fillna("").astype(str)
autores["apellidos"] = autores["apellidos"].fillna("").astype(str)
autores["autor_fmt"] = autores["nombres"] + ">" + autores["apellidos"]

# ==========
# 3. PROCESAR RELACIÓN LIBROS-AUTORES
# ==========

libros_autores["id_libro"] = libros_autores["id_libro"].astype(str).str.strip()
libros_autores["id_autor"] = libros_autores["id_autor"].astype(str).str.strip()

al = libros_autores.copy()  # Copia para no modificar el original

# ==========
# EDICIONES
# ==========

ediciones["id_edicion"] = ediciones["id_edicion"].astype(str).str.strip()
ediciones["id_libro"] = ediciones["id_libro"].astype(str).str.strip()

# ==========
# MERGE PARA OBTENER EL TEXTO DE CADA AUTOR
# ==========

al = al.merge(
    autores[["id_autor", "autor_fmt"]],
    on="id_autor",
    how="left"
)

# Evitar NaN y asegurarnos de que todo sea str
al["autor_fmt"] = al["autor_fmt"].fillna("").astype(str)

# ==========
# AGRUPAR POR LIBRO → CADENA CON TODOS LOS AUTORES
# ==========

autores_por_libro = (
    al.groupby("id_libro")["autor_fmt"]
      .apply(lambda s: ", ".join([x for x in s if x != ""]))
      .reset_index(name="autores")
)

# ==========================
# 4. UNIR LIBROS + AUTORES
# ==========================

catalogo = libros.merge(
    autores_por_libro,
    on="id_libro",
    how="left"
)

catalogo = catalogo.merge(
    ediciones[["id_libro", "edicion", "reimpresion", "anio", "isbn_libro", "editorial"]],
    on="id_libro",
    how="left"
)

# Volver a llamar 'id_libro' simplemente 'id' para el CSV final
catalogo = catalogo.rename(columns={"id_libro": "id"})
catalogo["anio"] = catalogo["anio"].fillna("").astype(str).str.replace(".0", "", regex=False)
catalogo["edicion"] = catalogo["edicion"].fillna("").astype(str).str.replace(".0", "", regex=False)
catalogo["reimpresion"] = catalogo["reimpresion"].fillna("").astype(str).str.replace(".0", "", regex=False)
catalogo["tomo"] = catalogo["tomo"].fillna("").astype(str).str.replace(".0", "", regex=False)

# ==========================
# 5. ORDENAR COLUMNAS COMO QUIERES
# ==========================

columnas_finales = [
    "id",
    "titulo",
    "autores",
    "coleccion",
    "serie",
    "num_serie",
    "isbn_col",
    "isbn_libro",
    "tomo",
    "anio",
    "editorial",
    "edicion",
    "reimpresion",
    "resumen",
    "estado",
]

# Por si acaso alguna columna faltara, filtramos a las que existan
columnas_existentes = [c for c in columnas_finales if c in catalogo.columns]
catalogo = catalogo[columnas_existentes]

# ==========================
# 6. GUARDAR CSV FINAL
# ==========================

catalogo.to_csv(SALIDA_CSV, index=False, lineterminator="\n")
print(f"Catálogo generado en: {SALIDA_CSV}")