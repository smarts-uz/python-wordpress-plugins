from bs4 import BeautifulSoup

import urllib.request as hyperlink
import os
import requests
from dotenv import load_dotenv

from Function.plugin_func import plugin_title
from Function.url_txt import create_url

load_dotenv()

src = os.getenv('src_path')
def plugins_parse():
    link = hyperlink.urlopen('http://plugins.svn.wordpress.org/',timeout=60)
    wordPressSoup = BeautifulSoup(link, 'html.parser')
    plugins_lists = wordPressSoup.find('ul')
    plugins = plugins_lists.find_all('li')
    for plugin in plugins[0:50]:
        plugin_name_old = plugin.get_text(strip=True)
        plugin_name = plugin_title(plugin_name=plugin_name_old)
        plugin_folder_name = f'{src}/All/{plugin_name}'
        create_url(path=plugin_folder_name,name=plugin_name_old)


plugins_parse()