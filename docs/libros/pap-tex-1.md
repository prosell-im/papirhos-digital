---
title: "Grupos I"
authors: [[['Diana'], ['Avella']], [['Octavio'], ['Mendoza']], [['Edith', 'Corina'], ['Saenz', 'Valadez']], [['María', 'José'], ['Souto']]]
tags: [Papirhos, Textos, 2014]
---
# Grupos I
<div class = "chips"><span class ="chip"></span class ="icon">🏷</span> Textos</span> <span class ="chip"></span class ="icon">📚</span> Papirhos</span> <span class ="chip"></span class ="icon">🗓</span> 2014</span> <span class ="chip"></span class ="icon">ℹ️</span> Publicado</span></div>

<p align = "left"> <img src = "../../assets/covers/pap-tex-1.png" width="500" height="600"></p>



## Resumen
Resumen 5

## Ediciones disponibles

<div class="edition-selector" id="edition-selector-pap-tex-1">
    <div class="edition-buttons">
        <button type="button" class="edition-button active" data-target="edicion-pap-tex-1-0">Edición 3</button>
    </div>

    <div class="edition-content">
        <div id="edicion-pap-tex-1-0" class="edition-panel"><h3>Edición 3</h3><ul><li><strong>Año:</strong> 2014</li><li><strong>Editorial:</strong> Instituto de Matemáticas, UNAM</li><li><strong>ISBN:</strong> 978-607-02-9435-8</li></ul></div>
    </div>
</div>

<script>
(() => {
    const selector = document.getElementById("edition-selector-pap-tex-1");

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
| Autores | Diana Avella, Octavio Mendoza, Edith Corina Saenz Valadez, María José Souto |
| Colección | Papirhos |
| Serie | Textos |
| Tomo | 1 |
| Año | 2014 |
| Editorial | Instituto de Matemáticas, UNAM |
| Edición | 3 |
| ISBN (Colección) | 978-607-02-9375-7 |
| ISBN (Texto) | 978-607-02-9435-8 |

## Descargas
<a class="md-button data-book-id=pap-tex-1 download-link" data-book-id="pap-tex-1" href = "pap-tex-1_mark.pdf" target = "_blank" rel ="noopener" > Abrir PDF </a>
<a class="md-button  data-book-id=pap-tex-1 download-link" data-book-id="pap-tex-1" href ="pap-tex-1_mark.pdf" download> Descargar</a>
<details>
<summary> Ver en línea (vista previa)</summary>
<object data = "pap-tex-1_mark.pdf" type="application/pdf" width="100%" height="700" >
<p> Tu navegador no puede mostrar PDF incrustado <a href="pap-tex-1_mark.pdf" target="_blank" rel ="noopener"> Abrir PDF </a> o usa el botón "Descargar".</p>
</object>
</details>

!!! info "Aviso"
    Documento con marca de agua para distribución **digital**.

## Cómo citar
> Diana Avella, Octavio Mendoza, Edith Corina Saenz Valadez, María José Souto. (2014). *Grupos I*. Instituto de Matemáticas, UNAM, 3

<details>
<summary>BibTeX</summary>
<textarea id="myInput" rows="6" cols="80" class="verbatim">
@BOOK{pap-tex-1, 
title = {Grupos I}, 
author = {Avella, Diana and Mendoza, Octavio and Saenz, Edith and Souto, María}, 
year = {2014}, 
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
