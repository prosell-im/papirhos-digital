import csv, os, json

#Módulos propios
import escritor_catalogo #Escribe el texto que se agrega al catálogo
import crea_paginas #Crea las páginas completas de cada texto
import genera_json

BASE = os.path.dirname(os.path.dirname(__file__))
DOCS = os.path.join(BASE, "docs")
CSV_PATH = os.path.join(BASE, "data", "catalogo.csv")

#Corre el código al ejecutar el archivo
def main():
    
#-------------------------------------------------------- LECTURA DE BASE DE DATOS --------------------------------------------------------

    #Abre la base de datos CSV
    with open(CSV_PATH, newline="",encoding="utf-8") as f:
        reader = csv.DictReader(f) #Reader de la base de datos
        filas = list(reader) #Convierte los datos a una lista
    print(f"Filas leídas: {len(filas)}") #Confirmación de lectura de fichas

    # Agrupa todas las filas de un mismo libro en una lista, para que luego se pueda generar un JSON con todas sus ediciones

    filas_por_libro = {}

    for fila in filas:
        id_libro = (fila.get("id") or "").strip()

        if id_libro not in filas_por_libro:
           filas_por_libro[id_libro] = []

        filas_por_libro[id_libro].append(fila)

    # Una sola fila representativa por libro para el catálogo general.
    filas_unicas=[
          filas_libro[0]
          for filas_libro in filas_por_libro.values()
    ] 

    libros_dir = os.path.join(BASE,"docs","libros") #Dirección de guardado de los libros ---BASE/DOCS---- (Aquí se guardarán las páginas de MARKDOWN)
    os.makedirs(libros_dir,exist_ok=True) #Verifica la no sobreescritura del directorio

#------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------- Escritura de catálogo  --------------------------------------------------------

    #Escribe el catálogo con titulo, identificador, coleccion, serie, estado y un separador; regresa una lista cuyas entradas son espacios y estos textos
    lineas = escritor_catalogo.lista_catalogo(filas_unicas)
    catalogo_path = os.path.join(BASE, "docs", "catalogo.md") #Path para guardar el catálogo: BASE/docs
    with open(catalogo_path, "w", encoding = "utf-8") as fcat:
           fcat.write("\n".join(lineas))
    print("Catalogo actualizado")

#------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------- JSON, Buscador y páginas --------------------------------------------------------

    #Buscalibros
    DATA_DIR = os.path.join(DOCS, "data") #Establece dirección para el archivo JSON (DOCS/DATA)
    os.makedirs(DATA_DIR, exist_ok = True) #Verifica que exista para no sobrescribir


    data_json = []

    for filas_libro in filas_por_libro.values():
       data_json.append(genera_json.gjsn(filas_libro))

    # Temporalmente, crea_paginas sigue trabajando con una sola fila.
       crea_paginas.fila_a_obj(filas_libro)

    json_path = os.path.join(DATA_DIR, "catalogo.json") #Path del JSON

    with open(json_path, "w", encoding = "utf-8") as jf: #Abriendo el archivo JSON como JSNfile
           json.dump(data_json,jf,ensure_ascii = False, indent = 2)

    print("JSON exportado:", json_path)

#------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
            main()

