from .settings import *
import os

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-portfolio-dev-key-change-in-production')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# WhiteNoise for static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security headers (enabled in prod)
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Database: use env variable if provided (for PostgreSQL on Railway)
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    import dj_database_url
    DATABASES = {'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)}
