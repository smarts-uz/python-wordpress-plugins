import os
def check_exists(chars,path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith(chars) and file.endswith('.txt'):
                return True
            else:
                pass