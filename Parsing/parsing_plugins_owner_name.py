import sys

from Function.ownername_func import func_ownername

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
src = f'{os.getenv("src_path")}/All'


def owner_name():
    plugins_dirs = os.listdir(src)
    for plugin_dir in plugins_dirs[0:20]:
        plugin_path = os.path.join(src, plugin_dir)
        plugin_in_dirs = os.listdir(plugin_path)
        check_owner = check_exists(path=plugin_path,chars='By')
        if check_owner != True:
            for plugin_in_dir in plugin_in_dirs:
                if plugin_in_dir.endswith('.url'):
                    plugins_url_path = os.path.join(plugin_path, plugin_in_dir)
                    try:
                        with open(plugins_url_path, 'r') as f:
                            data = f.read()
                            url = re.findall(r'https://wordpress.org/plugins.+', data)[0]
                        response = requests.get(url, timeout=60)
                        soup = BeautifulSoup(response.text, 'html.parser')
                        owner_name_class = soup.find('span', class_='byline')
                        owner_name = owner_name_class.find('span', class_='author vcard').get_text(strip=True)
                        if owner_name != '':
                            owner_name = f'By {owner_name}'
                            owner_name_path = os.path.join(plugin_path, f"{owner_name}.txt")
                            with open(owner_name_path, 'w') as f:
                                f.write(owner_name)
                            print(f'Owner name: {owner_name} added to folder!!!!')
                    except Exception as e:
                        print(e)
        else:
            print(f'This plugin\'s owner already added to folder!! path: {plugin_path}')




def owner_name_v2(start,end):
    plugins = Plugin.objects.all().order_by('pk')
    for plugin in plugins[start:end]:
        try:
            if plugin.owner_name == None and plugin.html != None:
                plugin_path = f"{src}/{plugin.name}"
                plugin_dirs = os.listdir(plugin_path)
                for plugin_dir in plugin_dirs:
                    if plugin_dir.lower().endswith('.html'):
                        # html_file_path = os.path.join(plugin_path, plugin.html)
                        html_file_path = os.path.join(plugin_path, plugin_dir)
                        print('owner_name', html_file_path)
                        func_ownername(html_file_path=html_file_path, plugin=plugin)
                plugin.save()
        except Exception as e:
            print(e)




