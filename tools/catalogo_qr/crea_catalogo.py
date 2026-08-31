import os
import pandas as pd

# ==========================
# RUTAS DE ENTRADA / SALIDA
# ==========================

BASE = os.path.dirname(os.path.dirname(__file__))  #Representa papirhos-digital/tools
PROJECT_ROOT = os.path.dirname(BASE) #Representa papirhos-digital


AUTORES_CSV        = os.path.join(BASE, "catalogo_qr", "autores.csv")
LIBROS_AUTORES_CSV = os.path.join(BASE, "catalogo_qr", "libros_autores.csv")
LIBROS_CSV         = os.path.join(BASE, "catalogo_qr", "libros.csv")
EDICIONES_CSV      = os.path.join(BASE, "catalogo_qr", "ediciones.csv")
REIMPRESIONES_CSV = os.path.join(BASE, "catalogo_qr", "reimpresiones.csv")

SALIDA_CSV         = os.path.join(PROJECT_ROOT, "data", "catalogo.csv") #Representa papirhos-digital/data/catalogo.csv

# ==========================
# 1. LEER ARCHIVOS
# ==========================

autores        = pd.read_csv(AUTORES_CSV)        # columnas: id_autor, nombres, apellidos
libros_autores = pd.read_csv(LIBROS_AUTORES_CSV) # columnas: id_libro, id_autor
libros         = pd.read_csv(LIBROS_CSV)         # columnas: id_libro, titulo, coleccion, serie, num_serie, isbn_col, tomo, resumen, estado
ediciones      = pd.read_csv(EDICIONES_CSV)      # columnas: id_edicion, id_libro, edicion, anio, isbn_libro, editorial
reimpresiones  = pd.read_csv(REIMPRESIONES_CSV, dtype=str).fillna("") # columnas: id_reimpresion, id_libro, reimpresion, anio, isbn_libro, editorial

# Asegurarnos de tener nombres de columnas coherentes


# Llama las columnas de los archivos .csv, convierte los valores a strings y prepara los datos para su uso posterior. 

# ==========
# AUTORES
# ==========

#Crea una nueva columna 'autor_fmt' que combina nombres y apellidos.

autores["id_autor"]  = autores["id_autor"].astype(str).str.strip()
autores["nombres"]   = autores["nombres"].fillna("").astype(str)
autores["apellidos"] = autores["apellidos"].fillna("").astype(str)
autores["autor_fmt"] = autores["nombres"] + ">" + autores["apellidos"]

# ==========
# PROCESAR RELACIÓN LIBROS-AUTORES
# ==========

libros_autores["id_libro"] = libros_autores["id_libro"].astype(str).str.strip()
libros_autores["id_autor"] = libros_autores["id_autor"].astype(str).str.strip()

# ==========
# EDICIONES
# ==========

ediciones["id_edicion"] = ediciones["id_edicion"].astype(str).str.strip()
ediciones["id_libro"] = ediciones["id_libro"].astype(str).str.strip()

# ==========
# REIMPRESIONES 
# ==========

reimpresiones["id_reimpresion"] = reimpresiones["id_reimpresion"].astype(str).str.strip()
reimpresiones["id_edicion"] = reimpresiones["id_edicion"].astype(str).str.strip()
reimpresiones["reimpresion"] = (reimpresiones["reimpresion"]
                                .fillna("")
                                .astype(str)
                                .str.replace(".0", "", regex=False))

# ==========
# MERGE DE LIBROS_AUTORES CON AUTORES 
# ==========

al = libros_autores.merge(
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
# UNIR LIBROS + AUTORES AGRUPADOS + EDICIONES
# ==========================

#Libros + autores agrupados

catalogo = libros.merge(
    autores_por_libro,
    on="id_libro",
    how="left"
)

#Libros + autores agrupados + ediciones

catalogo = catalogo.merge(
    ediciones[["id_edicion", "id_libro", "edicion", "anio", "isbn_libro", "editorial"]],
    on="id_libro",
    how="left"
)

# Volver a llamar 'id_libro' simplemente 'id' para el CSV final
catalogo = catalogo.rename(columns={"id_libro": "id"})

# Limpia y estandariza los datos de las columnas numéricas y de texto

for columna in ["anio", "edicion", "tomo"]:
    catalogo[columna] = (
        catalogo[columna]
        .fillna("")
        .astype(str)
        .str.replace(".0", "", regex=False)
    )

# ==========================
# ORDENAR COLUMNAS COMO QUIERES
# ==========================

columnas_finales = [
    "id",
    "id_edicion",
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
    "resumen",
    "estado",
]

catalogo = catalogo[columnas_finales]

# ==========================
# GUARDAR CSV FINAL
# ==========================

catalogo.to_csv(SALIDA_CSV, index=False, lineterminator="\n")

print(f"Catálogo generado en: {SALIDA_CSV}")