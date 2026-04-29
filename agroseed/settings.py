REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'core.exceptions.custom_exception_handler'
}

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'agronomia',  # ← nome do banco
        'USER': 'root',
        'PASSWORD': 'Ultr0n@2025',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "core/static"
]

DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = '7!dtd&t$ac2zgm_tzooc^9m9)(6l^u%g4x1d3-zb!kb05q(gdg'

ROOT_URLCONF = 'agroseed.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # pode deixar vazio ou adicionar pasta global depois
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