import sys
sys.dont_write_bytecode = True
# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
from django_orm.db.models import Plugin
import shutil
def plugin_update(plugin_url):
    plugin = Plugin.objects.get(url=plugin_url)
    plugin_path  = plugin.folder_path
    shutil.rmtree(plugin_path, ignore_errors=True)
    os.mkdir(plugin_path)
    

