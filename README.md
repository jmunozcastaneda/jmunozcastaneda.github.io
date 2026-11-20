# Web académica — Jose M. Muñoz-Castañeda

Proyecto Quarto para `https://jmunozcastaneda.github.io`.

## ANTES DE PUBLICAR

- Revisa los textos biográficos, docencia, cargos y números de proyectos contra tu CVA actualizado. **Esta versión incluye correcciones preliminares, pero no equivale a una auditoría biográfica completa.**
- Comprueba los metadatos bibliográficos de cada artículo. La Letter de PLB se indica como *online* con identificador 141137; no se inventa volumen de revista.
- La fotografía `images/photo.jpg` se ha recortado exclusivamente a partir de la fotografía original que facilitaste, sin modificar facialmente el retrato.
- Lee `COPYRIGHT.md` y `copyright.qmd`. No subas apuntes, PDF científicos ni notebooks de Mathematica sin decidir antes su régimen de derechos.
- Esta versión (v9) se ha compilado con Quarto 1.7 y revisado en escritorio y en móvil.

## Diseño (v9)

La web se presenta como un artículo científico: la portada tiene *Keywords*, las secciones van numeradas y los trabajos destacados se citan como referencias [1]–[4]. Las páginas interiores numeran sus secciones (`number-sections: true` en la cabecera de cada `.qmd`).

- **Tipografía:** Spectral para títulos, IBM Plex Sans para el texto y STIX Two Text para las letras griegas.
- **Color:** azul marino «vacío» (`$vacuum`) para la cabecera y el bloque final, papel crema para el resto, y los dos polos del mapa de Casimir (azul `$cold`, atracción; naranja `$warm`, repulsión) como acentos.
- **Portada:** el retrato delante del mapa de Casimir, que hace de fondo sin rótulos ni pie de figura.
- **El mapa de la portada y la Fig. 1 de Research** son datos calculados, no ilustraciones: la energía de Casimir entre dos placas sobre el rombo de condiciones de contorno consistentes U(α, β, n), a partir de la función espectral (2.20) de Asorey & Muñoz-Castañeda, *Nucl. Phys. B* 874 (2013). La portada muestra el corte n₁ = 0 y Research cuatro cortes. `tools/casimir_core.py` contiene el cálculo y se comprueba contra los casos exactos (Dirichlet, Neumann, periódico, antiperiódico, cuasiperiódico (3.21) y Dirichlet–Neumann) ejecutando `python tools/casimir_core.py`. `tools/casimir_map.py` regenera las dos imágenes.

## Blog

El blog está preparado pero **oculto**: no aparece en el menú ni se publica su página hasta que lo actives.

**Escribir una entrada.** Copia la carpeta `posts/_plantilla-entrada` dentro de `posts/` y quítale el guion bajo inicial, por ejemplo `posts/2026-12-casimir-pistons/`. Edita el `index.qmd` de dentro: título, descripción, fecha, categorías y texto. Admite ecuaciones LaTeX, figuras, código y enlaces. Las imágenes de cada entrada van en su misma carpeta. Mientras la línea `draft: true` siga en la cabecera, la entrada no se publica; cuando esté lista, bórrala y haz *Commit* y *Push*.

**Activar el blog** (cuando tengas la primera entrada), en `_quarto.yml`:

1. Borra la línea `- "!blog.qmd"`.
2. Quita el `#` de las dos líneas de `Blog` en el menú.

La página `blog.qmd` lista las entradas de la más reciente a la más antigua, permite filtrar por categorías y genera un canal RSS (`blog.xml`). El aspecto de la lista está en `blog.ejs`, y los ajustes comunes de las entradas en `posts/_metadata.yml`.

## Subirlo a GitHub

Puedes usar [GitHub Desktop](https://desktop.github.com/) para trabajar con el repositorio `jmunozcastaneda/jmunozcastaneda.github.io`, incluso si ya contiene un README:

1. Clona el repositorio con GitHub Desktop, si todavía no lo tienes clonado.
2. Copia **los archivos interiores de esta carpeta**, incluida la subcarpeta oculta `.github`, dentro de la carpeta local del repositorio.
3. En GitHub Desktop revisa los cambios, haz un commit y pulsa *Push origin*.
4. En el repositorio de GitHub abre *Settings → Pages*, y en *Build and deployment → Source* selecciona **GitHub Actions**.
5. Comprueba que la acción **Publish website** finaliza en verde y visita `https://jmunozcastaneda.github.io`.

Si la compilación falla, conserva el mensaje de error de la pestaña *Actions* para corregir la configuración antes de publicar.

## Archivos principales

- `_quarto.yml`: navegación, metadatos y configuración general.
- `index.qmd`: portada y selección de artículos.
- `research.qmd`: investigación, colaboraciones, charlas y reuniones.
- `publications.yml`: base de datos de la selección de artículos.
- `publications.ejs`: plantilla de las publicaciones.
- `publications.qmd`: página de publicaciones.
- `teaching.qmd`: docencia, supervisión y enlaces a recursos sujetos a licencia.
- `collaborations.qmd`: colaboradores y redes científicas.
- `mathematica.qmd`: catálogo de notebooks, sin distribuir código de investigación.
- `outreach.qmd`: divulgación para públicos no especializados.
- `academic-cv.qmd`: visión de méritos, liderazgo y servicio universitario.
- `contact.qmd`: contacto y perfiles.
- `copyright.qmd`, `COPYRIGHT.md`: política de derechos.
- `images/`: foto, figuras calculadas (`casimir-map.png`, `casimir-slices.png`) y favicon.
- `styles/theme.scss`: estilo de la web.
- `tools/`: scripts que generan las figuras de Casimir (no se publican).
- `.github/workflows/publish.yml`: compilación y publicación automáticas con GitHub Actions.

Para previsualizar en un ordenador con [Quarto](https://quarto.org) instalado, ejecuta `quarto preview` dentro de la carpeta.

## Navegación y privacidad

Los accesos Publications, Teaching, Collaborators, Mathematica y Outreach están junto al botón **Explore research** de la portada. La navegación superior contiene Home, Research, Publications, Academic CV y Contact, para evitar sobrecargar la cabecera. Copyright & Licensing permanece en el pie de página. Se han creado páginas iniciales sin incorporar PDF ni notebooks protegidos.

La información de méritos y colaboradores se ha trasladado o derivado de la versión de trabajo; **requiere validación antes de publicar**, particularmente periodos de cargos, afiliaciones, cifras y documentación acreditativa. No se han incluido planes de investigación confidenciales.

## Pendiente de verificar por el autor

- Confirmación de trayectoria, cargos, charlas, tesis y datos bibliográficos antes de la primera publicación.
- Completar la lista de publicaciones (actualmente solo una selección).
- Añadir asignaturas actuales en la página de docencia.
- Añadir perfiles web adicionales cuando estén disponibles.
- Decidir por separado la licencia de cada PDF o notebook antes de hacerlo público.

## Archivos reservados

Git no equivale a una barrera de privacidad. Los PDF y archivos Wolfram están excluidos por defecto mediante .gitignore para disminuir errores al hacer commits, pero deben mantenerse fuera de todo repositorio público hasta decidir expresamente su publicación y la licencia aplicable. Para publicar un archivo aprobado se podrá añadir explícitamente.
