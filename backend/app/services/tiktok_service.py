# TikTok Download Service
import requests
from requests.models import InvalidURL

BASE_URL = 'https://www.tikwm.com'

def get_media(url: str) -> list[dict]:
    """
    Fetches media information from a TikTok URL.

    :param url (str): The TikTok URL.

    :return: list[dict]: A list of dictionaries containing media information. Each dictionary has the following keys:
            - url (str): The URL of the media.
            - type (str): The type of the media (e.g., 'video', 'music').
            - watermark (bool): Indicates whether the media has a watermark.
    """
    response = requests.post(f'{BASE_URL}/api/', data={'url': url, 'count': 12, 'cursor': 0, 'web': 1, 'hd': 1})
    res = response.json()
    if res['code'] == 0:
        return [
            {
                'url': BASE_URL + res['data'].get('hdplay', res['data']['play']),
                'type': 'video',
                'watermark': False
            },
            {
                'url': BASE_URL + res['data']['wmplay'],
                'type': 'video',
                'watermark': True
            },
            {
                'url': BASE_URL + res['data']['music'],
                'type': 'music',
                'watermark': False
            }
        ]
    else:
        raise InvalidURL(res['msg'])

def get_tiktok_download_urls(tiktok_url: str) -> list[dict]:
    """
    Fetches the download URLs for the media associated with a TikTok video.

    :param tiktok_url (str): The URL of the TikTok video.

    :returns: list[dict]: A list of dictionaries containing the download URLs for the media.
                Each dictionary contains the following keys:
                    - 'url': The download URL of the media.
                    - 'type': The type of the media (e.g., 'video', 'image').
    """
    try:
        # Get the media download links
        download_links = get_media(tiktok_url)
        return download_links
    except Exception as e:
        print(f"Error fetching TikTok download URLs: {str(e)}")
        raise
