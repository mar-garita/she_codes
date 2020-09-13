import csv
import os

from utils import check_id


FILE_NAME = 'data/employees.csv'
quoting = csv.QUOTE_MINIMAL


def save_employee(data):
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'a') as f:
            writer = csv.DictWriter(
                f,
                fieldnames=['id', 'first_name', 'last_name', 'age', 'phone'],
                quoting=quoting,
            )
            writer.writerow(data)

    else:
        with open(FILE_NAME, 'w') as f:
            writer = csv.DictWriter(
                f,
                fieldnames=['id', 'first_name', 'last_name', 'age', 'phone'],
                quoting=quoting
            )
            writer.writeheader()
            writer.writerow(data)


def add_new_employee():
    data = {}
    while True:
        try:
            id = int(input('Please enter the employee ID number: '))
            if type(id) is int:
                data['id'] = id
                break
        except ValueError:
            print("The entered data is not correct!")

    while True:
        first_name = input("Please enter the employee's first name: ")
        if first_name.isalpha():
            data['first_name'] = first_name
            break
        else:
            print("The entered data is not correct!")

    while True:
        last_name = input("Please enter the employee's last name: ")
        if last_name.isalpha():
            data['last_name'] = last_name
            break
        else:
            print("The entered data is not correct!")

    while True:
        try:
            age = int(input("Please enter the employee's age: "))
            if type(age) is int:
                data['age'] = age
                break
        except ValueError:
            print("The entered data is not correct!")

    while True:
        try:
            phone = int(input("Please enter the employee's phone number: "))
            if type(phone) is int:
                data['phone'] = phone
                break
        except ValueError:
            print('The last name must be a string!')

    choose = input("Save the new employee? (y/n): ")
    if choose == 'y':
        save_employee(data=data)


def delete_employee():
    id = check_id()

    with open(FILE_NAME, 'r') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            if row.get('id') != id:
                data.append(row)

    with open(FILE_NAME, 'w') as f:
        writer = csv.DictWriter(
            f,
            fieldnames=['id', 'first_name', 'last_name', 'age', 'phone'],
            quoting=quoting
        )
        writer.writeheader()
        for employee in data:
            writer.writerow(employee)

    print(f'Employee with ID number {id} deleted!')


