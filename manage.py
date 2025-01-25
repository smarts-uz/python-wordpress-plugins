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


    # Barcha Plugin ob'ektlarini olish
    plugins = Plugin.objects.all()



    # Har bir Plugin ob'ekti uchun `slug` va `name` maydonlaridagi '/' belgisini olib tashlash
    for plugin in plugins:
        plugin.slug = plugin.slug.replace('/', '')
        # plugin.name = plugin.name.replace('/', '') if plugin.name else None  # Agar name bo'lsa, o'zgartiradi
        plugin.save()

    print("Barcha slug va name maydonlaridagi '/' belgisi olib tashlandi.")