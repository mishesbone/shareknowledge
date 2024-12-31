import os

SECRET_KEY = os.urandom(24)
SQLALCHEMY_DATABASE_URI = 'sqlite:///shareknowledge.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOADED_MEDIA_DEST = 'static/uploads'
