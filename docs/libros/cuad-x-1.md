---
title: "Combinatoria"
authors: [[['Maria', 'Luisa'], ['Pérez', 'Seguí']]]
tags: [Cuadernos de olimpiadas de matemáticas, 2018]
---
# Combinatoria
<div class = "chips"><span class ="chip"></span class ="icon">📚</span> Cuadernos de olimpiadas de matemáticas</span> <span class ="chip"></span class ="icon">🗓</span> 2018</span> <span class ="chip"></span class ="icon">ℹ️</span> Publicado</span></div>

<p align = "left"> <img src = "../../assets/covers/cuad-x-1.png" width="500" height="600"></p>



## Resumen
Resumen 2

## Ediciones disponibles

<div class="edition-selector" id="edition-selector-cuad-x-1">
    <div class="edition-buttons">
        <button type="button" class="edition-button active" data-target="edicion-cuad-x-1-0">Edición 2</button>
    </div>

    <div class="edition-content">
        <div id="edicion-cuad-x-1-0" class="edition-panel"><h3>Edición 2</h3><ul><li><strong>Año:</strong> 2018</li><li><strong>Editorial:</strong> Instituto de Matemáticas, UNAM</li><li><strong>ISBN:</strong> 978-607-02-85882</li></ul></div>
    </div>
</div>

<script>
(() => {
    const selector = document.getElementById("edition-selector-cuad-x-1");

    if (!selector) return;

    const botones = selector.querySelectorAll(".edition-button");
    const paneles = selector.querySelectorAll(".edition-panel");

    botones.forEach((boton) => {
        boton.addEventListener("click", () => {
            botones.forEach((b) => b.classList.remove("active"));
            paneles.forEach((panel) => panel.hidden = true);

            boton.classList.add("active");

            const panelActivo = selector.querySelector(
                "#" + boton.dataset.target
            );

            if (panelActivo) {
                panelActivo.hidden = false;
            }
        });
    });
})();
</script>


## Metadatos
|  |  |
|---|---|
| Autores | Maria Luisa Pérez Seguí |
| Colección | Cuadernos de olimpiadas de matemáticas |
| Año | 2018 |
| Editorial | Instituto de Matemáticas, UNAM |
| Edición | 2 |
| ISBN (Colección) | 978-968-36-8599-5 |
| ISBN (Texto) | 978-607-02-85882 |

## Descargas
<a class="md-button data-book-id=cuad-x-1 download-link" data-book-id="cuad-x-1" href = "cuad-x-1_mark.pdf" target = "_blank" rel ="noopener" > Abrir PDF </a>
<a class="md-button  data-book-id=cuad-x-1 download-link" data-book-id="cuad-x-1" href ="cuad-x-1_mark.pdf" download> Descargar</a>
<details>
<summary> Ver en línea (vista previa)</summary>
<object data = "cuad-x-1_mark.pdf" type="application/pdf" width="100%" height="700" >
<p> Tu navegador no puede mostrar PDF incrustado <a href="cuad-x-1_mark.pdf" target="_blank" rel ="noopener"> Abrir PDF </a> o usa el botón "Descargar".</p>
</object>
</details>

!!! info "Aviso"
    Documento con marca de agua para distribución **digital**.

## Cómo citar
> Maria Luisa Pérez Seguí. (2018). *Combinatoria*. Instituto de Matemáticas, UNAM, 2

<details>
<summary>BibTeX</summary>
<textarea id="myInput" rows="6" cols="80" class="verbatim">
@BOOK{cuad-x-1, 
title = {Combinatoria}, 
author = {Pérez, Maria}, 
year = {2018}, 
publisher = {Instituto de Matemáticas, UNAM}, 
address = {México}}
</textarea>
<br>
<button style ="cursor:pointer; background-color: #ecf3ff; color: #448aff; padding: 3px 6px; border-radius: 6px; text-align: center" onclick="myFunction()">Copiar BibTeX</button>

<style>
  .verbatim {
    font-family: monospace;
    white-space: pre;
  }
</style>

<script>
function myFunction() {
  const copyText = document.getElementById("myInput");
  copyText.select();
  navigator.clipboard.writeText(copyText.value);
  alert("¡Copiado!");
}
</script>
</details>


[Volver al catálogo](../catalogo.md)

[Explorar](../explorar.md)
