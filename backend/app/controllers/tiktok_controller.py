# TikTok Download Controller
from flask import Blueprint, request, jsonify
from app.services.tiktok_service import get_tiktok_download_urls

tiktok_bp = Blueprint('tiktok', __name__)

@tiktok_bp.route('/download', methods=['POST'])
def handle_tiktok_download():
    try:
        # Extract TikTok URL from the request
        tiktok_url = request.json.get('url')

        if not tiktok_url:
            return jsonify({'error': 'TikTok URL is required'}), 400  # HTTP 400 Bad Request

        # Get the download URL
        download_links = get_tiktok_download_urls(tiktok_url)

        # Return the download URL
        return jsonify({'downloadUrl': download_links}), 200  # HTTP 200 OK

    except ValueError as ve:
        print(f"ValueError in TikTok download handler: {str(ve)}")
        return jsonify({'error': str(ve)}), 404  # HTTP 404 Not Found

    except Exception as e:
        print(f"Error in TikTok download handler: {str(e)}")
        return jsonify({'error': 'Failed to get download URL'}), 500  # HTTP 500 Internal Server Error
