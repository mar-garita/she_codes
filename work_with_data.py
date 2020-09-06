import csv
import os


FILE_NAME = 'data/employees.csv'


def save_new_employee(data):
    if os.path.exists('data/employees.csv'):
        with open('data/employees.csv', 'a') as f:
            writer = csv.DictWriter(
                f,
                fieldnames=['id', 'first_name', 'last_name', 'age', 'phone'],
                quoting=csv.QUOTE_MINIMAL
            )
            writer.writerow(data)

    else:
        with open('data/employees.csv', 'w') as f:
            writer = csv.DictWriter(
                f,
                fieldnames=['id', 'first_name', 'last_name', 'age', 'phone'],
                quoting=csv.QUOTE_MINIMAL
            )
            writer.writeheader()
            writer.writerow(data)


def delete_employee():
    with open('data/employees.csv', 'r') as f:
        reader = csv.DictReader(f)
        while True:
            id = input('Please enter the employee ID number: ')
            for row in reader:
                if row['id'] == id:
                    input('Delete an employee of {} {}? (y/n) '.format(row['first_name'], row['last_name']))
            break
                # else:
                #     print('else')










