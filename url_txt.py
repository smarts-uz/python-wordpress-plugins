import os
def create_url(path,name):
    try:
        if not os.path.isdir(f"{path}/{name.replace("/","")}.url"):
            with open(f'{path}/{name.replace("/", "")}.url', mode='w', encoding='utf-8') as file:
                a = '{000214A0-0000-0000-C000-000000000046}'
                str = f"""[{a}]
            Prop3=19,11
            [InternetShortcut]
            IDList=
            URL=https://wordpress.org/plugins/{name}
            IconIndex=13
            HotKey=0
            IconFile=C:\\Windows\\System32\\SHELL32.dll"""
                file.write(str)

                print(f'Created url file:{path}/{name.replace("/","")}.url')
        else:
            print(f'url file:{path}/{name.replace("/","")}.url already exists')
    except Exception as e:
        print(e)