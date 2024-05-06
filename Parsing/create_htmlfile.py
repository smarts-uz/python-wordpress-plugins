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
    k = 0
    plugins = Plugin.objects.all().order_by('pk')
    for id,plugin in enumerate(plugins[start:end]):
        if plugin.name ==None:
            html_file_path = os.path.join(f'{src}/{plugin.name}', f'{plugin.html}')
            print(plugin.pk,html_file_path)
            text = f'{plugin.pk} {plugin.html}\r\n'
            if not os.path.exists(html_file_path):
                k+=1
                Plugin.objects.get(pk=plugin.pk).delete()
                print(f'{id} - Deleted {plugin.slug} from db')

                with open('pl.txt',mode='a',encoding='utf-8') as f:
                    f.write(text)
            print('kk',k)
    t = f'all count: {k}'
    with open('delete.txt', mode='w', encoding='utf-8') as f:
        f.write(t)
    print(f'{k} delete objects')

        # if plugin.html == None and plugin.name != None:
        #     print(f'{plugin.pk}: {plugin.name}')
        #     html_file_path = os.path.join(f'{src}/{plugin.name}', f'{plugin.name}')
        #     html_name = plugin.name
        #     print(html_name)
        #     if not os.path.exists(f"{html_file_path}.html"):
        #         return_code = run_2(html_file_path=html_file_path, url=plugin.url)
        #     else:
        #         print(f'This html already created: {html_file_path}')
        #     plugin = Plugin.objects.get(url=plugin.url)
        #     plugin.html = f'{html_name}.html'
        #     plugin.save()
        #     print(f'Updated {html_name} successfully!')






# run_y2z_v2(0,100)















