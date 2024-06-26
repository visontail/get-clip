import os

def ensure_download_path():
    downloads_folder = os.path.expanduser("~/Downloads")
    if not os.path.exists(downloads_folder):
        os.makedirs(downloads_folder)
    return downloads_folder