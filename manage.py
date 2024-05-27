#!/usr/bin/env python
import sys
from os import environ as ENV


def set_django_env():
    AVAILABLE_ENVS = ["development", "test", "production"]
    env = ENV.get("DJANGO_ENV", "development")
    if env not in AVAILABLE_ENVS:
        raise ValueError("Not a valid environment mode.")

    ENV.setdefault("DJANGO_SETTINGS_MODULE", f"config.environments.{env}")


def main():
    """Run administrative tasks."""
    set_django_env()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
