import utils
from employee import add_new_employee, delete_employee
from mark_attendance import mark_employee_entry
from report import get_attendance_report, get_monthly_report, get_late_employees


def main():
    while True:
        print('')
        choose = input('Please select an action: \n'
                       '1 - entry \n'
                       '2 - add a new employee \n'
                       '3 - delete a employee \n'
                       '4 - employee attendance report \n'
                       '5 - report on staff attendance for the month \n'
                       '6 - report of late employees \n'
                       '7 - exit \n'
                       '')
        print('')

        if choose == '1':
            mark_employee_entry()
        elif choose == '2':
            add_new_employee()
        elif choose == '3':
            delete_employee()
        elif choose == '4':
            get_attendance_report()
        elif choose == '5':
            get_monthly_report()
        elif choose == '6':
            get_late_employees()
        elif choose == '7':
            break
        else:
            print('INCORRECT INPUT')

    # print("ADD EMPLOYEE")
    # add_new_employee()
    #
    # print('DELETE EMPLOYEE')
    # delete_employee()
    #
    # print('MARK ENTER')
    # mark_employee_entry()

    # print('GET LIST')
    # get_attendance_report()

    # print('Get Monthly Report')
    # get_monthly_report()

    # print('report_late_employees')
    # get_late_employees()


if __name__ == '__main__':
    main()



