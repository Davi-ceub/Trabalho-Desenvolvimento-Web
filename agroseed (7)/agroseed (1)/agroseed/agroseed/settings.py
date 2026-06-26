
from pathlib import Path


# =========================================================
# BASE CONFIG
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '7!dtd&t$ac2zgm_tzooc^9m9)(6l^u%g4x1d3-zb!kb05q(gdg'

DEBUG = True

ALLOWED_HOSTS = ['*']

APPEND_SLASH = True


# =========================================================
# INSTALLED APPLICATIONS
# =========================================================

INSTALLED_APPS = [

    # DJANGO APPS
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # THIRD PARTY APPS
    'rest_framework',
    'rest_framework_simplejwt',

    # LOCAL APPS
    'core',
]


# =========================================================
# MIDDLEWARE
# =========================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =========================================================
# ROOT URL CONFIG
# =========================================================

ROOT_URLCONF = 'agroseed.urls'


# =========================================================
# TEMPLATES
# =========================================================

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


# =========================================================
# DATABASE
# =========================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'agronomia',
        'USER': 'root',
        'PASSWORD': 'ceub123456',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# =========================================================
# DJANGO REST FRAMEWORK
# =========================================================

REST_FRAMEWORK = {

    # JWT AUTHENTICATION
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    # DEFAULT PERMISSIONS
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    # CUSTOM EXCEPTION HANDLER
    'EXCEPTION_HANDLER': 'core.exceptions.custom_exception_handler',
}


# =========================================================
# LOGIN / LOGOUT
# =========================================================

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/login/'


# =========================================================
# EMAIL CONFIG
# =========================================================

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'seuemail@gmail.com'

EMAIL_HOST_PASSWORD = 'senha-de-app'


# =========================================================
# STATIC FILES
# =========================================================

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'core/static'
]


# =========================================================
# DEFAULT PRIMARY KEY
# =========================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
