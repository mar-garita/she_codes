import csv
import datetime

from utils import check_id


FILE_NAME = 'data/entry_time.csv'


def get_attendance_report():
    id = check_id()
    with open(FILE_NAME, 'r') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            if row.get('id') == id:
                data.append(row)
    for i in data:
        print('ID: {}, DATE: {}, TIME: {}'.format(i.get('id'), i.get('date'), i.get('time')))


def get_monthly_report():
    month = int(input('Please, enter the month number: '))
    with open(FILE_NAME, 'r') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            m = int(row.get('date').split('/')[1])
            if m == month:
                print('ID: {}, DATE: {}, TIME: {}'.format(row.get('id'), row.get('date'), row.get('time')))


def get_late_employees():
    data = []
    time = datetime.time(9, 30)

    with open(FILE_NAME, 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            dic = {}

            t = row.get('time').split(':')
            list_time = list()
            list_time.append(int(t[0]))
            list_time.append(int(t[1]))

            dic['id'] = row.get('id')
            dic['date'] = row.get('date')
            dic['time'] = list_time
            data.append(dic)

    for row in data:
        time_entry = datetime.time(row.get('time')[0], row.get('time')[1])
        if time_entry > time:
            h = str(row['time'][0])
            m = str(row['time'][1])
            print('ID: {}, DATE: {}, TIME: {}:{}'.format(row.get('id'), row.get('date'), h, m))
