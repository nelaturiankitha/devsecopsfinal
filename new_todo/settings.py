from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1+l(5qzq_1#e$#$k!g*+=6cs7ri@%$iu6u&%$n7g#z0uhgpm!v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','devsecopstry1-env.eba-wfqksbgq.us-west-2.elasticbeanstalk.com']
CSRF_TRUSTED_ORIGINS = ['http://try90.eba-mfbmxiis.ap-south-1.elasticbeanstalk.com','https://bc4f1197ac474b4e8d0c21f7f8f1eaa0.vfs.cloud9.eu-west-1.amazonaws.com','https://7b1f971ea52140d0b8e30096c7d178e9.vfs.cloud9.eu-west-1.amazonaws.com','https://bb8fd27cd5cf49d5a4effe26123fc50b.vfs.cloud9.eu-west-1.amazonaws.com','http://devsecopstry1-env.eba-wfqksbgq.us-west-2.elasticbeanstalk.com/']
CORS_ALLOWED_ORIGINS = [
    "https://bb8fd27cd5cf49d5a4effe26123fc50b.vfs.cloud9.eu-west-1.amazonaws.com",
    # Add other trusted origins as needed
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todoapp.apps.TodoappConfig',
]

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


ROOT_URLCONF = 'new_todo.urls'

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

WSGI_APPLICATION = 'new_todo.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '8IPkvMwMKn6PqkJCvXme',
        'HOST': 'devsecopstry6.chwlezgyi7rm.eu-west-1.rds.amazonaws.com',  
        'PORT': '5432',       
    }
}



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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = 'static'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
