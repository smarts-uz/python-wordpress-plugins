import subprocess
import sys

def gethtml_run(start,end):
    pros = subprocess.Popen([f'{sys.executable}', 'main.py', 'gethtml', f"--start={start}",f"--end={end}"],)
    code = pros.wait()
    return code



