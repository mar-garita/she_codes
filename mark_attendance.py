import datetime
import os
import csv

from utils import check_id

FILE_NAME = 'data/entry_time.csv'
quoting = csv.QUOTE_MINIMAL


def save_time_entry(data):
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'a') as f:
            writer = csv.DictWriter(
                f,
                fieldnames=['id', 'date', 'time'],
                quoting=quoting,
            )
            writer.writerow(data)

    else:
        with open(FILE_NAME, 'w') as f:
            writer = csv.DictWriter(
                f,
                fieldnames=['id', 'date', 'time'],
                quoting=quoting
            )
            writer.writeheader()
            writer.writerow(data)


def mark_employee_entry():
    data = {'id': check_id()}
    time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M").split(' ')
    data['date'] = time[0]
    data['time'] = time[1]
    save_time_entry(data)
    print(time[1])
    print('DONE!')


