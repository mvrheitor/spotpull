import requests

def download_image(url, nome_arquivo):
    resposta = requests.get(url)

    if resposta.status_code == 200:
        with open(nome_arquivo, 'wb') as f:
            f.write(resposta.content)
        print("Imagem baixada com sucesso!")
    else:
        print("Falha ao baixar a imagem.")

def get_album_cover(client, album_id):
    album = client.album(album_id)
    cover_url = album['images'][0]['url']

    download_image(cover_url, 'capa_album.jpg')

def get_playlist_image(client, playlist_id):
    playlist = client.playlist(playlist_id)
    image_url = playlist['images'][0]['url']
    
    download_image(image_url, 'imagem_playlist.jpg')

def get_artist_image(client, artist_id):
    artist = client.artist(artist_id)
    image_url = artist['images'][0]['url']
    
    download_image(image_url, 'perfil_artista.jpg')

def get_user_image(client, user_id):
    user = client.user(user_id)
    image_url = user['images'][0]['url']
    
    download_image(image_url, 'perfil_usuário.jpg')