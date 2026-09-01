---
title: "Combinatoria"
authors: [[['Maria', 'Luisa'], ['Pérez', 'Seguí']]]
tags: [Cuadernos de olimpiadas de matemáticas]
---
# Combinatoria
<div class = "chips"><span class ="chip"></span class ="icon">📚</span> Cuadernos de olimpiadas de matemáticas</span> <span class ="chip"></span class ="icon">ℹ️</span> Publicado</span></div>

<p align = "left"> <img src = "../../assets/covers/cuad-x-1.png" width="500" height="600"></p>



## Resumen
Resumen 2

## Ediciones disponibles

<div class="edition-selector" id="edition-selector-cuad-x-1">
    <div class="edition-buttons">
        <button type="button" class="edition-button active" data-target="edicion-cuad-x-1-0">Edición 2</button>
    </div>

    <div class="edition-content">
        <div id="edicion-cuad-x-1-0" class="edition-panel"><h3>Edición 2</h3><h4>Metadatos</h4>
<table>
    <tbody>
        <tr><th>Autores</th><td>Maria Luisa Pérez Seguí</td></tr><tr><th>Colección</th><td>Cuadernos de olimpiadas de matemáticas</td></tr><tr><th>Año</th><td>2018</td></tr><tr><th>Editorial</th><td>Instituto de Matemáticas, UNAM</td></tr><tr><th>Edición</th><td>2</td></tr><tr><th>ISBN (Colección)</th><td>978-968-36-8599-5</td></tr><tr><th>ISBN (Texto)</th><td>978-607-02-85882</td></tr>
    </tbody>
</table>
<h4 class="citation-title">Cómo citar</h4><div class="citation-box"><blockquote id="cita-ed-002">Maria Luisa Pérez Seguí. (2018). <em>Combinatoria</em>. Instituto de Matemáticas, UNAM. Edición 2.</blockquote><button type="button" class="citation-copy-button" data-target="cita-ed-002">Copiar cita</button></div><details><summary>BibTeX</summary><textarea id="bibtex-ed-002" rows="9" cols="80" class="verbatim">@BOOK{ed-002,
title = {Combinatoria},
author = {Pérez, Maria},
year = {2018},
publisher = {Instituto de Matemáticas, UNAM},
edition = {2},
isbn = {978-607-02-85882},
address = {México}
}</textarea><br><button type="button" class="bibtex-copy-button" data-target="bibtex-ed-002">Copiar BibTeX</button></details></div>
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
<a class="md-button data-book-id=cuad-x-1 download-link" data-book-id="cuad-x-1" href = "cuad-x-1_mark.pdf" target = "_blank" rel ="noopener" > Abrir PDF </a>
<a class="md-button  data-book-id=cuad-x-1 download-link" data-book-id="cuad-x-1" href ="cuad-x-1_mark.pdf" download> Descargar</a>
<details>
<summary> Ver en línea (vista previa)</summary>
<object data = "cuad-x-1_mark.pdf" type="application/pdf" width="100%" height="700" >
<p> Tu navegador no puede mostrar PDF incrustado <a href="cuad-x-1_mark.pdf" target="_blank" rel ="noopener"> Abrir PDF </a> o usa el botón "Descargar".</p>
</object>
</details>

[Volver al catálogo](../catalogo.md)

[Explorar](../explorar.md)
