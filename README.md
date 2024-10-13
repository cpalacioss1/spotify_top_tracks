# Top Tracks de Spotify

## Descripción

Este proyecto permite obtener y mostrar las 10 canciones más escuchadas en Spotify de un año específico. La información se presenta en una interfaz gráfica amigable, incluyendo el título de la canción, el artista, el álbum y la popularidad.

## Características

- Busca las canciones más escuchadas por año.
- Interfaz gráfica utilizando Tkinter.
- Muestra los resultados en columnas con número correlativo.
- Permite limpiar el campo de entrada de año.

## Requisitos

- Python 3.x
- Bibliotecas: `spotipy`, `tkinter`, `python-dotenv`

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/spotify_top_tracks.git

2. Navega a la carpeta del proyecto:
    cd spotify_top_tracks

3. Crea un entorno virtual (opcional pero recomendado):
    python -m venv venv

4. Instala las dependencias:
    pip install spotipy python-dotenv

5. Crea un archivo .env en la raíz del proyecto y añade tus credenciales de Spotify:
    SPOTIFY_CLIENT_ID=tu_client_id
    SPOTIFY_CLIENT_SECRET=tu_client_secret

## Uso

1. Ejecuta el script principal:
    python spotify_top_tracks.py

2. Ingresa un año (YYYY) en el campo correspondiente y haz clic en "Obtener Canciones" para ver las canciones más escuchadas de ese año.

3. Puedes usar el botón "Limpiar año" para borrar el filtro y realizar una nueva búsqueda.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar o contribuir al proyecto, por favor abre un issue o envía un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT

