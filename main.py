import csv
from datetime import datetime
import smtplib
import random

SENDER_EMAIL = '' # YOUR EMAIL HERE
SENDER_PASSWORD = '' # YOUR PASSWORD HERE


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

def main():
    with open('birthdays.csv', newline='') as csvfile: # OPEN CSV FILE
        persons = []
        reader = csv.DictReader(csvfile) 
        for row in reader: # ITERATE THROUGH ALL THE RECORDS IN CSV
            person_birthday = concat(row['day'], row['month'])
            if check_birthday(person_birthday): # CHECK IF PERSON'S BIRTHDAY IS TODAY
                person_name = row['name']
                persons.append(person_name)
                with smtplib.SMTP('smtp.gmail.com', port=587) as connection: # SEND THE EMAIL
                    connection.starttls()
                    connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
                    connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=row['email'], msg=f'Subject: Happy Birthday {person_name}\n\n{get_random_quote()}')
        if len(persons) >= 1:
            for i in persons:
                print(f'Successfully sent message to: {i}')
        else:
            print('No one in the \'birthdays.csv\' has birthday today!')


main()

