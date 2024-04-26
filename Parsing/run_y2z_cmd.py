import os
import subprocess
import time
from dotenv import load_dotenv
load_dotenv()
monolith_path = os.getenv('monolith_path')

def run_2(html_file_path,url):
    print(url)
    execute = subprocess.Popen(
        [f'{monolith_path}', f'{url}', '-o',
         f'{html_file_path}.html'])
    code = execute.wait()
    print('return code: ',code)
    return code
