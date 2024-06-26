from flask import Blueprint, request, jsonify
from app.services.instagram_service import download_instagram_video

instagram_bp = Blueprint('instagram', __name__)

@instagram_bp.route('/download', methods=['POST'])
def download_instagram():
    data = request.get_json()
    url = data.get('url')
    response = download_instagram_video(url)
    if response['status'] == 'OK':
        return jsonify(response), 200
    else:
        return jsonify(response), 500
