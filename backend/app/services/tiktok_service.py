# Import necessary modules
from TikTokApi import TikTokApi
import os
import requests
import re

def extract_video_id(url: str) -> str:
    """
    Extracts the video ID from a TikTok video URL.

    :param url: TikTok video URL.
    :return: Video ID extracted from the URL.
    :raises ValueError: If the URL is invalid or the video ID cannot be extracted.
    """
    # Regular expressions for different TikTok URL formats
    patterns = [
        r"/@[\w\-\.]+/video/(\d+)",          # Format: https://www.tiktok.com/@username/video/video_id
        r"/video/(\d+)\?"                    # Format: https://vm.tiktok.com/video/video_id?
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    raise ValueError("Invalid TikTok video URL. Unable to extract video ID.")

def download_tiktok_video(url: str, download_path: str) -> str:
    """
    Download a TikTok video from the provided URL.

    :param url: URL of the TikTok video to be downloaded.
    :param download_path: Path where the downloaded video will be saved.
    :return: Path to the downloaded video file.
    :raises ValueError: If the URL is invalid or downloading fails.
    """
    try:
        # Initialize TikTokApi
        api = TikTokApi()

        # Extract video ID from URL
        video_id = extract_video_id(url)

        # Fetch video metadata (e.g., video URL)
        video_info = api.getTikTokById(video_id)
        video_url = video_info['itemInfo']['itemStruct']['video']['downloadAddr']

        # Download video
        response = requests.get(video_url)
        response.raise_for_status()

        # Create file path
        video_path = os.path.join(download_path, f"{video_id}.mp4")

        # Save video file
        with open(video_path, 'wb') as f:
            f.write(response.content)

        return video_path
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise ValueError(f"Error downloading TikTok video: {str(e)}")
