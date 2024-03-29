"""
Django settings for library project.
Generated by 'django-admin startproject' using Django 4.1.7.
For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pw3e2i191mgdhiilpccf$w@8ph+_ti#-&ps7_6f0_0ck5vx1v*'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'drf_yasg',
    'corsheaders',
    'authors',
    'authapp',
    'toDoapp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
"http://localhost:3000",
"http://127.0.0.1:3000"
]


ROOT_URLCONF = 'library.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR /'frontend' / 'build'],
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

WSGI_APPLICATION = 'library.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
    #'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'],
    #'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.DjangoModelPermissions'],
    'DEFAULT_AUTHENTICATION_CLASSES': [#'rest_framework.authentication.BasicAuthentication',
                                       'rest_framework.authentication.SessionAuthentication',
                                       'rest_framework.authentication.TokenAuthentication',
                                       ],

    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 100

    # http://127.0.0.1:8002/api/authors/
    # http://127.0.0.1:8002/api/2.0/authors/
    # 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning'

    # http://127.0.0.1:8002/api/authors/
    # http://127.0.0.1:8002/api/2.0/authors/
    # 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning'

    # http://v1.somesite.com/api/authors/
    # http://v2.somesite.com/api/authors/
    # 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.HostNameVersioning'
    # http://127.0.0.1:8000/api/authors/?version=2.0
    # возможно один из самых удобных способов получения нужной версии апи, т.к. этот способ не требует "плодить" пути path
    # в urls, нужно всего лишь указать гет запрос с таким атрибутом ?version=2.0, соответсвенно название версии менять на ту которая нужна
    # всё что нужно это готовые переопределённые методы get_serializer_class с нужным сериализатором 
    #'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.QueryParameterVersioning',
     # http://somesite.com/api/authors/
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning'

}

# URLPathVersioning, NamespaceVersioning, HostNameVersioning, QueryParameterVersioning, AcceptHeaderVersioning

#if DEBUG:
#       REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append('rest_framework.renderers.BrowsableAPIRenderer',)

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators


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


AUTH_USER_MODEL = "authapp.User"

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#PASSWORD_HASHERS = [
#    'django.contrib.auth.hashers.Argon2PasswordHasher',
#    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
#    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
#    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
#    'django.contrib.auth.hashers.BCryptPasswordHasher',
#]


GRAPHENE = {
       "SCHEMA": "library.schema.schema"
       }

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR /'frontend' / 'build' / 'static'
]

