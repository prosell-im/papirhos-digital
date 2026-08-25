---
title: "Por la senda de los círculos"
authors: [[['Cecilia'], ['Neve', 'Jimenez']], [['Laura'], ['Rosales', 'Ortiz']]]
tags: [Papirhos, Mixbaal]
---
# Por la senda de los círculos
<div class = "chips"><span class ="chip"></span class ="icon">🏷</span> Mixbaal</span> <span class ="chip"></span class ="icon">📚</span> Papirhos</span> <span class ="chip"></span class ="icon">ℹ️</span> por recibir</span></div>

<p align = "left"> <img src = "../../assets/covers/pap-mix-1.jpg" width="500" height="600"></p>



## Resumen
Resumen proximamente

## Ediciones disponibles

<div class="edition-selector" id="edition-selector-pap-mix-1">
    <div class="edition-buttons">
        <button type="button" class="edition-button active" data-target="edicion-pap-mix-1-0">Edición sin especificar</button>
    </div>

    <div class="edition-content">
        <div id="edicion-pap-mix-1-0" class="edition-panel"><h3>Edición sin especificar</h3><h4>Metadatos</h4>
<table>
    <tbody>
        <tr><th>Autores</th><td>Cecilia Neve Jimenez, Laura Rosales Ortiz</td></tr><tr><th>Colección</th><td>Papirhos</td></tr><tr><th>Serie</th><td>Mixbaal</td></tr>
    </tbody>
</table>
<h4 class="citation-title">Cómo citar</h4><div class="citation-box"><blockquote id="cita-ed-007">Cecilia Neve Jimenez, Laura Rosales Ortiz. <em>Por la senda de los círculos</em>.</blockquote><button type="button" class="citation-copy-button" data-target="cita-ed-007">Copiar cita</button></div><details><summary>BibTeX</summary><textarea id="bibtex-ed-007" rows="9" cols="80" class="verbatim">@BOOK{ed-007,
title = {Por la senda de los círculos},
author = {Neve, Cecilia and Rosales, Laura},
address = {México}
}</textarea><br><button type="button" class="bibtex-copy-button" data-target="bibtex-ed-007">Copiar BibTeX</button></details></div>
    </div>
</div>

<script>
(() => {
    const selector = document.getElementById("edition-selector-pap-mix-1");

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
<a class="md-button data-book-id=pap-mix-1 download-link" data-book-id="pap-mix-1" href = "pap-mix-1_mark.pdf" target = "_blank" rel ="noopener" > Abrir PDF </a>
<a class="md-button  data-book-id=pap-mix-1 download-link" data-book-id="pap-mix-1" href ="pap-mix-1_mark.pdf" download> Descargar</a>
<details>
<summary> Ver en línea (vista previa)</summary>
<object data = "pap-mix-1_mark.pdf" type="application/pdf" width="100%" height="700" >
<p> Tu navegador no puede mostrar PDF incrustado <a href="pap-mix-1_mark.pdf" target="_blank" rel ="noopener"> Abrir PDF </a> o usa el botón "Descargar".</p>
</object>
</details>

!!! info "Aviso"
    Documento con marca de agua para distribución **digital**.

[Volver al catálogo](../catalogo.md)

[Explorar](../explorar.md)
