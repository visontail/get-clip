#Instagram Download Service
import instaloader

def generate_instagram_download_url(url: str) -> dict:
    """
    Generate a download URL for an Instagram video from the provided URL.

    :param url: URL of the Instagram video to be downloaded.
    :return: Dictionary containing the status and download URL or message of the operation.
    """
    print(f"Starting download for Instagram URL: {url}")
    try:
        loader = instaloader.Instaloader()
        shortcode = url.split('/')[-2]
        post = instaloader.Post.from_shortcode(loader.context, shortcode)

        if not post.is_video:
            raise ValueError("Provided URL is not a video")

        video_url = post.video_url
        print(f"Generated download URL: {video_url}")
        return {'status': 'OK', 'downloadUrl': video_url}

    except Exception as e:
        print(f"Error generating Instagram download URL: {str(e)}")
        return {'status': 'ERROR', 'message': str(e)}
