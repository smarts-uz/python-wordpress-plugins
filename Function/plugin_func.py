import os.path
import time
import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()
from django_orm.db.models import Plugin
import requests
from bs4 import BeautifulSoup

from dotenv import load_dotenv
load_dotenv()

src = os.getenv('src_path')
def plugin_title(plugin_name):
    plugin = Plugin.objects.get(slug=plugin_name)
    plugin_url = f"https://wordpress.org/plugins/{plugin_name}"
    try:
        response = requests.get(plugin_url, timeout=30, allow_redirects=False)
    except requests.exceptions.Timeout:
        time.sleep(30)
        print('Sleeping 30sec')
        response = requests.get(plugin_url, timeout=30, allow_redirects=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            plugin_folder_name = soup.find('h1', class_='plugin-title').get_text(strip=True,separator=' ')
            unsupchar = ["*", '"', "/", "\\", "<", ">", ":", "|", "?","\t",'..']
            for char in unsupchar:
                plugin_folder_name = plugin_folder_name.replace(char, ' ')
            if plugin_folder_name[-1] == '.':
                plugin_folder_name = plugin_folder_name.replace('.','')
            plugin_folder_name = plugin_folder_name.replace('  ', ' ').strip()
        except Exception as e:
            print(e)
            plugin_folder_name = plugin_name
        print(plugin_folder_name)
        if not os.path.exists(f'{src}/All/{plugin_folder_name}'):
            os.makedirs(f'{src}/All/{plugin_folder_name}')
            plugin.folder_path = f'{src}/All/{plugin_folder_name}'
            plugin.save()
            print(f'Created {plugin.folder_path}')
            print(f'Created folder: {src}/All/{plugin_folder_name}')
        else:
            print(f'Folder already exists: {src}/All/{plugin_folder_name}')
        if not os.path.isfile(f"{src}/All/{plugin_folder_name}/App.main"):
            with open(f"{src}/All/{plugin_folder_name}/App.main", "w", encoding='utf-8') as file:
                file.write(response.text)
        else:
            pass

        return plugin_folder_name

    else:
        print(plugin_name + " is already a plugin")


