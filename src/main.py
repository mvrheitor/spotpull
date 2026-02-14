from src.config import get_client
import requests
from pytubefix import YouTube
from pytubefix import Search

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

def get_music(client, music_id):
    music = client.track(music_id)
    
    # monta a query para buscar no youtube
    query = music['name']
    for i in music['artists']:
        query += f' {i['name']}'

    # pega o primeiro resultado
    videos = Search(query).videos
    video_url = videos[1].watch_url

    # pega o vídeo e baixa somente o áudio
    yt = YouTube(video_url)
    ys = yt.streams.get_audio_only()
    print('Baixando:', yt.title)
    ys.download()

def display_menu():
    client = get_client()
    print('Escolha uma opção: ')
    print('[1] - Baixar capa de album')
    print('[2] - Baixar imagem de playlist')
    print('[3] - Baixar imagem de perfil de artista')
    print('[4] - Baixar imagem de perfil de usuário')
    print('[5] - Baixar música')
    escolha = int(input())
    if escolha == 1:
        album_url = input('Digite o link do álbum: ')
        album_id = album_url.split("/")[-1].split("?")[0]
        get_album_cover(client, album_id)
    if escolha == 2:
        playlist_url = input('Digite o link da playlist: ')
        playlist_id = playlist_url.split("/")[-1].split("?")[0]
        get_playlist_image(client, playlist_id)
    if escolha == 3:
        artist_url = input('Digite o link do perfil do artista: ')
        artist_id = artist_url.split("/")[-1].split("?")[0]
        get_artist_image(client, artist_id)
    if escolha == 4:
        user_url = input('Digite o link do perfil do usuário: ')
        user_id = user_url.split("/")[-1].split("?")[0]
        get_user_image(client, user_id)
    if escolha == 5:
        music_url = input('Digite o link da música: ')
        music_id = music_url.split("/")[-1].split("?")[0]
        get_music(client, music_id)