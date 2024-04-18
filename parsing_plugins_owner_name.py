import time

from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import re
import requests
import urllib.request as hyperlink
load_dotenv()
src = f'{os.getenv('src_path')}/All'


def owner_name():
    plugins_dirs = os.listdir(src)
    for plugin_dir in plugins_dirs[0:10]:
        plugin_path = os.path.join(src, plugin_dir)
        plugin_in_dirs = os.listdir(plugin_path)
        for plugin_in_dir in plugin_in_dirs:
            if plugin_in_dir.endswith('.url'):
                plugins_url_path = os.path.join(plugin_path, plugin_in_dir)
                try:
                    with open(plugins_url_path, 'r') as f:
                        data = f.read()
                        url = re.findall(r'https://wordpress.org/plugins.+', data)[0]
                    response = requests.get(url, timeout=60)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    owner_name_class = soup.find('span',class_='byline')
                    owner_name = soup.find('span',class_='author vcard').get_text(strip=True)
                    if owner_name != '':
                        owner_name = f'By {owner_name}'
                        owner_name_path = os.path.join(plugin_path, f"{owner_name}.txt")
                        with open(owner_name_path, 'w') as f:
                            f.write(owner_name)
                        print(f'Owner name: {owner_name} added to folder!!!!')
                except Exception as e:
                    print(e)



owner_name()