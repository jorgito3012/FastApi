# ⚡ Pokemon API & Web App

Una aplicación web moderna para gestionar una colección de Pokémon, construida con **FastAPI** y estilizada con CSS moderno.

## 🚀 Tecnologías

*   **Backend**: Python, FastAPI
*   **Base de Datos**: SQLModel (SQLite)
*   **Frontend**: HTML5, Jinja2 Templates, CSS3 (Variables, Flexbox/Grid)
*   **Diseño**: Interfaz "Premium" con diseño responsivo y animaciones.

## ✨ Características

*   **Listado de Pokémon**: Visualiza todos tus pokémon en una tabla estilizada.
*   **Detalle de Pokémon**: Tarjetas individuales con estadísticas visuales (Nivel, Ataque, Defensa).
*   **Gestión**: Formulario para registrar nuevos Pokémon en la base de datos.
*   **UI Moderna**:
    *   Barra de navegación responsiva.
    *   Paleta de colores moderna (Violeta/Indigo).
    *   Tipografía 'Outfit' de Google Fonts.
    *   Efectos Hover y micro-interacciones.

## 🛠️ Instalación y Uso

1.  **Clonar el repositorio** (o descargar los archivos).
2.  **Crear un entorno virtual**:
    ```bash
    python -m venv .venv
    # Windows
    .\.venv\Scripts\activate
    # Mac/Linux
    source .venv/bin/activate
    ```
3.  **Instalar dependencias**:
    ```bash
    pip install fastapi uvicorn sqlmodel jinja2 python-multipart
    ```
4.  **Ejecutar la aplicación**:
    El archivo principal se encuentra en `src/main.py`. Asegúrate de ejecutarlo desde la raíz del proyecto o ajustando el path.
    ```bash
    # Ejemplo desde la raíz
    python src/main.py
    ```
    O usando uvicorn directamente si se prefiere:
    ```bash
    uvicorn src.main:app --reload
    ```
5.  **Abrir en el navegador**:
    Visita `http://127.0.0.1:3000`

## 📂 Estructura del Proyecto

*   `src/main.py`: Punto de entrada de la aplicación.
*   `src/data/`: Configuración de base de datos y repositorios.
*   `src/models/`: Modelos de datos (SQLModel).
*   `src/routers/`: Rutas de la API.
*   `src/templates/`: Plantillas HTML (Jinja2).
*   `src/static/`: Archivos estáticos (CSS, Imágenes).

---
Autor: Jorge Narbona Gallego
