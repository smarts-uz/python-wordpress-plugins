import os.path
import os
import requests
from bs4 import BeautifulSoup

from dotenv import load_dotenv
load_dotenv()

src = os.getenv('src_path')
def plugin_title(plugin_name):
    plugin_url = f"https://wordpress.org/plugins/{plugin_name}"
    response = requests.get(plugin_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    plugin_folder_name = soup.find('h1', class_='plugin-title').get_text(strip=True)
    if not os.path.exists(f'{src}/All/{plugin_folder_name}'):
        os.makedirs(f'{src}/All/{plugin_folder_name}')
    else:
        pass
    with open(f"{src}/All/{plugin_folder_name}/App.main", "w",encoding='utf-8') as file:
        file.write(response.text)

    return plugin_folder_name