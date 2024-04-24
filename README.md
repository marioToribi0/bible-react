<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Rag Intro" />

  &#xa0;

  <!-- <a href="https://ragintro.netlify.app">Demo</a> -->
</div>

<h1 align="center">Biblia RAG</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/mariotoribi0/bible_react?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/mariotoribi0/bible_react?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/mariotoribi0/bible_react?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/mariotoribi0/bible_react?color=56BEB8">

</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Rag Intro 🚀 Under construction...  🚧
</h4> 

<hr> -->

<br>

## :dart: Acerca del proyecto ##

Agente de la Biblia basado en IA generativa. Este agente es capaz de consultar la biblia a través de diferentes query. Con este conocimiento te da respuestas basadas en versículos, realiza citaciones y te coloca en la página de la lectura que te está explicando.

## :rocket: Tecnologías ##

Las siguientes herramientas fueron utilizadas en el proyecto:

- Python
- Langchain
- Streamlit

## :white_check_mark: Requerimientos ##

Antes de iniciar :checkered_flag:, tendrás que tener instalado [Git](https://git-scm.com) y [Docker](https://docs.docker.com/engine/install/ubuntu/).
Copia el siguiente contenido en un archivo `.env` en la raíz del proyecto, sustituyendo `<tu-valor>` con tus credenciales reales:
```bash
INDEX_NAME=<your-index-pinecone>
PINECONE_API_KEY=<your-pinecone-api-key>
OPENAI_API_KEY=<your-openai-api-key>
```
## :checkered_flag: Inicio ##

```bash
# Clone this project
$ git clone https://github.com/mariotoribi0/bible_react

# Access
$ cd bible_react

# Build image
$ docker build -t bible_react .

# Run the project
$ docker run -p 80:80 bible_react

# The server will initialize in the <http://localhost:3000>
```

## :memo: Licencia ##

Este proyecto está bajo una licencia del MIT. Para más detalles, leer [LICENSE](LICENSE.md).


Hecho con :heart: por <a href="https://github.com/mariotoribi0" target="_blank">Mario Toribio</a>

&#xa0;

<a href="#top">Volver a la parte superior</a>
