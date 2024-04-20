import time

from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import re
import requests
import urllib.request as hyperlink
load_dotenv()
src = f'{os.getenv('src_path')}/All'

def plugins_elements():
    plugins_dirs = os.listdir(src)
    for plugin_dir in plugins_dirs:
        plugin_path = os.path.join(src, plugin_dir)
        plugin_in_dirs = os.listdir(plugin_path)
        if 'Readme.txt' in plugin_in_dirs:
            print('This plugin elements already parsed!!')
        else:
            for plugin_in_dir in plugin_in_dirs:
                if plugin_in_dir.endswith('.url'):
                    plugins_url_path = os.path.join(plugin_path, plugin_in_dir)
                    try:
                        with open(plugins_url_path, 'r') as f:
                            data = f.read()
                            url = re.findall(r'https://wordpress.org/plugins.+', data)[0]
                        response = requests.get(url, timeout=60)
                        soup = BeautifulSoup(response.text, 'html.parser')
                        try:
                            plugins_info_class = soup.find('div', class_='widget plugin-meta').find('ul').find_all('li')
                            for plugin in plugins_info_class:
                                if plugin('div', class_='tags'):
                                    tags = plugin.find('div', class_='tags').find_all('a')
                                    for tag in tags:
                                        tag_path = os.path.join(plugin_path, f'#{tag.text}.txt')
                                        if not os.path.isfile(tag_path):
                                            with open(tag_path, 'w') as f:
                                                f.write(tag.text)
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
                                        plugin_text_path = os.path.join(plugin_path, f'{plugin_text}.txt')

                                        if not os.path.isfile(plugin_text_path):
                                            with open(plugin_text_path, 'w') as f:
                                                f.write(plugin_text)
                                                print(f'Created txt file {plugin_text_path}')
                                        else:
                                            print(f'File {plugin_text_path} already exists')
                            readme_txt_path = os.path.join(plugin_path, f'Readme.txt')
                            if not os.path.isfile(readme_txt_path):
                                with open(readme_txt_path, 'w') as f:
                                    f.write('Parsed!!!')
                        except:
                            pass
                    except Exception as e:
                        print(e)










plugins_elements()