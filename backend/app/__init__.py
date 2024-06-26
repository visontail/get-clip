from flask import Flask

def create_app():
    app = Flask(__name__)

    #import blueprints
    from app.controllers.youtube_controller import youtube_bp
    from app.controllers.instagram_controller import instagram_bp
    from app.controllers.tiktok_controller import tiktok_bp

    #register blueprints
    app.register_blueprint(youtube_bp, url_prefix='/api/youtube')
    app.register_blueprint(instagram_bp, url_prefix='/api/instagram')
    app.register_blueprint(tiktok_bp, url_prefix='/api/tiktok')

    return app