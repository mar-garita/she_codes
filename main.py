import utils
from add_employee_manually import add_new_employee
from delete_employee_manually import delete_employee
from mark_attendance import mark_employee_enter
from employee_attendance_report import get_attendance_report
from monthly_report import get_monthly_report
from report_late_employees import get_late_employees


def main():
    # print("ADD EMPLOYEE")
    # add_new_employee()
    #
    # print('DELETE EMPLOYEE')
    # delete_employee()
    #
    # print('MARK ENTER')
    # mark_employee_enter()

    # print('GET LIST')
    # get_attendance_report()

    # print('Get Monthly Report')
    # get_monthly_report()

    print('report_late_employees')
    get_late_employees()


if __name__ == '__main__':
    main()



