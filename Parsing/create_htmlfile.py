import sys
sys.dont_write_bytecode = True
# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
from django_orm.db.models import Plugin
import os
import subprocess
from Parsing.run_y2z_cmd import run_2

import re
import time
from dotenv import load_dotenv
load_dotenv()
src = f'{os.getenv('src_path')}/All'



def run_y2z_v2(start,end):
    plugins = Plugin.objects.filter(html=None).order_by('pk')
    for plugin in plugins[start:end]:
        if plugin.name != None:
            html_file_path = os.path.join(f'{src}/{plugin.name}', f'{plugin.name}')
            html_name = plugin.name
            print(html_name)
            if not os.path.exists(f"{html_file_path}.html"):
                return_code = run_2(html_file_path=html_file_path, url=plugin.url)
            else:
                print(f'This html already created: {html_file_path}')
            plugin = Plugin.objects.get(url=plugin.url)
            plugin.html = f'{html_name}.html'
            plugin.save()
            print(f'Updated {html_name} successfully!')



















