#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin_bot.settings')
    os.environ.setdefault('DB_LOCAL', 'True')
    os.environ.setdefault('TOKEN_ADMIN_BOT', 'admin_bot.django-insecure-jaes6cu-vorpqsppr4c#(3i87x81mc(up2f(h7axwkgs50%mg(')
    os.environ.setdefault('DB_PSW', 'as89lokan07')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
