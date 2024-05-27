from .base import *

# installed app in development mode
INSTALLED_APPS += []

# Logs in console
if DEBUG:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "console": {
                "level": "DEBUG",
                "class": "rich.logging.RichHandler",
                "show_time": False,
            },
            "file": {
                "level": "DEBUG",
                "class": "logging.FileHandler",
                "filename": "logs/development.log",
            },
        },
        "loggers": {
            "django.db.backends": {
                "handlers": ["console", "file"],
                "level": "DEBUG",
                "propagate": False,
            },
        },
    }
