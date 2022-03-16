import csv
from datetime import datetime
import smtplib
import random

SENDER_EMAIL = 'dummyman567@gmail.com'
SENDER_PASSWORD = 'iamdummy13'


def check_birthday(birthday):
    '''Checks person's birth-date against today's-date'''
    now = datetime.now().strftime('%d-%m')
    if now == birthday:
        return True
    return False


def concat(d,m):
    '''Concats date and month into DD-MM format'''
    output = f"{d}-{m}"
    return output

def get_random_quote():
    '''Returns a random birthday wish quote'''
    with open('quotes.txt', 'r') as file:
        all_quotes = file.readlines()
        random_quote = random.choice(all_quotes)
        return random_quote


with open('birthdays.csv', newline='') as csvfile: # OPEN CSV FILE
    reader = csv.DictReader(csvfile) 
    for row in reader: # ITERATE THROUGH ALL THE RECORDS IN CSV
        person_birthday = concat(row['day'], row['month'])
        if check_birthday(person_birthday): # CHECK IF PERSON'S BIRTHDAY IS TODAY
            with smtplib.SMTP('smtp.gmail.com', port=587) as connection: # SEND THE EMAIL
                connection.starttls()
                connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
                connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=row['email'], msg=f'Subject: Happy Birthday\n\n{get_random_quote()}')
    print('All messages sent successfully')

