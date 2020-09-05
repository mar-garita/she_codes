import csv
import os


FILE_NAME = 'data/employees.csv'


def save_new_employee(data):
    if os.path.exists('data/employees.csv'):
        print('IF')
        with open('data/employees.csv', 'a') as f:
            writer = csv.DictWriter(
                f,
                fieldnames=['id', 'first_name', 'last_name', 'age', 'phone'],
                quoting=csv.QUOTE_MINIMAL
            )
            writer.writerow(data)

    else:
        print('ELSE')
        with open('data/employees.csv', 'w') as f:
            writer = csv.DictWriter(
                f,
                fieldnames=['id', 'first_name', 'last_name', 'age', 'phone'],
                quoting=csv.QUOTE_MINIMAL
            )
            writer.writeheader()
            writer.writerow(data)












