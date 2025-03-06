# app/config.py
import os
from pathlib import Path

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-for-development'
    UPLOADED_PHOTOS_DEST = os.path.join('static', 'uploads')
    UPLOAD_FOLDER = os.path.join('static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload
    TEMPLATE_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
    STATIC_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))