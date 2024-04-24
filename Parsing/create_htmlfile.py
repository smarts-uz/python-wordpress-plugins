import sys
sys.dont_write_bytecode = True
# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
from django_orm.db.models import Plugin
import os
import subprocess
from Parsing.run_y2z_cmd import run_2

import re
import time
from dotenv import load_dotenv
load_dotenv()
src = f'{os.getenv('src_path')}/All'
src_app = f'{os.getenv('src_path')}/App'
def run_y2z():
    plugins_dirs = os.listdir(src)
    for plugins_dir in plugins_dirs:
        plugin_path = os.path.join(src, plugins_dir)
        if os.path.isdir(plugin_path):
            plugin_items_dirs = os.listdir(plugin_path)
            for plugin_item_dir in plugin_items_dirs:
                if plugin_item_dir.endswith('.url'):
                    url_file = os.path.join(plugin_path, plugin_item_dir)
                    html_name = plugin_item_dir.split('.')[0].title()
                    html_file_path = os.path.join(plugin_path, html_name)
                    with open(url_file, 'r') as f:
                        data = f.read()
                        url = re.findall(r'https://wordpress.org/plugins.+', data)[0]
                        if os.path.exists(f"{src_app}/{html_name}.txt"):
                            print(f'This html already created: {html_file_path}')
                        else:
                            return_code = run_2(html_file_path=html_file_path,url=url)
                            plugin = Plugin.objects.get(url=url)
                            plugin.html = html_name
                            plugin.save()
                            print(f'Updated {html_name} successfully!')


def run_y2z_v2(start,end):
    plugins = Plugin.objects.filter(html=None).order_by('pk')
    for plugin in plugins[start:end]:
        if plugin.folder_path != None:
            html_file_path = os.path.join(plugin.folder_path, f'{plugin.name}')
            html_name = plugin.name
            print(html_name)
            if not os.path.exists(f"{html_file_path}.html"):
                return_code = run_2(html_file_path=html_file_path, url=plugin.url)
            else:
                print(f'This html already created: {html_file_path}')
            plugin = Plugin.objects.get(url=plugin.url)
            plugin.html = f'{html_name}.html'
            plugin.save()
            print(f'Updated {html_name} successfully!')



















