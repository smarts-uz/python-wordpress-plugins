import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()
import os
import subprocess
import re
from dotenv import load_dotenv
load_dotenv()
src = f'{os.getenv('src_path')}/All'
src_app = f'{os.getenv('src_path')}/App'
def run_y2z():
    plugins_dirs = os.listdir(src)
    for plugins_dir in plugins_dirs:
        plugin_path = os.path.join(src, plugins_dir)
        if os.path.isdir(plugin_path):
            plugin_items_dirs = os.listdir(plugin_path)
            for plugin_item_dir in plugin_items_dirs:
                if plugin_item_dir.endswith('.url'):
                    url_file = os.path.join(plugin_path, plugin_item_dir)
                    html_name = plugin_item_dir.split('.')[0].title()
                    html_file_path = os.path.join(plugin_path, html_name)
                    with open(url_file, 'r') as f:
                        data = f.read()
                        url = re.findall(r'https://wordpress.org/plugins.+', data)[0]
                        if os.path.exists(f"{src_app}/{html_name}.txt"):
                            print(f'This html already created: {html_file_path}')
                        else:
                            pass
                            execute = subprocess.Popen(
                                [f'y2z/1_2_1/monolith.exe', f'{url}', '-o',
                                 f'{html_file_path}.html'])
                            code = execute.wait()
                            with open(f'{src_app}/{html_name}.txt', 'w') as f:
                                f.write(html_name)
                                print(f'{html_name} Plugin saved!!!!!!!!')










run_y2z()