---
title: "Curso breve de geometría proyectiva"
authors: [[['Felipe'], ['Cano']], [['Beatriz'], ['Molina-Samper']], [['Fernando'], ['Sanz']]]
tags: [Papirhos, Textos]
---
# Curso breve de geometría proyectiva
<div class = "chips"><span class ="chip"></span class ="icon">🏷</span> Textos</span> <span class ="chip"></span class ="icon">📚</span> Papirhos</span> <span class ="chip"></span class ="icon">ℹ️</span> Físico</span></div>

<p align = "left"> <img src = "../../assets/covers/pap-tex-11.png" width="500" height="600"></p>



## Resumen
Resumen proximamente

## Ediciones disponibles

<div class="edition-selector" id="edition-selector-pap-tex-11">
    <div class="edition-buttons">
        <button type="button" class="edition-button active" data-target="edicion-pap-tex-11-0">Edición sin especificar</button>
    </div>

    <div class="edition-content">
        <div id="edicion-pap-tex-11-0" class="edition-panel"><h3>Edición sin especificar</h3><ul><li><strong>Editorial:</strong> Instituto de Matemáticas, UNAM</li></ul></div>
    </div>
</div>

<script>
(() => {
    const selector = document.getElementById("edition-selector-pap-tex-11");

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
| Autores | Felipe Cano, Beatriz Molina-Samper, Fernando Sanz |
| Colección | Papirhos |
| Serie | Textos |
| Editorial | Instituto de Matemáticas, UNAM |
| ISBN (Colección) | 000 |

## Descargas
<a class="md-button data-book-id=pap-tex-11 download-link" data-book-id="pap-tex-11" href = "pap-tex-11_mark.pdf" target = "_blank" rel ="noopener" > Abrir PDF </a>
<a class="md-button  data-book-id=pap-tex-11 download-link" data-book-id="pap-tex-11" href ="pap-tex-11_mark.pdf" download> Descargar</a>
<details>
<summary> Ver en línea (vista previa)</summary>
<object data = "pap-tex-11_mark.pdf" type="application/pdf" width="100%" height="700" >
<p> Tu navegador no puede mostrar PDF incrustado <a href="pap-tex-11_mark.pdf" target="_blank" rel ="noopener"> Abrir PDF </a> o usa el botón "Descargar".</p>
</object>
</details>

!!! info "Aviso"
    Documento con marca de agua para distribución **digital**.

## Cómo citar
> Felipe Cano, Beatriz Molina-Samper, Fernando Sanz. *Curso breve de geometría proyectiva*. Instituto de Matemáticas, UNAM

<details>
<summary>BibTeX</summary>
<textarea id="myInput" rows="6" cols="80" class="verbatim">
@BOOK{pap-tex-11, 
title = {Curso breve de geometría proyectiva}, 
author = {Cano, Felipe and Molina-Samper, Beatriz and Sanz, Fernando}, 
year = {}, 
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
