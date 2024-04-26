
import subprocess
import sys


def getdata_run(start,end):
    pros = subprocess.Popen([f'{sys.executable}', 'main.py', 'getdata', f"--start={start}", f"--end={end}"], )
    code = pros.wait()
    return code