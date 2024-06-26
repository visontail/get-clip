from flask import Blueprint, request, jsonify
from app.services.tiktok_service import download_tiktok_video

tiktok_bp = Blueprint('tiktok', __name__)

@tiktok_bp.route('/download', methods=['POST'])
def download_tiktok():
    data = request.get_json()
    url = data.get('url')
    response = download_tiktok_video(url)
    if response['status'] == 'OK':
        return jsonify(response), 200
    else:
        return jsonify(response), 500
