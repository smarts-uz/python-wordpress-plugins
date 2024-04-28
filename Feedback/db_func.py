import sys


sys.dont_write_bytecode = True
# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
from django_orm.db.models import Plugin



def objects_count():
    return Plugin.objects.count()
def html_count():
    plugins_count_none = Plugin.objects.filter(html=None,name__isnull=False).count()
    plugins_count_notnone = Plugin.objects.filter(html__isnull=False, name__isnull=False).count()
    return plugins_count_none,plugins_count_notnone






def zip_count():
    zip_none = Plugin.objects.filter(zipfile=None,name__isnull=False).count()
    zip_notnone = Plugin.objects.filter(zipfile__isnull=False,name__isnull=False).count()
    return zip_none,zip_notnone



def screenshot_count():
    screen_none = Plugin.objects.filter(screenshot=False,name__isnull=False).count()
    screen_notnone = Plugin.objects.filter(screenshot=True,name__isnull=False).count()
    return screen_none,screen_notnone

def elements_count():
    elements_none = Plugin.objects.filter(elements=False, name__isnull=False).count()
    elements_notnone = Plugin.objects.filter(elements=True, name__isnull=False).count()
    return elements_none, elements_notnone


def ownername_count():
    owner_name_none = Plugin.objects.filter(owner_name=None, name__isnull=False).count()
    owner_name_notnone = Plugin.objects.filter(owner_name__isnull=False, name__isnull=False).count()
    return owner_name_none, owner_name_notnone

def unused_count():
    unused_none = Plugin.objects.filter(unused=False, name__isnull=False).count()
    unused_notnone = Plugin.objects.filter(unused=True, name__isnull=False).count()
    return unused_none, unused_notnone


def fivestars_count():
    fivestars_none = Plugin.objects.filter(fivestars=None, name__isnull=False).count()
    fivestars_notnone = Plugin.objects.filter(fivestars__isnull=False, name__isnull=False).count()
    return fivestars_none, fivestars_notnone

