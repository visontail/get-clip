import yt_dlp
from app.utils.path_processor import ensure_download_path

def download_youtube_video(url: str):
    """
    Download a YouTube video from the provided URL using yt-dlp.
    :param url: URL of the YouTube video to be downloaded.
    :return: Dictionary containing the status and message of the download operation.
    """
    try:
        download_path = ensure_download_path()
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        return {'status': 'OK', 'message': 'Video downloaded successfully'}
    except Exception as e:
        return {'status': 'ERROR', 'message': str(e)}