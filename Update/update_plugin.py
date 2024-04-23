import sys

from Function.plugin_func import plugin_title
from Function.rating_func import func_rating
from Function.screens_func import func_screens
from Function.url_txt import create_url
from Parsing.rating import get_rating
from Parsing.run_y2z_cmd import run_2

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
    if plugin_url[-1] != '/':
        plugin_url += '/'
    slug = plugin_url.split('/')[-2]
    slug += '/'
    plugin.slug = slug
    print(f'Slug updated: {slug}')
    plugin_path = plugin.folder_path
    # shutil.rmtree(plugin_path, ignore_errors=True)
    # print(f'Path deleted: {plugin_path}')
    # plugin_name = plugin_title(plugin_name=slug)
    # if not os.path.exists(f'{src}/All/{plugin_name}'):
    #     os.makedirs(f'{src}/All/{plugin_name}')
    # create_url(path=plugin_path, name=slug)
    # plugin.url = plugin_url
    # html_file_path = os.path.join(plugin.folder_path, f'{plugin.name}')
    # html_name = plugin.name
    # return_code = run_2(html_file_path=html_file_path, url=plugin.url)
    screen_path = os.path.join(plugin.folder_path, 'Screens')
    if not os.path.exists(screen_path):
        os.makedirs(screen_path)
    html_file = os.path.join(plugin.folder_path,plugin.html)
    func_screens(html_file, screen_path, plugin)
    func_rating(html_file,plugin)
    plugin.save()

    



plugin_update("https://wordpress.org/plugins/0-errors/")