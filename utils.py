import csv

FILE_NAME = 'data/employees.csv'
quoting = csv.QUOTE_MINIMAL


def check_id():
    with open(FILE_NAME, 'r') as f:
        reader = csv.DictReader(f)
        all_id = []
        for row in reader:
            all_id.append(row.get('id'))
    while True:
        id = input('Please enter the employee ID number: ')
        if id in all_id:
            print('ID is correct')
            break
        else:
            print('ID is not correct!')

    return id