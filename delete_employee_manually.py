import csv
from utils import check_id


FILE_NAME = 'data/employees.csv'
quoting = csv.QUOTE_MINIMAL


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