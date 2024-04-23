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
import re
import requests
import urllib.request as hyperlink
load_dotenv()
src = f'{os.getenv('src_path')}/All'
src_app = f'{os.getenv('src_path')}/App'
def func_screens(html_file_path,screen_path,plugin):
    with open(html_file_path, 'rb') as f:
        html_body = f.read()
    picture_soup = BeautifulSoup(html_body, 'html.parser')
    try:
        screenshots = picture_soup.find('div', class_='plugin-screenshots')
        picture_list = screenshots.find('ul')
        pictures = picture_list.find_all('li')
        for picture in pictures:
            picture_name = picture.get_text(strip=True).replace('.', '')
            src_picture = picture.find('a')['href']

            if not os.path.isfile(f"{screen_path}/{picture_name}.png"):
                with open(f'{screen_path}/{picture_name}.png', 'wb') as f:
                    res = hyperlink.urlopen(src_picture, timeout=60)
                    print(src_picture)
                    f.write(res.read())
                    print(f'Picture saved successfully {picture_name}')

            else:
                print(f'Picture already exists {picture_name}')

    except:
        with open(f'{screen_path}/NoPhoto.txt', "w") as f:
            f.write("Photo not found")
        print('Photo not found')
    plugin.screenshot = True
    plugin.save()
    print(f'Picture updated successfully {plugin.screenshot}')