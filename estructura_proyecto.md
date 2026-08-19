# Estructura del código:

## Objetivo : 
Descripción y resumen de la organización del proyecto. Archivos que deban manejarse con cuidado está señalados junto con un recorrido de el propósito de cada sección.


## data:
Archivos .csv ocupados como base de datos para los libros que se muestran en la página web. 
### Características de los archivos:
Cada archivo comparte datos similares con ciertas diferencias:
catalogo_old.csv: Recopilación de datos de solo ciertos libros
catalogo-pre.csv: Mayor cantidad de libros entre los tres
catalogo.csv: Prácticamente igual a catalogo-pre.csv. Tiene un libro menos
### Estado de uso:
- Pendiente de verificar:
- Sin referencias encontradas:
catalogo_old.csv, 
catalogo-pre.csv

### Observaciones pendientes:
¿Es necesario mantener en la carpeta los tres catálogos?
¿El atributo de <resumen> se toma de algún otro archivo o por qué algunos solo tienen resumen #?
En caso de mantener más de un catálogo, ¿cuál es el principal?


## docs:
Carpeta que contiene los archivos fuentes del contenido del sitio. Todo archivo en esta carpeta es utilizado directamente para el sitio web (MkDocs lo genera directamente)

### Estado de uso:
- Pendiente de verificar:
catalogo-unsort.json (editar)
- Sin referencias encontradas:

### Archivos importantes:
- Assets: Archivos fuentes para el sitio (imágenes, PDFs y logos)
- Páginas principales del sitio web: acerca.md, catalogo.md, explorar.md, index.md, tul.md
- Datos para el frontend: data/catalogo.json, catalogo.json

### Notas:
La carpeta pdfs_src contiene archivos fuente (assets). Sin embargo, en la misma sección (docs) se puede encontrar carpetas individuales de cada libro con su respectivo PDF con una marca de agua. Se usa watermark_to_book_folder.py para la elaboración de dichas carpetas. No se recomienda editar las versiones individuales.

En data, estos archivos son generados por /tools/genera_json.py.

Js contiene los archivos JavaScript encargados en la lógica interactiva del sitio (autentificación, lectura de datos, conexión con Supabase y acciones del usuario.)

Overrides y stylesheets contienen personalizaciones del tema de MkDocs, modificando componentes específicos sin alterar archivos originales como modificaciones en la apariencia visual.

Todos los archivos .md de esta carpeta son los archivos principales para el sitio web (contenido fuente en Markdown). Estos son transformados automáticamente por MkDocs en las páginas visibles para el usuario. 

### Observaciones pendientes:
-Verificar la utilidad de mantener catalogo-unsort.json y catalogo.json simultáneamente. Checar si es posible optimizar la parte de pdfs con y sin marca de agua.
-Es posible automatizar ordenando directamente catalogo-unsort y solo escribir catalogo.json

## legacy_files:
Archivos ya no relevantes en el proyecto que contienen versiones/código usado anteriormente.
### Observaciones pendientes:
¿Qué tan útil es mantener estos archivos?

## site:
Carpeta generada por MkDocs automáticamente de la carpeta \docs. Todo archivo markdown lo convierte a HTML. No se debe de modificar. En caso de querer cambiar algo del sitio, se debe de hacer la modificación en \docs y luego regenerar el sitio ('mkdocs build')
### Observaciones pendientes:
¿Cómo es publicada la página web (¿Desde Github Pages o por qué está versionada?)?

## tools:
Serie de scripts que generan, transforman y organizan los datos y recursos del proyecto (csv, json, páginas o recursos) que posteriormente son utilizados por el sitio.

### Scripts que generan datos:
- crea_catalogo.py -> /data/catalogo-csv 
Archivos en uso: autores.csv, libros_autores.csv, resumenes.csv, libros.csv
- pipeline_archivos -> /docs/catalogo.md
- watermark_to_book_folders.py -> /docs/assets/pdfs_src

### Scripts que generan contenido del sitio:
- crea_paginas.py: Crea páginas individuales de cada libro 
Archivos generados: /docs/libros 
Scripts usados: , mostrador_PDF (bloque_pdf), escribe_metadatos.py, extractidatos.py
- mostrador_PDF.py: Verifica si existe la versión del PDF con marca de agua y genera el bloque de visualización y descarga en su página individual. En caso de no existir muestra "disponible próximamente". Los enlaces incluyen identificadores para el seguimiento de descargas.
Notas: Se puede limpiar el código (variables no usadas e inconsistencias con la descripción)


### Scripts que preparan archivos:
-escribe_metadatos.py: Función auxiliar que recibe los datos bibliográficos de un libro y genera una tabla en formato md con los campos disponibles. 
-escritor_catalogo.py: Recibe una lista de datos de los libros y genera las líneas de Markdown del catálogo general.
-extractidatos.py: Extrae todos los campos de una fila en un orden fijo (cuidado con alterar el orden). 
Scripts usados: mostrador_PDF (bloque_pdf)
-genera_json.py: Devuelve un diccionario compatible para generar el archivo JSON (no genera el JSON)
Scripts usados: extractidatos.py
Notas: Revisar imports y variables no utilizados.

### Scripts que automatizan un flujo:
-pipeline_archivos.py: Coordina varios de los otros archivos de /tools y genera casi todo lo relacionado con el catálogo
Scripts usados: escritor_catalogo, crea_paginas, genera_json, catalogo.csv


### Estado de uso: 
-Sin referencias encontradas: 
escritor_bibtex.py 

### Observaciones pendientes:
-El nombre y descripción de escritor_bibtex.py en 'README.txt' no coincide con su contenido actual. Mas allá de eso, se duplica parcialmente la función escribe_metadatos, donde se genera directamente el bloque Bibtex en crea_paginas con la función mencionada.
-Actualizar y corregir descripciones de los archivos en el README
-Acabar de añadir los links/ textos en watermark_to_book_folders.py



## Archivos raíz:
-Manejar con cuidado mkdocs.yml

## Observaciones pendientes:
-Agregar al .gitignore, si es posible, los archivos temporales generados por Python (__pycache__, )
-Cambiar el site_name en mkdocs.yml 

## Posibles mejoras al código:
- Confirmar el uso de archivos en la sección principal
- Analizar la posibilidad de trasladar ciertos documentos a legacy files
<<<<<<< HEAD
- Evaluar si ciertos archivos son necesario o se pueden generar a partir del catálogo principal.
=======
- Evaluar si ciertos archivos son necesarios o se pueden generar a partir del catálogo principal.
>>>>>>> 9f325b5b9b354b4aa10c3ea86b5a4b6e9a076b10
-Consistencia en los datos (archivos con más o menos libros que en otros)