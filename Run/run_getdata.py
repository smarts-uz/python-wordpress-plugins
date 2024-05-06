
import subprocess
import sys


def getdata_run(start,end):
    print('run getdata')
    pros = subprocess.Popen([f'{sys.executable}', 'main.py', 'getdata', f"--start={start}", f"--end={end}"], )
    code = pros.wait()
    return code



def getscreen_run(start,end):
    pros = subprocess.Popen([f'{sys.executable}', 'main.py', 'getscreen', f"--start={start}", f"--end={end}"], )
    code = pros.wait()
    return code


def getrating_run(start,end):

    pros = subprocess.Popen([f'{sys.executable}', 'main.py', 'getrating', f"--start={start}", f"--end={end}"], )
    code = pros.wait()
    return code


def getelements_run(start,end):
    pros = subprocess.Popen([f'{sys.executable}', 'main.py', 'getelements', f"--start={start}", f"--end={end}"], )
    code = pros.wait()
    return code

def getowner_run(start,end):

    pros = subprocess.Popen([f'{sys.executable}', 'main.py', 'getowner-name', f"--start={start}", f"--end={end}"], )
    code = pros.wait()
    return code

def getunused_run(start,end):

    pros = subprocess.Popen([f'{sys.executable}', 'main.py', 'getunused', f"--start={start}", f"--end={end}"], )
    code = pros.wait()
    return code