from flask import Blueprint, request, jsonify
from app.services.instagram_service import generate_instagram_download_url

instagram_bp = Blueprint('instagram', __name__)

@instagram_bp.route('/download', methods=['POST'])
def download_instagram():
    """
    Generate a download URL for an Instagram video from the provided URL.

    :return: Dictionary containing the status and download URL or message of the download operation.
    """
    data = request.get_json()
    url = data.get('url')
    print(f"Received request to generate download URL for Instagram video from URL: {url}")
    response = generate_instagram_download_url(url)
    if response['status'] == 'OK':
        print(f"Download URL generated successfully, URL: {response['downloadUrl']}")
        return jsonify(response), 200
    else:
        print(f"Failed to generate download URL, message: {response['message']}")
        return jsonify(response), 500
