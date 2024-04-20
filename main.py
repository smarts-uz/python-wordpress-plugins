############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()

from Parsing.parse_plugins import plugins_parse
# Import your models for use in your script
import click


@click.group('Plugin')
def plugin():
    pass

@plugin.command(help='Parsing plugins name from https://ps.w.org/')
def parse():
    plugins_parse()



try:
    if __name__ == '__main__':
        plugin()
except Exception as e:
    print(e)