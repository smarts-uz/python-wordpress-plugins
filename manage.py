#!/usr/bin/env python
import os
import sys

from dotenv import load_dotenv

# Django sozlamalarini yuklash
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_orm.settings")
import django
django.setup()

# Django modelini import qilish
from django_orm.db.models import Plugin

if __name__ == "__main__":
    # .env faylini yuklash
    load_dotenv()

    # .env faylidan 'DATABASE_NAME' ni olish
    db_name = os.getenv('DATABASE_NAME')
    print(db_name)

    # Django uchun kerakli buyruqlarni bajarish
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
    # .env faylidan 'DATABASE_NAME' ni olish
    db_name = os.getenv('DATABASE_NAME')
    print(db_name)
