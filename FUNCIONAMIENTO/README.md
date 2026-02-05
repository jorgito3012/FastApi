# ⚡ Pokemon API & Web App

Una aplicación web moderna para gestionar una colección de Pokémon, construida con **FastAPI** y estilizada con CSS moderno.

## 🚀 Tecnologías

*   **Backend**: Python, FastAPI
*   **Base de Datos**: PostgreSQL (manejada via Docker)
*   **Driver BD**: `psycopg2-binary` (Elegido por ser el estándar más robusto y fácil de implementar en entornos Docker/Dev sin compilación compleja).
*   **Contenedorización**: Docker & Docker Compose
*   **Frontend**: HTML5, Jinja2 Templates, CSS3 (Variables, Flexbox/Grid)
*   **Diseño**: Interfaz "Premium" con diseño responsivo y animaciones.

## ✨ Características

*   **Listado de Pokémon**: Visualiza todos tus pokémon en una tabla estilizada.
*   **Detalle de Pokémon**: Tarjetas individuales con estadísticas visuales (Nivel, Ataque, Defensa).
*   **Gestión**: Formulario para registrar nuevos Pokémon en la base de datos PostgreSQL.
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
4.  **Abrir en el navegador**:
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

## 🔄 Cambios Recientes: Migración a PostgreSQL

Recientemente se migró la base de datos de MySQL a **PostgreSQL** para aprovechar su mayor robustez y compatibilidad con entornos de producción modernos.

### ¿Por qué `psycopg2-binary`?
Para conectar Python con PostgreSQL, hemos elegido el driver **`psycopg2-binary`** en lugar de otras opciones (como `asyncpg` o `psycopg2` puro) por las siguientes razones:
1.  **Facilidad de instalación**: Es una versión pre-compilada que incluye todas las librerías necesarias. Esto evita errores comunes de compilación en Docker (falta de `gcc`, `libpq-dev`, etc.) y acelera el tiempo de construcción del contenedor.
2.  **Estabilidad**: Es el driver más maduro y ampliamente probado en el ecosistema Python.
3.  **Compatibilidad**: Funciona perfectamente con `SQLModel` y `SQLAlchemy` sin configuraciones exóticas.

---
Autor: Jorge Narbona Gallego

## ☁️ Despliegue en Render

Este proyecto está configurado para desplegarse fácilmente en **Render** utilizando Docker. Sigue estos pasos:

### 1. Crear la Base de Datos (PostgreSQL)
El primer paso es crear el servicio de base de datos donde se almacenarán los pokémon.

1. Entra en tu dashboard de [Render](https://dashboard.render.com/).
2. Haz clic en **New +** y selecciona **PostgreSQL**.
3. Dale un nombre (ej. `fastapi-db`) y configura el resto de opciones (la capa gratuita es suficiente).
4. Una vez creada, espera a que esté disponible y busca la sección **Internal Database URL**.
5. Copia esa URL completa.
   - Tendrá un formato similar a: `postgres://usuario:password@hostname:5432/basedatos`

### 2. Crear el Servicio Web (Docker)
Ahora desplegaremos la aplicación FastAPI utilizando la imagen de Docker.

1. En el dashboard, haz clic en **New +** y selecciona **Web Service**.
2. Conecta tu repositorio de GitHub donde tienes este código.
3. Elige un nombre para tu servicio.
4. En **Runtime** (Entorno), selecciona **Docker**.
5. Render detectará automáticamente el `Dockerfile` en la raíz de tu repositorio.
6. Desplázate hasta la sección **Environment Variables** y añade la siguiente variable:
   - **Key**: `DB_URL`
   - **Value**: *Pega la "Internal Database URL" que copiaste en el paso anterior*.
7. Haz clic en **Create Web Service**.

Render comenzará a construir la imagen de Docker baseda en tu `Dockerfile`. Una vez finalizado el despliegue, tu aplicación estará online. Gracias al evento `lifespan` definido en `main.py`, la base de datos se inicializará automáticamente con las tablas y datos de prueba la primera vez que arranque.
