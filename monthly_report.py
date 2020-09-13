import csv

FILE_NAME = 'data/entry_time.csv'


def get_monthly_report():
    month = int(input('Please, enter the month number: '))
    with open(FILE_NAME, 'r') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            m = int(row.get('date').split('/')[1])
            if m == month:
                print('ID: {}, DATE: {}, TIME: {}'.format(row.get('id'), row.get('date'), row.get('time')))

