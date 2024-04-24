
import subprocess
def run_2(html_file_path,url):
    execute = subprocess.Popen(
        [f'C:/Users/Administrator/Desktop/Learning Parser/python-wordpress-plugins/Parsing/monolith.exe', f'{url}', '-o',
         f'{html_file_path}.html'],shell=True)
    code = execute.wait()
    if code !=0:
        run_2(html_file_path=html_file_path, url=url)
