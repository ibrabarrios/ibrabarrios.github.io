import requests

API = "https://spotify-backend-umber.vercel.app"

print("Spotify Analyzer")

def obtener_top_artistas():
    respuesta = requests.get(f"{API}/top-artists")
    datos = respuesta.json()
    return datos["items"]

artistas = obtener_top_artistas()
print(f"Tienes {len(artistas)} artistas en tu tpo")

for artista in artistas:
    print(artista["name"])

for i, artista in enumerate(artistas):
    genero = artista["genres"][0] if artista["genres"] else "desconocido"
    print(f"{i + 1}.{artista['name']} - {genero}")
    

todos_los_generos = []

for artista in artistas:
    for genero in artista["genres"]:
        todos_los_generos.append(genero)

generos_unicos = set(todos_los_generos)

print(f"\nEscuchas {len(generos_unicos)} géneros diferentes:")
for genero in generos_unicos:
    print(f"  - {genero}")

from collections import Counter

conteo = Counter(todos_los_generos)
genero_top = conteo.most_common(1)[0]

print(f"\nTu género más escuchado es: {genero_top[0]} ({genero_top[1]} artistas)")

