import instaloader
from app.utils.path_processor import ensure_download_path
import os
import shutil
import tempfile

def download_instagram_video(url: str):
    """
    Download an Instagram video from the provided URL.

    :param url: URL of the Instagram video to be downloaded.
    :return: Dictionary containing the status and message of the download operation.
    """
    try:
        loader = instaloader.Instaloader(dirname_pattern="{target}", filename_pattern="{date_utc}_UTC_{shortcode}")
        shortcode = url.split('/')[-2]
        post = instaloader.Post.from_shortcode(loader.context, shortcode)

        download_folder = ensure_download_path()
        temp_dir = tempfile.mkdtemp()

        # Set the target as the temporary directory
        loader.dirname_pattern = temp_dir

        # Download the post
        loader.download_post(post, target=shortcode)

        # Move only the MP4 files to the download folder
        for file_name in os.listdir(temp_dir):
            temp_file_path = os.path.join(temp_dir, file_name)
            if os.path.isfile(temp_file_path) and file_name.endswith('.mp4'):
                shutil.move(temp_file_path, os.path.join(download_folder, file_name))

        # Cleanup temporary directory
        shutil.rmtree(temp_dir)

        return {'status': 'OK', 'message': 'Video downloaded successfully'}
    except Exception as e:
        return {'status': 'ERROR', 'message': str(e)}
