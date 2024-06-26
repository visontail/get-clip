
from app.utils.path_processor import ensure_download_path

def download_tiktok_video(url):
    try:

        #code goes here
        ensure_download_path()

        return {'status': 'OK', 'message': 'Video downloaded successfully'}

    except Exception as e:
        error_message = f"Unexpected error occurred: {str(e)}"
        return {'status': 'ERROR', 'message': error_message}
