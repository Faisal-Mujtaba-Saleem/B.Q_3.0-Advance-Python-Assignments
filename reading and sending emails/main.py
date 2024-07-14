import pandas as pd
import smtplib
import email
import os
import datetime
from dotenv import load_dotenv
from utils import print_centered_text

# Loading Env. Variables
load_dotenv()

# Initializing SMTP Conststants and User-Email & Password
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
USER_EMAIL = 'faisalmujtaba2005@gmail.com'
USER_PASSWORD = os.getenv('GMAIL_PASSWORD')


def send_mail(recipient, subject, content):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            # Putting SMTP Server Connection into TLS (Transport Layer Security) to secure the connection
            server.starttls()
            # Logging-in to the SMTP Server with User-Email & Password
            server.login(USER_EMAIL, USER_PASSWORD)

            # Initializing Email Message Object and setting up the required details i.e. Sender's and the Recipient's Email-Address and the Subject of the Email
            msg = email.message.EmailMessage()
            msg['From'] = USER_EMAIL
            msg['To'] = recipient
            msg['Subject'] = subject

            # Setting the main body content into Email Message
            msg.set_content(content)

            # Sending Message
            server.send_message(msg)

        return 1

    # Exception-Handling for the SMTPAuthenticationError i.e. if the SMTP Server Fails to Login with the User Account
    except smtplib.SMTPAuthenticationError as auth_error:
        print(f'Failed to send email to {recipient}:', auth_error)
        return 0

    # Exeptions-Handling for the General Exception
    except Exception as error:
        print(f'Failed to send email to {recipient}:', error)
        return 0


def today_quote():
    try:
        # Opening 'index.txt' Containing the Index of the Quote i.e. to be Send on This Monday
        with open('index.txt', 'r+') as file:
            # Reading quotes.csv where All the Motivatonal-Quote are Enlisted and Storing All these Quotes in an Array/List.
            quotes_table = pd.read_csv('quotes.csv')
            quotes = [quote['Quote'] for i, quote in quotes_table.iterrows()]

            # Extracting Index of the Quote that is to be Send from the 'index.txt' File
            index = file.read()
            index = int(index)

            # Appointing/Placing the File Writer Pointer at the 1st index (0) of the file to re-Write the Previous Content of the File i.e. Index of the Quote
            file.seek(0)

            # Incrementing the Index with Step 1 if the Index is in the Range of Quotes List
            if index < (len(quotes)-1):
                updated_index = index+1
                file.write(
                    str(updated_index)
                )

            # Else Resetting it to the Zero (0)
            else:
                file.write('0')

            # Returning Quote of a Day
            return quotes[index]

    except Exception as error:
        print('Failed to generate quote:', error)


def checkSchedule_sendQuotes():
    try:
        # Initializing the Dictionary of Weekdays
        weekdays = {
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday',
            7: 'Sunday'
        }

        # Finding the Index of the Day of Today and on Behalf of it and Extracting Today's Day from the Weeakdays Dictionary
        today_index = datetime.date.today().isoweekday()
        Today = weekdays[today_index]

        # Reading 'recipients.csv' where All the Recipients of the Motivational-Quotes are Enlisted with the Necessary Details About them i.e. the Name, Email and the Day When to Send the Email to him.
        recipients = pd.read_csv('recipients.csv')

        # Initializing the Subject & Content i.e. the Quote of the Day, of the Email to Send
        subject = 'Start Your Week with Inspiration!'
        content = today_quote()

        # Iterating Over Recipients
        for i, recipient in recipients.iterrows():
            # Extracting the Details of the Recipients
            name = recipient['name']
            email = recipient['email']
            recieve_day = recipient['recieve_day']

            # Sending Mail on Behalf of the Condition/Check i.e. if the Day Today is the Same as the Recieve-Day
            if Today == recieve_day:
                mail_sent = send_mail(email, subject, content)
                print(f'Successfully send quote via email to {name} at email-address {email}') if mail_sent else print(
                    f'Failed to send quote via email to {name} at email-address {email}')

    # Catching Any Exception Raises While Sending Quotes
    except Exception as error:
        print(error, 'in Sending Quotes')

    else:
        # Showing Success Message if All the Quotes are Delivered Successfully to The Recipients Else Showing Faliure Message.
        print('')
        if mail_sent:
            print_centered_text(
                'Successfully Send Today\'s Motivational Quotes!')
        else:
            print_centered_text('Failed to Send Today\'s Motivational Quotes!')


# Sending Quotes If the File is Running on Main Not with-in any Module
if __name__ == "__main__":
    checkSchedule_sendQuotes()
