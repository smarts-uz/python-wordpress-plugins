import sys
sys.dont_write_bytecode = True
# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
import os
from django_orm.db.models import Plugin
from dotenv import load_dotenv
from bs4 import BeautifulSoup
load_dotenv()
src = f'{os.getenv('src_path')}/All'



def func_rating(html_file_path,plugin):
    with open(html_file_path, 'rb') as f:
        html_body = f.read()
    soup = BeautifulSoup(html_body, 'html.parser')
    try:
        rating_container = soup.find('div', class_='widget plugin-ratings')
        ratings_lists = rating_container.find('ul', class_='ratings-list')
        rating_lists = ratings_lists.find_all('li')
        for rating_list in rating_lists[0:1]:
            fives_count = rating_list.find('span', class_='counter-count').get_text(strip=True)
            fivesstart_txt = os.path.join(f'{src}/{plugin.name}', f'5 starts - {fives_count}.txt')
            if not os.path.exists(fivesstart_txt):
                with open(fivesstart_txt, mode='w', encoding='utf-8') as f:
                    f.write(f'5 starts - {fives_count}')
                print(f'Created txt file {fivesstart_txt}')
            plugin.fivestars = int(fives_count)
            plugin.save()
    except Exception as e:
        pass