import datetime
from pathlib import Path
from decouple import config as env
from datetime import timedelta

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for Django project
SECRET_KEY = env("SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = []
INTERNAL_IPS = ['127.0.0.1']
# Debug configuration
if DEBUG:
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "172.19.0.7"]
    INTERNAL_IPS = ALLOWED_HOSTS


# Installed applications
Local_Apps = [
    "td_apps.user.apps.UserConfig",
    "td_apps.core.apps.CoreConfig",
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'debug_toolbar',
    'django_prometheus',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = Local_Apps + THIRD_PARTY_APPS + DJANGO_APPS

# Middleware settings
MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_prometheus.middleware.PrometheusAfterMiddleware',
]

# URLs configuration
ROOT_URLCONF = 'config.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'

# Database settings
DATABASES = {
    'default': {
        'ENGINE': env("DATABASE_ENGINE"),
        'NAME': BASE_DIR / env("DATABASE_NAME"),
    }
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Site name
SITE_NAME = env("SITE_NAME")

# Static files settings
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model
AUTH_USER_MODEL = "user.user"

# Email settings
# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'marashipouya@gmail.com'  # Replace with your Gmail address
EMAIL_HOST_PASSWORD = 'sample'  # Replace with your App Password
DEFAULT_FROM_EMAIL = "myapp"

# REST framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# setting for redis cache 
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  # Replace with your Redis server info
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}


# Celery settings
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"

# Celery Task Serialization and Content Acceptance
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_DEBUG = "DEBUG"

# Celery Timezone (UTC by default)
CELERY_TIMEZONE = 'Asia/Tehran'