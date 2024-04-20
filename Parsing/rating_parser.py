import os
from bs4 import BeautifulSoup


def get_html_files(folder_path):
    files = os.listdir(folder_path)
    return [file for file in files if file.endswith('.html')]


def parse_html_file(html_file_path):
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, 'html.parser')
        result = soup.find(class_="ratings-list")
        rate = result.find(class_="counter-label").text.replace(" ", "-")
        count = result.find(class_="counter-count").text
        return rate, count
    except Exception as e:
        print(f"Error parsing HTML file {html_file_path}: {e}")
        return None, None


def create_txt_file(folder_path, file_name, rate, count):
    txt_file_name = f"{rate} {count}.txt"
    txt_file_path = os.path.join(folder_path, txt_file_name)
    try:
        with open(txt_file_path, 'x') as txt_file:  # 'x' mode will create the file only if it does not exist
            txt_file.write(f"Rate: {rate}\nCount: {count}")
        print(f"Text file '{txt_file_name}' created successfully.")
    except FileExistsError:
        print(f"Error: Text file '{txt_file_name}' already exists.")
    except Exception as e:
        print(f"Error creating text file {txt_file_name}: {e}")

print("hello world")

def process_folder(folder_path):
    html_files = get_html_files(folder_path)
    for html_file in html_files:
        print(html_file)
        html_file_path = os.path.join(folder_path, html_file)
        rate, count = parse_html_file(html_file_path)
        if rate is not None and count is not None:
            create_txt_file(folder_path, html_file[:-5], rate, count)
        else:
            print("Parsing failed for this file.")


def process_folders(all_folder_path):
    folders = [item for item in os.listdir(all_folder_path) if os.path.isdir(os.path.join(all_folder_path, item))]
    for folder in folders:  # Only processing a specific folder for demonstration
        folder_path = os.path.join(all_folder_path, folder)
        process_folder(folder_path)


# Example usage:
all_folder_path = "../All"
process_folders(all_folder_path)
