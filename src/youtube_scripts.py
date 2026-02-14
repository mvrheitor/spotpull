from pytubefix import YouTube
from pytubefix import Search

def search_video(query):
    videos = Search(query).videos
    video_url = videos[0].watch_url # pega o link do primeiro resultado

    return video_url

def download_video_audio(url, path=None):
    yt = YouTube(url)
    ys = yt.streams.get_audio_only()
    print('Baixando:', yt.title)
    ys.download(output_path=path)
    print("Música baixada com sucesso!")