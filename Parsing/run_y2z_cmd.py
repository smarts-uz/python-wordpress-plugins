
import subprocess
import time


def run_2(html_file_path,url):
    print(url)
    execute = subprocess.Popen(
        [f'C:/Users/Administrator/Desktop/Learning Parser/python-wordpress-plugins/Parsing/monolith.exe', f'{url}', '-o',
         f'{html_file_path}.html'])
    code = execute.wait()
    print('return code: ',code)
    return code
