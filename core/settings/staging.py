import os

from .base import *


ALLOWED_HOSTS = ["*"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "postgres"),
        "USER": os.environ.get("POSTGRES_USER", "postgres"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "postgres"),
        "HOST": os.environ.get("POSTGRES_HOST", "postgres"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
        'CONN_MAX_AGE': int(os.environ.get("DB_CONN_MAX_AGE", "500")),
    }
}

REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")
CACHE_DB = os.environ.get("CACHE_DB", "0")

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"{REDIS_URL}/{CACHE_DB}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PARSER_CLASS": "redis.connection.HiredisParser",
        },
        "KEY_PREFIX": "core-be",
    },
}

import django_heroku
django_heroku.settings(
    locals(), databases=False,
    test_runner=True, staticfiles=True,
    allowed_hosts=False, logging=True,
    secret_key=True)