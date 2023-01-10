from .middleware_settings import *  # noqa: ignore=F401 isort:skip
from .rest_framework_settings import *  # noqa: ignore=F401 isort:skip
from .installed_apps_settings import *  # noqa: ignore=F401 isort:skip
from .internationalizations_settings import *  # noqa: ignore=F401 isort:skip
from .auth_settings import *  # noqa: ignore=F401 isort:skip
from .host_settings import *  # noqa: ignore=F401 isort:skip
from .media_settings import *  # noqa: ignore=F401 isort:skip
from .database_settings import *  # noqa: ignore=F401 isort:skip


from pathlib import Path

from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = config('DEBUG', default=False, cast=bool)

DJANGO_SETTINGS_MODULE = config('DJANGO_SETTINGS_MODULE')

ROOT_URLCONF = 'configuration.urls'

WSGI_APPLICATION = 'configuration.wsgi.application'
