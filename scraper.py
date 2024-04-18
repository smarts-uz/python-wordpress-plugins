# from bs4 import BeautifulSoup
# import urllib.request as hyperlink
# import os
#
# link = hyperlink.urlopen('http://plugins.svn.wordpress.org/')
# wordPressSoup = BeautifulSoup(link,'lxml')
# filePath = os.path.dirname(os.path.realpath(__file__))
# fileNaming = (filePath + ('scrapedlist.txt'))
# print('The current working directory of the file is ' + filePath + ' the scraped list has been saved to this directory as scrapedlist.txt')
# with open('scrapedlist.txt', 'wt', encoding='utf8') as file:
#         file.write(wordPressSoup.text)

# import requests
# from bs4 import BeautifulSoup
#
#
# def get_plugin_names(url, output_file):
#         try:
#                 # Send a GET request to the provided URL
#                 response = requests.get(url)
#                 # Check if the request was successful
#                 if response.status_code > 200:
#                         # Parse the HTML content of the page
#                         soup = BeautifulSoup(response.text, 'html.parser')
#                         # Find all links to plugin pages
#                         plugin_links = soup.find_all('a', class_='plugin-icon')
#                         # Extract plugin names from the links
#                         plugin_names = [link.get('href').split('/')[-2] for link in plugin_links]
#
#                         # Write plugin names to a text file
#                         with open(output_file, 'w') as file:
#                                 for name in plugin_names:
#                                         file.write(name + '\n')
#
#                         print(f"Plugin names have been written to '{output_file}' successfully.")
#                 else:
#                         print("Failed to retrieve data. Status code:", response.status_code)
#         except Exception as e:
#                 print("An error occurred:", str(e))
#
#
# # Example usage:
# url = "http://plugins.svn.wordpress.org/"
# output_file = "plugin_names.txt"
# get_plugin_names(url, output_file)


import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def create_plugin_folders(url):
        try:
                # Send a GET request to the provided URL
                response = requests.get(url)
                # Check if the request was successful
                if response.status_code > 200:
                        # Parse the HTML content of the page
                        soup = BeautifulSoup(response.text, 'html.parser')
                        # Find all links to plugin pages
                        plugin_links = soup.find_all('a', class_='plugin-icon')

                        # Create a folder for each plugin and parse its content
                        for link in plugin_links:
                                plugin_name = link.get('href').split('/')[-2]
                                plugin_url = urljoin(url, plugin_name)
                                parse_plugin_content(plugin_name, plugin_url)

                        print("Plugin folders have been created and parsed successfully.")
                else:
                        print("Failed to retrieve data. Status code:", response.status_code)
        except Exception as e:
                print("An error occurred:", str(e))


def parse_plugin_content(plugin_name, plugin_url):
        try:
                # Send a GET request to the plugin URL
                response = requests.get(plugin_url)
                # Check if the request was successful
                if response.status_code > 200:
                        # Parse the HTML content of the page
                        soup = BeautifulSoup(response.text, 'html.parser')

                        # Create a folder for the plugin if it doesn't exist
                        folder_path = os.path.join("plugins", plugin_name)
                        if not os.path.exists(folder_path):
                                os.makedirs(folder_path)

                        # Write plugin content to a file inside the folder
                        with open(os.path.join(folder_path, "index.html"), 'w', encoding='utf-8') as file:
                                file.write(response.text)
                else:
                        print(f"Failed to retrieve data for plugin '{plugin_name}'. Status code:", response.status_code)
        except Exception as e:
                print(f"An error occurred while parsing plugin '{plugin_name}':", str(e))


# Example usage:
url = "http://plugins.svn.wordpress.org/"
create_plugin_folders(url)