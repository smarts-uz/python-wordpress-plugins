import sys

from Function.download_zip import func_download

sys.dont_write_bytecode = True
# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
import os
from django_orm.db.models import Plugin
from dotenv import load_dotenv
from bs4 import BeautifulSoup
load_dotenv()
src = f'{os.getenv('src_path')}/All'
import requests
def download():
    plugins_dirs = os.listdir(src)
    for plugins_dir in plugins_dirs:
        plugin_path = os.path.join(src, plugins_dir)
        if os.path.isdir(plugin_path):
            plugin_items_dirs = os.listdir(plugin_path)
            for plugin_item_dir in plugin_items_dirs:
                if plugin_item_dir.endswith('.html'):
                    html_file = plugin_item_dir
                    plugin = Plugin.objects.get(html=html_file)
                    html_file_path = os.path.join(plugin_path, plugin_item_dir)
                    with open(html_file_path, 'rb') as f:
                        html_body = f.read()
                    soup = BeautifulSoup(html_body, 'html.parser')
                    try:
                        container = soup.find('div', class_='plugin-actions')
                        download_url = container.find('a', class_='plugin-download button download-button button-large')['href']
                        zipfile_name = download_url.split('/')[-1]
                        response = requests.get(download_url,timeout=30, allow_redirects=False)
                        zipfile_path = os.path.join(plugin_path, 'Portable')
                        if not os.path.exists(zipfile_path):
                            os.makedirs(zipfile_path)
                            if response.status_code == 200:
                                with open(f"{zipfile_path}/{zipfile_name}", 'wb') as f:
                                    f.write(response.content)
                                    print(f'Downloaded {zipfile_name} successfully!')
                                    plugin.html = zipfile_name
                                    plugin.save()
                                    print(f'Updated zipfile name: {zipfile_name} successfully!')


                    except:
                        pass


def download_v2(start,end):
    plugins = Plugin.objects.all().order_by('pk')
    for plugin in plugins[start:end]:
        if plugin.zip == None and plugin.html != None:
            plugin_path = f'{src}/{plugin.name}'
            print(plugin_path)
            html_file_path = os.path.join(plugin_path, plugin.html)
            func_download(html_file_path, plugin)








