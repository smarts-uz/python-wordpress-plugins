import sys

from Function.unused_func import func_unused

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


def plugin_desc():
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
                response = requests.get(url, timeout=60)
                soup = BeautifulSoup(response.text, 'html.parser')
                description_1 = soup.find('div', id="tab-description",class_='plugin-description section')
                try:
                    description = description_1.find('div', class_='plugin-notice notice notice-error notice-alt').get_text(strip=True)
                    if description !=  None:
                        description_path = f'{description.replace("  ", " ")}.txt'
                        plugin_desc_path = os.path.join(plugin_path, description_path)
                        if not os.path.isfile(plugin_desc_path):
                            with open(plugin_desc_path, 'w') as f:
                                f.write(description)
                            print(f'{plugin_desc_path} has been created txt file')
                        else:
                            print(f'{plugin_desc_path} already exists')


                except:
                    pass





def unused_plugin():
    plugins = Plugin.objects.filter(unused=False)
    for plugin in plugins:
        plugin_path = plugin.folder_path
        if plugin.html != None:
            html_file_path = os.path.join(plugin.folder_path, plugin.html)
            func_unused(html_file_path, plugin)
            plugin.save()
            # with open(html_file_path, 'rb') as f:
            #     html_body = f.read()
            # soup = BeautifulSoup(html_body, 'html.parser')
            # try:
            #     description_1 = soup.find('div', id="tab-description", class_='plugin-description section')
            #     description = description_1.find('div', class_='plugin-notice notice notice-error notice-alt').get_text(
            #         strip=True)
            #     if description != None:
            #         description_path = f'{description.replace("  ", " ")}.txt'
            #         plugin_desc_path = os.path.join(plugin_path, description_path)
            #         if not os.path.isfile(plugin_desc_path):
            #             with open(plugin_desc_path, 'w') as f:
            #                 f.write(description)
            #             print(f'{plugin_desc_path} has been created txt file')
            #         else:
            #             print(f'{plugin_desc_path} already exists')
            #     plugin.unused = True
            #     plugin.save()
            # except:
            #      pass



