from config import get_client
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

def display_menu():
    client = get_client()
    print('Escolha uma opção: ')
    print('[1] - Baixar capa de album')
    print('[2] - Baixar imagem de playlist')
    escolha = int(input())
    if escolha == 1:
        album_url = input('Digite o link do álbum: ')
        album_id = album_url.split("/")[-1].split("?")[0]
        get_album_cover(client, album_id)
    if escolha == 2:
        playlist_url = input('Digite o link da playlist: ')
        playlist_id = playlist_url.split("/")[-1].split("?")[0]
        get_playlist_image(client, playlist_id)

if __name__ == '__main__':
    display_menu()

