import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import tkinter as tk
from tkinter import messagebox, ttk

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

# Verificar que las variables de entorno se hayan cargado correctamente
if not client_id or not client_secret:
    raise ValueError("Las variables de entorno SPOTIFY_CLIENT_ID y SPOTIFY_CLIENT_SECRET deben estar configuradas en el archivo .env.")

# Inicializar Spotipy
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Función para obtener las canciones más escuchadas
def get_top_tracks():
    year = year_entry.get().strip()
    if not year.isdigit() or len(year) != 4:
        messagebox.showerror("Error", "Por favor, ingresa un año válido de 4 dígitos.")
        return
    
    try:
        # Obtén las canciones más escuchadas del año especificado
        results = sp.search(q=f'year:{year}', type='track', limit=10)
        top_tracks = results['tracks']['items']
        
        # Limpiar el árbol de canciones
        for i in tree.get_children():
            tree.delete(i)

        if not top_tracks:
            messagebox.showinfo("Información", f"No se encontraron canciones para el año {year}.")
            return
        
        # Mostrar los resultados en el árbol
        for index, track in enumerate(top_tracks, start=1):
            track_name = track['name']
            artist_name = ', '.join([artist['name'] for artist in track['artists']])
            album_name = track['album']['name']
            play_count = track['popularity']
            tree.insert("", "end", values=(index, track_name, artist_name, album_name, play_count))

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al obtener las canciones: {e}")

# Función para limpiar el campo de entrada del año
def clear_year():
    year_entry.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Top Tracks de Spotify")
root.geometry("600x400")

# Etiqueta y campo de entrada para el año
year_label = tk.Label(root, text="Ingresa el año (YYYY):")
year_label.pack(pady=10)

year_entry = tk.Entry(root)
year_entry.pack(pady=5)

# Botón para obtener las canciones
get_tracks_button = tk.Button(root, text="Obtener Canciones", command=get_top_tracks)
get_tracks_button.pack(pady=10)

# Botón para limpiar el campo de año
clear_button = tk.Button(root, text="Limpiar Año", command=clear_year)
clear_button.pack(pady=5)

# Crear el Treeview para mostrar los resultados
columns = ("#", "Título", "Artista", "Álbum", "Popularidad")
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading("#", text="#")
tree.heading("Título", text="Título")
tree.heading("Artista", text="Artista")
tree.heading("Álbum", text="Álbum")
tree.heading("Popularidad", text="Popularidad")

# Ajustar las columnas
tree.column("#", width=30, anchor='center')
tree.column("Título", width=200)
tree.column("Artista", width=150)
tree.column("Álbum", width=150)
tree.column("Popularidad", width=100)

tree.pack(pady=10, fill=tk.BOTH, expand=True)

# Ejecutar la aplicación
root.mainloop()
