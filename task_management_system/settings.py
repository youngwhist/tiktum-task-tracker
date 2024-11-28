from pathlib import Path
import environ
import os
from datetime import timedelta

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY', default='django-insecure-default-key')
DEBUG = env('DEBUG', default=True)
# Настройки ALLOWED_HOSTS для продакшн и разработки
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['0.0.0.0', '176.115.151.66', '85.193.83.211', 'localhost', 'tiktum.com'])

# Приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',  # Добавлено
    'users',
    'projects',
    'tasks',
    "sslserver",
]

# Django REST Framework настройки
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# JWT настройки
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'task_management_system.urls'

# Шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Указываем путь к папке templates
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

WSGI_APPLICATION = 'task_management_system.wsgi.application'

# Настройки базы данных для PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'task_db'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', '25111'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),  # This should be 'db'
        'PORT': '5432',
    }
}


# Валидация паролей
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

# Интернационализация
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Статические файлы
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Пользовательская модель пользователя
AUTH_USER_MODEL = 'users.CustomUser'

# Первичный ключ по умолчанию
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Настройки CORS для разработки и продакшн
#CORS_ALLOWED_ORIGINS = [
#    "http://localhost:80",  # фронтенд на другом порту в разработке
#    "http://85.193.83.211",   # ваш сервер
#    "https://tiktum.com",    # домен для продакшн
#]

CORS_ALLOW_ALL_ORIGINS = True  # только для разработки или тестирования!
