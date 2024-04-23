############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys

from Update.update_plugin import plugin_update

sys.dont_write_bytecode = True
# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
from django_orm.db.models import Plugin
from Parsing.parse_plugins import plugins_parse
from Parsing.create_htmlfile import run_y2z_v2
from Parsing.download_zip_file import download_v2
from Parsing.parser_plugins_elements import plugins_elements_v2
from Parsing.parsing_plugins_owner_name import owner_name_v2
from Parsing.plugin_description import unused_plugin
from Parsing.rating import get_rating
from Parsing.save_picture import parse_picture_v2
import datetime
# Import your models for use in your script
import click


@click.group('Plugin')
def plugin():
    pass

@plugin.command(help='Parsing plugins name from https://ps.w.org/')
@click.option('--start')
@click.option('--end')
def parse(start,end):
    plugins_parse(start,end)





@plugin.command(help='Create asset file for plugins')
def create_asset():
    run_y2z_v2()
    parse_picture_v2()
    get_rating()
    download_v2()
    plugins_elements_v2()
    owner_name_v2()
    unused_plugin()


@plugin.command(help='Delete or update plugin')
@click.argument('plugin_url')
def update(plugin_url):
    plugin_update(plugin_url=plugin_url)
    plugin = Plugin.objects.get(url=plugin_url)
    plugin.last_updated = datetime.datetime.now()
    plugin.save()
    print('Plugin\'s data  updated')




try:
    if __name__ == '__main__':
        plugin()
except Exception as e:
    print(e)