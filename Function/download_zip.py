import sys
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
src_app = f'{os.getenv('src_path')}/App'
import requests


def func_download(html_file_path,plugin):
    with open(html_file_path, 'rb') as f:
        html_body = f.read()
    soup = BeautifulSoup(html_body, 'html.parser')
    try:
        container = soup.find('div', class_='plugin-actions')
        download_url = container.find('a', class_='plugin-download button download-button button-large')['href']
        zipfile_name = download_url.split('/')[-1]
        response = requests.get(download_url, timeout=30, allow_redirects=False)
        zipfile_path = os.path.join(plugin.folder_path, 'Portable')
        if not os.path.exists(zipfile_path):
            os.makedirs(zipfile_path)
        if response.status_code == 200:
            if not os.path.exists(f"{zipfile_path}/{zipfile_name}"):
                with open(f"{zipfile_path}/{zipfile_name}", 'wb') as f:
                    f.write(response.content)
                    print(f'Downloaded {zipfile_name} successfully!')
            plugin.zipfile = zipfile_name
            plugin.save()
            print(f'Updated zipfile name: {zipfile_name} successfully!')



    except:
        pass
