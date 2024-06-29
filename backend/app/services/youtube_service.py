from pytube import YouTube
from app.utils.path_processor import ensure_download_path

def download_youtube_video(url : str):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        download_path = ensure_download_path()
        stream.download(output_path=download_path)
        return {'status': 'OK', 'message': 'Video downloaded successfully'}
    except Exception as e:
        return {'status': 'ERROR', 'message': str(e)}
