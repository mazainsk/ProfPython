from datetime import date

import application.salary as s  # Импорт модуля с назначением псевдонима для его имени.
from application.db.people import get_employees  # Импорт конкретной функции из модуля.

if __name__ == '__main__':
    print(date.today(), end=' ')
    s.calculate_salary()
    print(date.today(), end=' ')
    get_employees()