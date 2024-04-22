
import subprocess
def run_2(html_file_path,url):
    execute = subprocess.Popen(
        [f'y2z/1_2_1/monolith.exe', f'{url}', '-o',
         f'{html_file_path}.html'])
    code = execute.wait()
    if code !=0:
        run_2(html_file_path=html_file_path, url=url)
