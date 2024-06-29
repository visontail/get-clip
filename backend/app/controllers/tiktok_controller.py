from flask import Blueprint, request, jsonify
from app.services.tiktok_service import download_tiktok_video
from app.utils.path_processor import ensure_download_path

tiktok_bp = Blueprint('tiktok', __name__)

@tiktok_bp.route('/download', methods=['POST'])
def download_tiktok():
    """
    Download a TikTok video from the provided URL.

    :return: Dictionary containing the status and message of the download operation.
    """
    data = request.get_json()
    url = data.get('url')

    try:
        download_path = ensure_download_path()
        video_path = download_tiktok_video(url, download_path)

        response = {
            'status': 'OK',
            'message': 'Video downloaded successfully.',
            'video_path': video_path
        }
        return jsonify(response), 200
    except ValueError as e:
        response = {
            'status': 'Error',
            'message': str(e)
        }
        return jsonify(response), 500
