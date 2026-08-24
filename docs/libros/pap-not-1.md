---
title: "Teoría de singularidades en topología, geometría y foliaciones I"
authors: [[['Jean-Paul'], ['Brasselet']], [['Felipe'], ['Cano']], [['Dominique'], ['Cerveau']], [['Dung', 'Tráng'], ['Lê']], [['Frank'], ['Loray']], [['Mutsuo'], ['Oka']], [['José'], ['Seade']], [['Mark'], ['Spivakovsky']]]
tags: [Papirhos, Notas, 2017]
---
# Teoría de singularidades en topología, geometría y foliaciones I
<div class = "chips"><span class ="chip"></span class ="icon">🏷</span> Notas</span> <span class ="chip"></span class ="icon">📚</span> Papirhos</span> <span class ="chip"></span class ="icon">🗓</span> 2017</span> <span class ="chip"></span class ="icon">ℹ️</span> Publicado</span></div>

<p align = "left"> <img src = "../../assets/covers/pap-not-1.jpg" width="500" height="600"></p>



## Resumen
Resumen proximamente

## Ediciones disponibles

<div class="edition-selector" id="edition-selector-pap-not-1">
    <div class="edition-buttons">
        <button type="button" class="edition-button active" data-target="edicion-pap-not-1-0">Edición 2</button><button type="button" class="edition-button" data-target="edicion-pap-not-1-1">Edición 1</button>
    </div>

    <div class="edition-content">
        <div id="edicion-pap-not-1-0" class="edition-panel"><h3>Edición 2</h3><ul><li><strong>Año:</strong> 2017</li><li><strong>Editorial:</strong> Instituto de Matemáticas, UNAM</li><li><strong>ISBN:</strong> 978-607-02-9845-test</li></ul></div><div id="edicion-pap-not-1-1" class="edition-panel" hidden><h3>Edición 1</h3><ul><li><strong>Año:</strong> 2017</li><li><strong>Editorial:</strong> Instituto de Matemáticas, UNAM</li><li><strong>ISBN:</strong> 978-607-02-9845-5</li></ul></div>
    </div>
</div>

<script>
(() => {
    const selector = document.getElementById("edition-selector-pap-not-1");

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
| Autores | Jean-Paul Brasselet, Felipe Cano, Dominique Cerveau, Dung Tráng Lê, Frank Loray, Mutsuo Oka, José Seade, Mark Spivakovsky |
| Colección | Papirhos |
| Serie | Notas |
| Año | 2017 |
| Editorial | Instituto de Matemáticas, UNAM |
| Edición | 1 |
| ISBN (Colección) | 978-607-02-5149-8 |
| ISBN (Texto) | 978-607-02-9845-5 |

## Descargas
<a class="md-button data-book-id=pap-not-1 download-link" data-book-id="pap-not-1" href = "pap-not-1_mark.pdf" target = "_blank" rel ="noopener" > Abrir PDF </a>
<a class="md-button  data-book-id=pap-not-1 download-link" data-book-id="pap-not-1" href ="pap-not-1_mark.pdf" download> Descargar</a>
<details>
<summary> Ver en línea (vista previa)</summary>
<object data = "pap-not-1_mark.pdf" type="application/pdf" width="100%" height="700" >
<p> Tu navegador no puede mostrar PDF incrustado <a href="pap-not-1_mark.pdf" target="_blank" rel ="noopener"> Abrir PDF </a> o usa el botón "Descargar".</p>
</object>
</details>

!!! info "Aviso"
    Documento con marca de agua para distribución **digital**.

## Cómo citar
> Jean-Paul Brasselet, Felipe Cano, Dominique Cerveau, Dung Tráng Lê, Frank Loray, Mutsuo Oka, José Seade, Mark Spivakovsky. (2017). *Teoría de singularidades en topología, geometría y foliaciones I*. Instituto de Matemáticas, UNAM, 1

<details>
<summary>BibTeX</summary>
<textarea id="myInput" rows="6" cols="80" class="verbatim">
@BOOK{pap-not-1, 
title = {Teoría de singularidades en topología, geometría y foliaciones I}, 
author = {Brasselet, Jean-Paul and Cano, Felipe and Cerveau, Dominique and Lê, Dung and Loray, Frank and Oka, Mutsuo and Seade, José and Spivakovsky, Mark}, 
year = {2017}, 
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
