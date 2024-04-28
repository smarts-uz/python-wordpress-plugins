import os
import time
import telebot
from dotenv import load_dotenv

from Feedback.db_func import objects_count,html_count,zip_count,screenshot_count,elements_count,ownername_count,unused_count,fivestars_count

load_dotenv()
token = os.getenv('token')
chat_id = os.getenv('channel_id')
secund =os.getenv('secund')
bot = telebot.TeleBot(token)



def send_report():
    while True:
        all_count = objects_count()
        html = html_count()
        html_none = html[0]
        html_notnone = html[1]
        zip = zip_count()
        zip_none = zip[0]
        zip_notnone = zip[1]
        screenshot = screenshot_count()
        screenshot_none = screenshot[0]
        screenshot_notnone = screenshot[1]
        elements = elements_count()
        elements_none = elements[0]
        elements_notnone = elements[1]
        ownername = ownername_count()
        ownername_none = ownername[0]
        ownername_notnone = ownername[1]
        fivestars = fivestars_count()
        fivestars_none = fivestars[0]
        fivestars_notnone = fivestars[1]
        unused = unused_count()
        unused_none = unused[0]
        unused_notnone = unused[1]
        text = f"""All: {all_count}
        
html: none: {html_none} | notnone: {html_notnone}

zip: none: {zip_none} | notnone: {zip_notnone}

screenshot: none: {screenshot_none} | notnone: {screenshot_notnone}

elements: none: {elements_none} | notnone: {elements_notnone}

ownername: none: {ownername_none} | notnone: {ownername_notnone}

fivestart: none: {fivestars_none} | none: {fivestars_notnone}

unused: none: {unused_none} | none: {unused_notnone}
        """
        try:
            bot.send_message(chat_id=chat_id,text=text)
        except Exception as e:
            print(e)
            time.sleep(5)
            bot.send_message(chat_id=chat_id,text=e)
            time.sleep(5)
            bot.send_message(chat_id=chat_id,text=text)
        for i in range(int(secund)):
            print(i)
            time.sleep(1)
        print("Feedback succesfully sent")







