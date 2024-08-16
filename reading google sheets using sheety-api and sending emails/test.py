# import pywhatkit as kit
# import pyautogui
# import time
from datetime import datetime
import json

# date_now = datetime.now()
# print(date_now.strftime('%d/%m/%Y'))

date_now = datetime.now()
print(type(date_now.day))

print('i' in 'inner')
print(', '.join(['16/08/2024', '16/08/2024', '16/08/2024']))

print(', '.join(['21/08/2024', '23/08/2024', '25/08/2024',
                 '21/08/2024', '23/08/2024', '25/08/2024']))

# with open('C:/Users/Faisal/OneDrive/Desktop/code playground/B.Q_3.0 Advance Python Assignments/reading google sheets using sheety-api and sending emails/sample_sheety_response.json', 'r') as file:
#     # print(file.read())
#     print(json.load(file))

# kit.sendwhatmsg_instantly('+923308479616', 'hi')
# time.sleep(10)
# pyautogui.press('enter')
