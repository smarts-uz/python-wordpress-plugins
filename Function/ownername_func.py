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

from Function.check_txt_exists import check_exists

load_dotenv()
src = f'{os.getenv('src_path')}/All'


def func_ownername(html_file_path,plugin):
    with open(html_file_path, 'rb') as f:
        html_body = f.read()
    soup = BeautifulSoup(html_body, 'html.parser')
    try:
        owner_name_class = soup.find('span', class_='byline')
        owner_name_1 = owner_name_class.find('span', class_='author vcard').get_text(strip=True)
        if owner_name_1 != '':
            owner_name = f'By {owner_name_1}'
            owner_name_path = os.path.join(plugin.folder_path, f"{owner_name}.txt")
            with open(owner_name_path, 'w') as f:
                # f.write(owner_name)
                print(f'[OS]Owner name: {owner_name} added to folder!!!!')
            plugin.owner_name = owner_name_1
            plugin.save()
            print(f'[DB] Owner name: updated to {owner_name_1}')


    except:
        pass