import sys

from Function.plugin_func import plugin_title
from Function.url_txt import create_url

sys.dont_write_bytecode = True
# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
from django_orm.db.models import Plugin
import shutil
from dotenv import load_dotenv
load_dotenv()
src = os.getenv('src_path')
def plugin_update(plugin_url):
    plugin = Plugin.objects.get(url=plugin_url)
    print(plugin_url)
    if plugin_url[-1] != '/':
        plugin_url += '/'
    slug = plugin_url.split('/')[-2]
    slug += '/'
    plugin.slug = slug
    print(f'Slug updated: {slug}')
    plugin_path = plugin.folder_path
    print(plugin_path)
    shutil.rmtree(plugin_path, ignore_errors=True)
    print(f'Path deleted: {plugin_path}')
    plugin_name = plugin_title(plugin_name=slug)
    if not os.path.exists(f'{src}/All/{plugin_name}'):
        os.makedirs(f'{src}/All/{plugin_name}')
    create_url(path=plugin_path, name=slug)
    plugin.url = plugin_url
    plugin.save()

    



plugin_update("https://wordpress.org/plugins/0-errors/")