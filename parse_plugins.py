from bs4 import BeautifulSoup

import urllib.request as hyperlink
import os

from url_txt import create_url


def plugins_parse():
    link = hyperlink.urlopen('http://plugins.svn.wordpress.org/')
    wordPressSoup = BeautifulSoup(link, 'html.parser')
    plugins_lists = wordPressSoup.find('ul')
    plugins = plugins_lists.find_all('li')
    for plugin in plugins[0:20]:
        plugin_name = plugin.get_text(strip=True)
        plugin_folder_name = f'All/{plugin_name.replace("/", "").replace("-"," ").title()}'
        if os.path.exists(plugin_folder_name):
            print(f'{plugin_folder_name} folder already exists')
        else:
            os.mkdir(plugin_folder_name)
            print(f'{plugin_folder_name} folder created')
            create_url(path=plugin_folder_name,name=plugin_name)


plugins_parse()