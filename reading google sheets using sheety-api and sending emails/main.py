# import requests
import json
import smtplib
from email.message import EmailMessage
# import pywhatkit as kit
import pyautogui
from dotenv import load_dotenv
import os
import time
from datetime import datetime
from typing import List, Dict

load_dotenv()

sheet_url = os.getenv('SHEET_URL')

CLINIC_NAME = 'The Cupping Therapy Clinic'
CONTACT_NUMBER = '03308479616'
DATE_NOW = datetime.now()


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
PASSWORD = os.getenv('APP_KEY')
SUBJECT = 'Cupping Therapy Dates Notification For This Month'
FROM = 'faisalmujtaba2005@gmail.com'


def fetch_clients_from_sheet(url):
    try:
        # res = requests.get(url)
        # print(res.text)
        # sheet = res.json()
        # return sheet["clients"]

        # To preserve maximum api calls!
        file_path = 'C:/Users/Faisal/OneDrive/Desktop/code playground/B.Q_3.0 Advance Python Assignments/reading google sheets using sheety-api and sending emails/sample_sheety_response.json'

        with open(file=file_path, mode='r') as file:
            return json.load(file)['clients']

    except Exception as e:
        print(f'Failed to fetch clients from the google sheet, {e}')


# Failed Experiment!
# def send_whatsapp_message(to_phoneNumber, reciver_name, message):
#     try:
#         kit.sendwhatmsg_instantly(to_phoneNumber, message)
#         time.sleep(20)
#         pyautogui.press('enter')

#         print(f'Successfully send message to, {
#               reciver_name} at whatsapp with number {to_phoneNumber}')
#     except Exception as e:
#         print(f'Failed to send message to, {
#               reciver_name} at whatsapp with number {to_phoneNumber}, {e}')


def send_monthly_whatsapp_n_email_messages_to_clients():
    clients: List[Dict[str]] = fetch_clients_from_sheet(sheet_url=sheet_url)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        if isinstance(DATE_NOW.day, int) and DATE_NOW.day == 1:
            # if isinstance(DATE_NOW.day, int):
            server.starttls()
            server.login(FROM, PASSWORD)

            sunnah_dates_list = []
            for client in clients:
                client_name = client['name']
                client_email = client['email']
                # client_whatsapp = client['whatsapp']

                # This method is preferred for its simplicity when you have a fixed and known number of keys to combine in a dictionary. It allows for quick and clear formatting of specific values, such as the sunnah dates!
                sunnah_dates = f'{client['sunnahDate1']}, {
                    client['sunnahDate2']}, {client['sunnahDate3']}'

                # If you dont actually know how many keys you have to join then this way is best!
                for key, value in client.items():
                    if 'sunnahDate' in key:
                        sunnah_dates_list.append(value)
                sunnah_dates = ', '.join(sunnah_dates)

                if client_email != '':
                    message = EmailMessage()

                    message['Subject'] = SUBJECT
                    message['From'] = FROM
                    message['To'] = client_email

                    TEXT = f"""
                    Hi {client_name},

                    Assalam u Alaikum,

                    We hope you're doing well. We wanted to inform you about the cupping therapy dates for this month.

                    Cupping therapy is a traditional practice that involves creating a vacuum on the skin to draw out blood and promote healing. It has been used for centuries to reduce inflammation and improve circulation.

                    This month, the recommended dates for cupping therapy are {sunnah_dates}. We believe these dates will be most beneficial for your well-being.

                    If you'd like to schedule an appointment, please contact us at your earliest convenience. For any concerns,
                    please reach
                    out to us at {CONTACT_NUMBER}. We are here to support your health and wellness.

                    Thank you for choosing our clinic. We appreciate your attention and hope to see you soon.

                    Best regards,
                    {CLINIC_NAME}
                    """

                    # I write it by my self but the text content is from Chat-GPT!
                    HTML = f"""
                    <html lang="en">

                        <body>
                            <h1>
                                <u>
                                    {SUBJECT}
                                </u>
                            </h1>

                            <p>
                                Hi <b>{client_name}</b>,
                            </p>

                            <p>
                                <i>Assalam u Alaikum</i>,
                            </p>

                            <p>
                                We hope this message finds you well.
                            </p>

                            <h2>
                                <u>
                                    Recommended Cupping Therapy Dates
                                </u>
                            </h2>

                            <p>
                                We would like to inform you about this month's recommended cupping therapy dates: {sunnah_dates}. Cupping
                                therapy is a
                                time-tested practice that helps reduce inflammation and improve circulation by creating a vacuum on the skin.
                            </p>

                            <h2>
                                <u>
                                    Schedule an Appointment
                                </u>
                            </h2>

                            <p>
                            If you'd like to schedule an appointment, please contact us at your earliest convenience. For any concerns,
                            please reach
                            out to us at {CONTACT_NUMBER}. We are here to support your health and wellness.

                Thank you for choosing our clinic. We look forward to seeing you soon.
                            </p>

                            <strong>Best regards,</strong>
                            <br>
                            <i>{CLINIC_NAME}</i>
                        </body>

                    </html>
        """

                    message.set_content(TEXT)
                    message.add_alternative(HTML)

                    server.send_message(msg=message)

                    print(f'Successfully sent email to {client_name}!')

                else:
                    print(f'No email address found for {client_name}!')

                # send_whatsapp_message(client_whatsapp, client_name, TEXT)

        server.quit()


if __name__ == "__main__":
    try:
        send_monthly_whatsapp_n_email_messages_to_clients()
    except Exception as e:
        print('Failed to send email to clients,', e)
