---
title: "Curso introductorio de álgebra II"
authors: [[['Diana'], ['Avella']], [['Gabriela'], ['Campero']], [['Edith', 'Corina'], ['Saenz', 'Valadez']]]
tags: [Papirhos, Textos]
---
# Curso introductorio de álgebra II
<div class = "chips"><span class ="chip"></span class ="icon">🏷</span> Textos</span> <span class ="chip"></span class ="icon">📚</span> Papirhos</span> <span class ="chip"></span class ="icon">ℹ️</span> Publicado</span></div>

<p align = "left"> <img src = "../../assets/covers/pap-tex-10.png" width="500" height="600"></p>



## Resumen
Resumen proximamente

## Ediciones disponibles

<div class="edition-selector" id="edition-selector-pap-tex-10">
    <div class="edition-buttons">
        <button type="button" class="edition-button active" data-target="edicion-pap-tex-10-0">Edición 1</button>
    </div>

    <div class="edition-content">
        <div id="edicion-pap-tex-10-0" class="edition-panel"><h3>Edición 1</h3><h4>Metadatos</h4>
<table>
    <tbody>
        <tr><th>Autores</th><td>Diana Avella, Gabriela Campero, Edith Corina Saenz Valadez</td></tr><tr><th>Colección</th><td>Papirhos</td></tr><tr><th>Serie</th><td>Textos</td></tr><tr><th>Tomo</th><td>2</td></tr><tr><th>Año</th><td>2020</td></tr><tr><th>Editorial</th><td>Instituto de Matemáticas, UNAM</td></tr><tr><th>Edición</th><td>1</td></tr><tr><th>ISBN (Colección)</th><td>978-607-02-5149-8</td></tr><tr><th>ISBN (Texto)</th><td>978-607-30-3681-8</td></tr>
    </tbody>
</table>
<h4 class="citation-title">Cómo citar</h4><div class="citation-box"><blockquote id="cita-ed-004">Diana Avella, Gabriela Campero, Edith Corina Saenz Valadez. (2020). <em>Curso introductorio de álgebra II</em>. Instituto de Matemáticas, UNAM. Edición 1.</blockquote><button type="button" class="citation-copy-button" data-target="cita-ed-004">Copiar cita</button></div><details><summary>BibTeX</summary><textarea id="bibtex-ed-004" rows="9" cols="80" class="verbatim">@BOOK{ed-004,
title = {Curso introductorio de álgebra II},
author = {Avella, Diana and Campero, Gabriela and Saenz, Edith},
year = {2020},
publisher = {Instituto de Matemáticas, UNAM},
edition = {1},
isbn = {978-607-30-3681-8},
address = {México}
}</textarea><br><button type="button" class="bibtex-copy-button" data-target="bibtex-ed-004">Copiar BibTeX</button></details></div>
    </div>
</div>

<script>
(() => {
    const selector = document.getElementById("edition-selector-pap-tex-10");

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

    const botonesBibtex = selector.querySelectorAll(".bibtex-copy-button");

    botonesBibtex.forEach((boton) => {
        boton.addEventListener("click", () => {
            const textarea = selector.querySelector(
                "#" + boton.dataset.target
            );

            if (!textarea) return;

            navigator.clipboard.writeText(textarea.value).then(() => {
              const textoOriginal = boton.textContent;

              boton.textContent = "Copiado";
              boton.classList.add("copied");

              setTimeout(() => {
                       boton.textContent = textoOriginal;
                       boton.classList.remove("copied");
              }, 1500);
            });
        });
    });
    const botonesCita = selector.querySelectorAll(".citation-copy-button");

    botonesCita.forEach((boton) => {
       boton.addEventListener("click", () => {
           const cita = selector.querySelector(
               "#" + boton.dataset.target
           );

           if (!cita) return;

           navigator.clipboard.writeText(cita.innerText).then(() => {
              const textoOriginal = boton.textContent;

              boton.textContent = "Copiado";
              boton.classList.add("copied");

              setTimeout(() => {
                 boton.textContent = textoOriginal;
                 boton.classList.remove("copied");
              }, 1500);
           });
       });
});
})();
</script>


## Descargas
<a class="md-button data-book-id=pap-tex-10 download-link" data-book-id="pap-tex-10" href = "pap-tex-10_mark.pdf" target = "_blank" rel ="noopener" > Abrir PDF </a>
<a class="md-button  data-book-id=pap-tex-10 download-link" data-book-id="pap-tex-10" href ="pap-tex-10_mark.pdf" download> Descargar</a>
<details>
<summary> Ver en línea (vista previa)</summary>
<object data = "pap-tex-10_mark.pdf" type="application/pdf" width="100%" height="700" >
<p> Tu navegador no puede mostrar PDF incrustado <a href="pap-tex-10_mark.pdf" target="_blank" rel ="noopener"> Abrir PDF </a> o usa el botón "Descargar".</p>
</object>
</details>

[Volver al catálogo](../catalogo.md)

[Explorar](../explorar.md)
