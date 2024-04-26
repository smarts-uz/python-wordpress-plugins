import sys

from Function.rating_func import func_rating

sys.dont_write_bytecode = True
# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
import os
from django_orm.db.models import Plugin
from dotenv import load_dotenv
from bs4 import BeautifulSoup
load_dotenv()
src = f'{os.getenv('src_path')}/All'

import requests


def get_rating(start,end):
    plugins = Plugin.objects.filter(fivestars=None,html__isnull=False).order_by('pk')
    for plugin in plugins[start:end]:
        plugin_path = f'{src}/{plugin.name}'
        html_file_path = os.path.join(f'{src}/{plugin.name}', plugin.html)
        func_rating(html_file_path, plugin)









