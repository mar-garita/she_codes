import csv

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
