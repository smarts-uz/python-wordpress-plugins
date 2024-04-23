import sys
import time

sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
from bs4 import BeautifulSoup
from django_orm.db.models import Plugin
import urllib.request as hyperlink
import os
from dotenv import load_dotenv

from Function.plugin_func import plugin_title
from Function.url_txt import create_url
load_dotenv()
src = os.getenv('src_path')
src_all = os.path.join(src, 'All')
src_app = os.path.join(src, 'App')
def plugins_parse(start:int,end:int):
    if not os.path.isdir(src_all):
        os.mkdir(src_all)
    if not os.path.isdir(src_app):
        os.mkdir(src_app)
    link = hyperlink.urlopen('http://plugins.svn.wordpress.org/',timeout=60)
    wordPressSoup = BeautifulSoup(link, 'html.parser')
    plugins_lists = wordPressSoup.find('ul')
    plugins = plugins_lists.find_all('li')
    k = start
    for plugin in plugins[start:]:
        print(f'current: {k} | end: {end}')
        plugin_name_old = plugin.get_text(strip=True)
        try:
            slug = Plugin.objects.get(slug=plugin_name_old)
            print(f'Plugin {plugin_name_old} already exists')
        except Plugin.DoesNotExist:
            slug = Plugin.objects.create(slug=plugin_name_old,screenshot=False,elements=False)
            print('Plugin\'s slug has been created',slug.slug)
        if slug.url == None or slug.folder_path ==None or slug.name==None:
            plugin_name = plugin_title(plugin_name=plugin_name_old)
            if plugin_name != None:
                plugin_folder_name = f'{src}/All/{plugin_name}'
                create_url(path=plugin_folder_name, name=plugin_name_old)
                slug.folder_path = plugin_folder_name
                slug.name = plugin_name
                slug.url = f"https://wordpress.org/plugins/{plugin_name_old}"
            else:
                pass
            slug.save()
        k += 1





