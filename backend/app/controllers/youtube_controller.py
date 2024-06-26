from flask import Blueprint, request, jsonify
from app.services.youtube_service import download_youtube_video

youtube_bp = Blueprint('youtube', __name__)

@youtube_bp.route('/download', methods=['POST'])
def download_youtube():
    data = request.get_json()
    url = data.get('url')
    response = download_youtube_video(url)
    if response['status'] == 'OK':
        return jsonify(response), 200
    else:
        return jsonify(response), 500
