import csv
import datetime


FILE_NAME = 'data/entry_time.csv'


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



