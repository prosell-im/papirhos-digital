---
title: "Grupos II"
authors: [[['Diana'], ['Avella']], [['Octavio'], ['Mendoza']], [['Edith', 'Corina'], ['Saenz', 'Valadez']], [['María', 'José'], ['Souto']]]
tags: [Papirhos, Textos]
---
# Grupos II
<div class = "chips"><span class ="chip"></span class ="icon">🏷</span> Textos</span> <span class ="chip"></span class ="icon">📚</span> Papirhos</span> <span class ="chip"></span class ="icon">ℹ️</span> Publicado</span></div>

<p align = "left"> <img src = "../../assets/covers/pap-tex-4.jpg" width="500" height="600"></p>



## Resumen
Resuemn 6

## Ediciones disponibles

<div class="edition-selector" id="edition-selector-pap-tex-4">
    <div class="edition-buttons">
        <button type="button" class="edition-button active" data-target="edicion-pap-tex-4-0">Edición 1</button>
    </div>

    <div class="edition-content">
        <div id="edicion-pap-tex-4-0" class="edition-panel"><h3>Edición 1</h3><h4>Metadatos</h4>
<table>
    <tbody>
        <tr><th>Autores</th><td>Diana Avella, Octavio Mendoza, Edith Corina Saenz Valadez, María José Souto</td></tr><tr><th>Colección</th><td>Papirhos</td></tr><tr><th>Serie</th><td>Textos</td></tr><tr><th>Tomo</th><td>2</td></tr><tr><th>Año</th><td>2016</td></tr><tr><th>Editorial</th><td>Instituto de Matemáticas, UNAM</td></tr><tr><th>Edición</th><td>1</td></tr><tr><th>ISBN (Colección)</th><td>978-607-02-5149-8</td></tr><tr><th>ISBN (Texto)</th><td>978-607-02-7814-3</td></tr>
    </tbody>
</table>
<h4 class="citation-title">Cómo citar</h4><div class="citation-box"><blockquote id="cita-ed-006">Diana Avella, Octavio Mendoza, Edith Corina Saenz Valadez, María José Souto. (2016). <em>Grupos II</em>. Instituto de Matemáticas, UNAM. Edición 1.</blockquote><button type="button" class="citation-copy-button" data-target="cita-ed-006">Copiar cita</button></div><details><summary>BibTeX</summary><textarea id="bibtex-ed-006" rows="9" cols="80" class="verbatim">@BOOK{ed-006,
title = {Grupos II},
author = {Avella, Diana and Mendoza, Octavio and Saenz, Edith and Souto, María},
year = {2016},
publisher = {Instituto de Matemáticas, UNAM},
edition = {1},
isbn = {978-607-02-7814-3},
address = {México}
}</textarea><br><button type="button" class="bibtex-copy-button" data-target="bibtex-ed-006">Copiar BibTeX</button></details></div>
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

[Volver al catálogo](../catalogo.md)

[Explorar](../explorar.md)
