---
title: "Grupos II"
authors: [[['Diana'], ['Avella']], [['Octavio'], ['Mendoza']], [['Edith', 'Corina'], ['Saenz', 'Valadez']], [['María', 'José'], ['Souto']]]
tags: [Papirhos, Textos, 2016]
---
# Grupos II
<div class = "chips"><span class ="chip"></span class ="icon">🏷</span> Textos</span> <span class ="chip"></span class ="icon">📚</span> Papirhos</span> <span class ="chip"></span class ="icon">🗓</span> 2016</span> <span class ="chip"></span class ="icon">ℹ️</span> Publicado</span></div>

<p align = "left"> <img src = "../../assets/covers/pap-tex-4.jpg" width="500" height="600"></p>



## Resumen
Resuemn 6

## Ediciones disponibles

<div class="edition-selector" id="edition-selector-pap-tex-4">
    <div class="edition-buttons">
        <button type="button" class="edition-button active" data-target="edicion-pap-tex-4-0">Edición 1</button>
    </div>

    <div class="edition-content">
        <div id="edicion-pap-tex-4-0" class="edition-panel"><h3>Edición 1</h3><ul><li><strong>Año:</strong> 2016</li><li><strong>Editorial:</strong> Instituto de Matemáticas, UNAM</li><li><strong>ISBN:</strong> 978-607-02-7814-3</li></ul></div>
    </div>
</div>

<script>
(() => {
    const selector = document.getElementById("edition-selector-pap-tex-4");

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
| Tomo | 2 |
| Año | 2016 |
| Editorial | Instituto de Matemáticas, UNAM |
| Edición | 1 |
| ISBN (Colección) | 978-607-02-5149-8 |
| ISBN (Texto) | 978-607-02-7814-3 |

## Descargas
<a class="md-button data-book-id=pap-tex-4 download-link" data-book-id="pap-tex-4" href = "pap-tex-4_mark.pdf" target = "_blank" rel ="noopener" > Abrir PDF </a>
<a class="md-button  data-book-id=pap-tex-4 download-link" data-book-id="pap-tex-4" href ="pap-tex-4_mark.pdf" download> Descargar</a>
<details>
<summary> Ver en línea (vista previa)</summary>
<object data = "pap-tex-4_mark.pdf" type="application/pdf" width="100%" height="700" >
<p> Tu navegador no puede mostrar PDF incrustado <a href="pap-tex-4_mark.pdf" target="_blank" rel ="noopener"> Abrir PDF </a> o usa el botón "Descargar".</p>
</object>
</details>

!!! info "Aviso"
    Documento con marca de agua para distribución **digital**.

## Cómo citar
> Diana Avella, Octavio Mendoza, Edith Corina Saenz Valadez, María José Souto. (2016). *Grupos II*. Instituto de Matemáticas, UNAM, 1

<details>
<summary>BibTeX</summary>
<textarea id="myInput" rows="6" cols="80" class="verbatim">
@BOOK{pap-tex-4, 
title = {Grupos II}, 
author = {Avella, Diana and Mendoza, Octavio and Saenz, Edith and Souto, María}, 
year = {2016}, 
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
