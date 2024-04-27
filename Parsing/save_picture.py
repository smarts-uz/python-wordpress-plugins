import sys

from Function.screens_func import func_screens
from Parsing.run_y2z_cmd import run_2

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

def parse_picture():
    plugins_dirs = os.listdir(src)
    for plugin_dir in plugins_dirs:
        plugin_path = os.path.join(src, plugin_dir)
        plugin_in_dirs = os.listdir(plugin_path)
        if "Screens" in plugin_in_dirs:
            print('This plugin\'s photo already parsed')
        else:
            for plugin_in_dir in plugin_in_dirs:
                if plugin_in_dir.endswith('.url'):
                    screen_path = os.path.join(plugin_path, 'Screens')
                    if not os.path.exists(screen_path):
                        os.makedirs(screen_path)
                    plugins_url_path = os.path.join(plugin_path, plugin_in_dir)
                    with open(plugins_url_path, 'r') as f:
                        data = f.read()
                        url = re.findall(r'https://wordpress.org/plugins.+', data)[0]
                    response = requests.get(url, timeout=60)
                    picture_soup = BeautifulSoup(response.text, 'html.parser')
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




def parse_picture_v2(start,end):
    plugins = Plugin.objects.all().order_by('pk')
    for plugin in plugins[start:end]:
        if plugin.screenshot ==False and plugin.html !=None:
            try:
                print(plugin.pk, plugin.slug)
                plugin_path = f"{src}/{plugin.name}"
                html_file_path = os.path.join(plugin_path, plugin.html)
                if not os.path.isfile(html_file_path):
                    # run_2(html_file_path,plugin.url)
                    continue
                screen_path = os.path.join(plugin_path, 'Screens')
                if not os.path.exists(screen_path):
                    a = os.makedirs(screen_path)
                    print('created folder:', screen_path)
                func_screens(html_file_path, screen_path, plugin)

            except Exception as e:
                print(e)



