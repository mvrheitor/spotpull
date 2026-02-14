from src.config import get_client
from src.get_images import get_album_cover, get_artist_image, get_playlist_image, get_user_image
from src.youtube_scripts import search_video, download_video_audio

def get_music(client, music_id, path=None):
    music = client.track(music_id)
    
    # monta a query para buscar no youtube
    query = music['name']
    for i in music['artists']:
        query += f' {i['name']}'

    video_url = search_video(query)
    download_video_audio(video_url, path)

def get_playlist_musics(client, playlist_id, path='./Musics/'):
    playlist = client.playlist_tracks(playlist_id)
    for i in playlist['items']:
        get_music(client, i['track']['id'], path)

def display_menu():
    client = get_client()
    print('Escolha uma opção: ')
    print('[1] - Baixar capa de album')
    print('[2] - Baixar imagem de playlist')
    print('[3] - Baixar imagem de perfil de artista')
    print('[4] - Baixar imagem de perfil de usuário')
    print('[5] - Baixar música')
    print('[6] - Baixar todas as músicas de uma playlist')
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
    if escolha == 6:
        playlist_url = input('Digite o link da playlist: ')
        playlist_id = playlist_url.split("/")[-1].split("?")[0]
        path = input('Digite o diretório para salvar as músicas: ')
        if not path:
            path = './Musics/'
        get_playlist_musics(client, playlist_id, path)