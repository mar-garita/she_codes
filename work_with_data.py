import csv
import os


FILE_NAME = 'data/employees.csv'
quoting = csv.QUOTE_MINIMAL


def save_employee(data):
    if os.path.exists('data/employees.csv'):
        with open('data/employees.csv', 'a') as f:
            writer = csv.DictWriter(
                f,
                fieldnames=['id', 'first_name', 'last_name', 'age', 'phone'],
                quoting=quoting,
            )
            writer.writerow(data)

    else:
        with open('data/employees.csv', 'w') as f:
            writer = csv.DictWriter(
                f,
                fieldnames=['id', 'first_name', 'last_name', 'age', 'phone'],
                quoting=quoting
            )
            writer.writeheader()
            writer.writerow(data)


# def make_list_data():
#     id = input('Please enter the employee ID number: ')
#     with open('data/employees.csv', 'r') as f:
#         reader = csv.DictReader(f)
#         data = []
#         for row in reader:
#             if row.get('id') != id:
#                 data.append(row)
#
#     return data


def delete_employee():
    id = input('Please enter the employee ID number: ')

    with open('data/employees.csv', 'r') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            if row.get('id') != id:
                data.append(row)

    with open('data/employees.csv', 'w') as f:
        writer = csv.DictWriter(
            f,
            fieldnames=['id', 'first_name', 'last_name', 'age', 'phone'],
            quoting=quoting
        )
        writer.writeheader()
        for employee in data:
            writer.writerow(employee)






