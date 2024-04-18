import os
def create_url(path,name):
    try:
        if not os.path.isfile(f"{path}/{name.replace("/","")}.url"):
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


# ---------  #
import os
folder_path='d:\\Admin\\Task_Projects\\mht save\\htmls'
txt_folpath='d:\\Admin\\Task_Projects\\mht save\\App'
paths_folder=[]
paths_txt=[]

# Spliting the plugns names every varable

with open('plugins.txt',encoding='utf8') as configfile:

    for i in configfile:
        i=i.strip()

        # print(i)
        # Folder path
        path_folders=f"{folder_path}\\{i}"
        paths_folder.append(path_folders)

        # Txt path
        path_txt_file=f'{txt_folpath}\\{i}'
        paths_txt.append(path_txt_file)

# print(paths_txt)



import requests


for url in folder_path:

    check = requests.get(url)

    if check.ok:
        print('have a url')
        for t in paths_txt:
            if not os.path.exists(t):
                put = f"{t}.txt"
                open(put, "x")
            else:
                print(f"{t}:Folder already exists!!!")


# Check if the folder already exists
for f in paths_folder:

    if not os.path.exists(f):
        # Create the folder
        os.makedirs(f)
        print(f"{f}:Folder created successfully.")
    else:
        print(f"{f}:Folder already exists.")



#         cheking in located App main folder if sucses procses create txt file else not sucsesed procses  none!!!




for f in paths_folder:
    if  os.listdir(f):
        print(f"{f}:Directory is not empty")
        for t in paths_txt:
            if not os.path.exists(t):
                put=f"{t}.txt"
                open(put, "x")
            else:
                print(f"{t}:Folder already exists!!!")
    elif not os.listdir(f):
        print("Directory is empty")
