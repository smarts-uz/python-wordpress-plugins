
import subprocess
import sys


def getzip_run(start,end):
    pros = subprocess.Popen([f'{sys.executable}', 'main.py', 'getzip', f"--start={start}", f"--end={end}"], )
    code = pros.wait()
    return code