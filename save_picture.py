from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import re
import requests
import urllib.request as hyperlink
load_dotenv()
src = f'{os.getenv('src_path')}/All'

def parse_picture():
    plugins_dirs = os.listdir(src)
    for plugin_dir in plugins_dirs:
        plugin_path = os.path.join(src, plugin_dir)
        plugin_in_dirs = os.listdir(plugin_path)
        for plugin_in_dir in plugin_in_dirs:
            if plugin_in_dir.endswith('.url'):
                plugins_url_path = os.path.join(plugin_path, plugin_in_dir)
                with open(plugins_url_path, 'r') as f:
                    data = f.read()
                    url = re.findall(r'https://wordpress.org/plugins.+', data)[0]
                response = requests.get(url,timeout=60)
                picture_soup = BeautifulSoup(response.text, 'html.parser')
                try:
                    screenshots = picture_soup.find('div',class_='plugin-screenshots')
                    picture_list = screenshots.find('ul')
                    pictures = picture_list.find_all('li')
                    for picture in pictures:
                        picture_name = picture.get_text(strip=True).replace('.','')
                        src_picture = picture.find('a')['href']
                        screen_path = os.path.join(plugin_path,'Screens')
                        if not os.path.exists(screen_path):
                            os.makedirs(screen_path)
                        if not os.path.isfile(f"{screen_path}/{picture_name}.png"):
                            with open(f'{screen_path}/{picture_name}.png', 'wb') as f:
                                res = hyperlink.urlopen(src_picture, timeout=60)
                                print(src_picture)
                                f.write(res.read())
                                print(f'Picture saved successfully {picture_name}')

                        else:
                            print(f'Picture already exists {picture_name}')






                except:
                    print('Photo not found')


parse_picture()