import instaloader
from app.utils.path_processor import ensure_download_path

def download_instagram_video(url):
    try:
        loader = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(loader.context, url.split('/')[-2])
        filename = f"{ensure_download_path()}/{post.owner_username}_{post.date_utc}.mp4"
        loader.download_post(post, target=filename)
        return {'status': 'OK', 'message': 'Video downloaded successfully'}
    except Exception as e:
        return {'status': 'ERROR', 'message': str(e)}
