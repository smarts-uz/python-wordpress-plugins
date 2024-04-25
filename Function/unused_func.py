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

def func_unused(html_file_path,plugin):
    with open(html_file_path, 'rb') as f:
        html_body = f.read()
    soup = BeautifulSoup(html_body, 'html.parser')
    try:
        description_1 = soup.find('div', id="tab-description", class_='plugin-description section')
        description = description_1.find('div', class_='plugin-notice notice notice-error notice-alt').get_text(
            strip=True)
        if description != None:
            description_path = f'{description.replace("  ", " ")}.txt'
            plugin_desc_path = os.path.join(f'{src}/{plugin.name}', description_path)
            if not os.path.isfile(plugin_desc_path):
                with open(plugin_desc_path, 'w') as f:
                    # f.write(description)
                    print(f'{plugin_desc_path} has been created txt file')
            else:
                print(f'{plugin_desc_path} already exists')
        plugin.unused = True
        plugin.save()
    except:
        print('This plugin is active!!')