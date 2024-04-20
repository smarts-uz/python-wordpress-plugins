import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()
from bs4 import BeautifulSoup
from db.models import Plugin
import urllib.request as hyperlink
import os
import requests
from dotenv import load_dotenv

from Function.plugin_func import plugin_title
from Function.url_txt import create_url
load_dotenv()
src = os.getenv('src_path')
def plugins_parse():
    link = hyperlink.urlopen('http://plugins.svn.wordpress.org/',timeout=60)
    wordPressSoup = BeautifulSoup(link, 'html.parser')
    plugins_lists = wordPressSoup.find('ul')
    plugins = plugins_lists.find_all('li')
    for plugin in plugins[:10]:
        plugin_name_old = plugin.get_text(strip=True)
        try:
            slug = Plugin.objects.get(slug=plugin_name_old)
        except Plugin.DoesNotExist:
            slug = Plugin(slug=plugin_name_old)
            slug.save()
            print('Plugin\'s slug has been created')
        plugin_name = plugin_title(plugin_name=plugin_name_old)
        if plugin_name !=None:
            plugin_folder_name = f'{src}/All/{plugin_name}'
            create_url(path=plugin_folder_name, name=plugin_name_old)
        else:
            pass



plugins_parse()