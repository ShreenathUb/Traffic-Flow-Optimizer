from flask import Flask
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__, 
                static_folder='static',
                template_folder='templates')
    app.config.from_object(config_class)
    
    # Initialize uploads folder
    from flask_uploads import configure_uploads, UploadSet, IMAGES
    photos = UploadSet('photos', IMAGES)
    configure_uploads(app, photos)
    
    # Register blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app