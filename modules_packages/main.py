"""
Домашнее задание к лекции 1. «Import. Module. Package» """

from datetime import date

import application.salary as s
from application.db.people import get_employees

if __name__ == '__main__':
    print(date.today(), end=' ')
    s.calculate_salary()
    print(date.today(), end=' ')
    get_employees()
