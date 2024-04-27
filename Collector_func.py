import sys


sys.dont_write_bytecode = True
# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
from django_orm.db.models import Plugin

import time

import sys
import subprocess
def execute_run_subprocess(start,end):
    pros = subprocess.Popen([f'{sys.executable}', 'main.py', 'execute', f"--start={start}", f"--end={end}"], )
    # code = pros.wait()
    print(f'process starting: start={start}, end={end}')

def func_collector(num):
    plugins_count = Plugin.objects.count()
    print("All",plugins_count)
    every_flows_count  = plugins_count // num
    ostatok_count = plugins_count % num
    for i in range(1,num+1):
        start = i*every_flows_count
        if i == num-1:
            end = (i+1)*every_flows_count+ostatok_count
        else:
            end = (i+1)*every_flows_count
        if end > plugins_count:
            continue
        else:
            print(f'{i}: start:{start}  end:{end}')
            execute_run_subprocess(start,end)
            time.sleep(1)





