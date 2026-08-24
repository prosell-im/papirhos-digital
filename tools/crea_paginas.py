import os
from textwrap import dedent

import extractidatos
import escribe_metadatos

BASE = os.path.dirname(os.path.dirname(__file__))
DOCS = os.path.join(BASE, "docs")

def fila_a_obj(filas_libro):
       r = filas_libro[0]  # Usamos la primera fila como referencia para los metadatos del libro
       autores, anio, _id, titulo, coleccion, serie, tomo, editorial, edicion, isbn_col, isbn_libro, estado, resumen, downs = extractidatos.extractidatos(r)

       #Autores para citar:
       #Recuerda que se recibe una lista del tipo [[nombre1, nombre2], [apellido1, apellido2]]
       autsnor = [" ".join(autor[0]) + " " + " ".join(autor[1]) for autor in autores]

       #Autores bibtex:
       
       autbib =  [autor[1][0] +", "+ autor[0][0] for autor in autores]


       #Obtención de gráficos
       covername = f"assets/covers/{_id}"
       cover_rel = covername+".png" 
       cover_abs = os.path.join(DOCS, cover_rel)
       cover_file = f'\"../../{cover_rel}\"' if os.path.exists(cover_abs) else '\"../../'+covername+'.jpg\"' 

       #Escritor de chip para la página de ficha
       def chip(label, val, emoji):
              return f'<span class ="chip"></span class ="icon">{emoji}</span> {val}</span>' if val else ""
       chips = " ".join(x for x in [chip("Serie", serie, "🏷"), chip("Colección", coleccion, "📚"), chip("Año", anio, "🗓"), chip("Estado", estado.replace("_", " "), "ℹ️") ] if x
                        )
       #Tabla de metadatos
       metadatos = escribe_metadatos.escribe_metadatos(autores, coleccion, serie, tomo, anio, editorial, edicion, isbn_col, isbn_libro)


       bloques_ediciones = []

       for fila in filas_libro:
              id_edicion = (fila.get("id_edicion") or "").strip()
              num_edicion = (fila.get("edicion") or "").strip()
              reimpresion = (fila.get("reimpresion") or "").strip()
              anio_edicion = (fila.get("anio") or "").strip()
              isbn_edicion = (fila.get("isbn_libro") or "").strip()
              editorial_edicion = (fila.get("editorial") or "").strip()

              titulo_edicion = (
                     f"Edición {num_edicion}"
                     if num_edicion
                     else "Edición sin especificar"
              )

              datos_edicion = [
                     f"- **Año:** {anio_edicion}" if anio_edicion else "",
                     f"- **Editorial:** {editorial_edicion}" if editorial_edicion else "",
                     f"- **ISBN:** {isbn_edicion}" if isbn_edicion else "",
                     f"- **Reimpresión:** {reimpresion}" if reimpresion else "",
              ]

              datos_edicion = "\n".join(
                     dato for dato in datos_edicion if dato
              )

              bloques_ediciones.append(
                     f"""### {titulo_edicion}

{datos_edicion if datos_edicion else "Información editorial pendiente."}
"""
              )

       seccion_ediciones = "\n".join(bloques_ediciones)

  
       #YAML front matter para búsqueda SEO
       front_matter = dedent(f"""\
       ---
       title: "{titulo}"
       authors: {autores if autores else []}
       tags: [{", ".join(t for t in [coleccion, serie, anio] if t)}]
       ---
       """)
       #Contenido de la ficha en MARKDOWN. Nota que quité la sangría porque estoy dentro del entorno con tres comillas, entonces no importa la indentación. Si esto no se hace así, la ficha no se genera correctamente.
       contenido = front_matter + dedent(f"""# {titulo}
<div class = "chips">{chips}</div>

<p align = "left"> <img src = {cover_file} width="500" height="600"></p>



## Resumen
{(resumen if resumen else "_Resumen próximamente._")}

## Ediciones disponibles
{seccion_ediciones}

## Metadatos
{metadatos}

## Descargas
{downs}

!!! info "Aviso"
    Documento con marca de agua para distribución **digital**.

## Cómo citar
> {(", ".join(autsnor) +". ") if autores else ""}{f"({anio}). " if anio else ""}*{titulo}*. {editorial}{(", " + str(edicion)) if edicion else ""}

<details>
<summary>BibTeX</summary>
<textarea id="myInput" rows="6" cols="80" class="verbatim">
@BOOK{{{_id}, 
title = {{{titulo}}}, 
author = {{{" and ".join(autbib) if autores else ""}}}, 
year = {{{anio}}}, 
publisher = {{{editorial}}}, 
address = {{México}}}}
</textarea>
<br>
<button style ="cursor:pointer; background-color: #ecf3ff; color: #448aff; padding: 3px 6px; border-radius: 6px; text-align: center" onclick="myFunction()">Copiar BibTeX</button>

<style>
  .verbatim {{
    font-family: monospace;
    white-space: pre;
  }}
</style>

<script>
function myFunction() {{
  const copyText = document.getElementById("myInput");
  copyText.select();
  navigator.clipboard.writeText(copyText.value);
  alert("¡Copiado!");
}}
</script>
</details>


[Volver al catálogo](../catalogo.md)

[Explorar](../explorar.md)
""")
       #Crear el archivo con los datos
       out_path = os.path.join(os.path.join(BASE,"docs","libros"), f"{_id}.md")
       with open(out_path, "w", encoding="utf-8") as fh:
              fh.write(contenido)

