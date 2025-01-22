import sys

from Function.download_zip import func_download
from Function.element_func import func_elements
from Function.ownername_func import func_ownername
from Function.plugin_func import plugin_title
from Function.rating_func import func_rating
from Function.screens_func import func_screens
from Function.unused_func import func_unused
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
src = f'{os.getenv("src_path")}/All'
def plugin_update(plugin_url):
    plugin = Plugin.objects.get(url=plugin_url)
    if plugin_url[-1] != '/':
        plugin_url += '/'
    slug = plugin_url.split('/')[-2]
    slug += '/'
    plugin.slug = slug
    print(f'Slug updated: {slug}')
    plugin_path = os.path.join(src, plugin.name)
    if plugin.html != None:
        shutil.rmtree(plugin_path, ignore_errors=True)
        print(f'Path deleted: {plugin_path}')
        plugin_name = plugin_title(plugin_name=slug)
        if not os.path.exists(f'{src}/{plugin_name}'):
            os.makedirs(f'{src}/{plugin_name}')
        create_url(path=plugin_path, name=slug)
        plugin.url = plugin_url
        html_file_path = os.path.join(plugin_path, f'{plugin.name}')
        html_name = plugin.name
        return_code = run_2(html_file_path=html_file_path, url=plugin.url)
        screen_path = os.path.join(f'{src}/{plugin.name}', 'Screens')
        if not os.path.exists(screen_path):
            os.makedirs(screen_path)
        print(plugin.html)
        html_file_dst = os.path.join(f'{src}/{plugin.name}', plugin.html)
        func_screens(html_file_dst, screen_path, plugin)
        func_rating(html_file_path=html_file_dst, plugin=plugin)
        func_download(html_file_path=html_file_dst, plugin=plugin)
        func_elements(html_file_path=html_file_dst, pl=plugin)
        func_ownername(html_file_path=html_file_dst, plugin=plugin)
        func_unused(html_file_path=html_file_dst, plugin=plugin)
    plugin.save()


    


# plugin_update('https://wordpress.org/plugins/0-errors/')
