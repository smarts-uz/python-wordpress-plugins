import sys
sys.dont_write_bytecode = True
# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
from django_orm.db.models import Plugin
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import re
import requests
import urllib.request as hyperlink
load_dotenv()
src = f'{os.getenv('src_path')}/All'

def func_elements(html_file_path,pl):
    with open(html_file_path, 'rb') as f:
        html_body = f.read()
    soup = BeautifulSoup(html_body, 'html.parser')
    try:
        plugins_info_class = soup.find('div', class_='widget plugin-meta').find('ul').find_all('li')
        for plugin in plugins_info_class:
            if plugin('div', class_='tags'):
                tags = plugin.find('div', class_='tags').find_all('a')
                for tag in tags:
                    tag_path = os.path.join(f"{src}/{pl.name}", f'#{tag.text}.txt')
                    if not os.path.isfile(tag_path):
                        with open(tag_path, 'w') as f:
                            # f.write(tag.text)
                            print(f'Created txt file {tag_path}')
                    else:
                        print(f'File {tag_path} already exists')
            else:
                plugin_text = plugin.text
                if 'Advanced View' not in plugin_text:
                    plugin_text = plugin.get_text(' ', strip=True)
                    unsupchar = ["*", '"', "/", "\\", "<", ">", ":", "|", "?"]
                    for char in unsupchar:
                        plugin_text = plugin_text.replace(char, " ")
                    plugin_text = plugin_text.replace('  ', ' ')
                    plugin_text_path = os.path.join(f'{src}/{pl.name}', f'{plugin_text}.txt')
                    if not os.path.isfile(plugin_text_path):
                        with open(plugin_text_path, 'w') as f:
                            f.write(plugin_text)
                            print(f'Created txt file {plugin_text_path}')
                    else:
                        print(f'File {plugin_text_path} already exists')
        pl.elements = True
        pl.save()
    except:
        pl.elements = True
        pl.save()