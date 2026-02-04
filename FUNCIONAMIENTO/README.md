# ⚡ Pokemon API & Web App

Una aplicación web moderna para gestionar una colección de Pokémon, construida con **FastAPI** y estilizada con CSS moderno.

## 🚀 Tecnologías

*   **Backend**: Python, FastAPI
*   **Base de Datos**: MySQL (manejada via Docker)
*   **Contenedorización**: Docker & Docker Compose
*   **Frontend**: HTML5, Jinja2 Templates, CSS3 (Variables, Flexbox/Grid)
*   **Diseño**: Interfaz "Premium" con diseño responsivo y animaciones.

## ✨ Características

*   **Listado de Pokémon**: Visualiza todos tus pokémon en una tabla estilizada.
*   **Detalle de Pokémon**: Tarjetas individuales con estadísticas visuales (Nivel, Ataque, Defensa).
*   **Gestión**: Formulario para registrar nuevos Pokémon en la base de datos MySQL.
*   **Entorno Dev**: Configuración lista para usar con Docker Compose.
*   **UI Moderna**:
    *   Barra de navegación responsiva.
    *   Paleta de colores moderna (Violeta/Indigo).
    *   Tipografía 'Outfit' de Google Fonts.
    *   Efectos Hover y micro-interacciones.

## 🛠️ Instalación y Uso (Docker)

La forma recomendada de ejecutar este proyecto es utilizando **Docker Desktop**.

1.  **Clonar el repositorio** (o descargar los archivos).
2.  **Asegurarse de tener Docker Desktop iniciado**.
3.  **Ejecutar la aplicación**:
    Abre una terminal en la carpeta `FastApi` (donde está el `docker-compose.yml`) y ejecuta:
    
    ```bash
    docker-compose up --build
    ```
5.  **Abrir en el navegador**:
    Visita `http://localhost:8000`

> **Nota**: La base de datos MySQL se crea e inicializa automáticamente dentro de su propio contenedor. No necesitas instalar nada extra en tu ordenador.

## 📂 Estructura del Proyecto

*   `Dockerfile` / `docker-compose.yml`: Configuración para despliegue en contenedores.
*   `src/main.py`: Punto de entrada de la aplicación.
*   `src/data/`: Configuración de base de datos y repositorios.
*   `src/models/`: Modelos de datos (SQLModel).
*   `src/routers/`: Rutas de la API.
*   `src/templates/`: Plantillas HTML (Jinja2).
*   `src/static/`: Archivos estáticos (CSS, Imágenes).

---
Autor: Jorge Narbona Gallego
