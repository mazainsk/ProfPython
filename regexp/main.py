"""
Домашнее задание к лекции 2.2 «Regular expressions» """

import os
import csv
import re
from itertools import groupby

module_dir = os.path.dirname(os.path.abspath(__file__))

# Загрузка из файла CSV информации о клиентах.
with open(os.path.join(module_dir, 'phonebook_raw.csv'), encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# Распределение ФИО по трем первым элементам списка каждого контакта.
for contact in contacts_list[1:]:  # Нулевой элемент списка - заголовки, поэтому с 1-го.
    full_name = " ".join(contact[:3])
    full_name = [n for n in full_name.split()]
    # Длина среза должна быть равна длине списка, иначе произойдет смещение.
    contact[:len(full_name)] = full_name

# Поиск и замена формата номеров телефонов.
pattern = re.compile(r'\+?[7|8]\s?\(?(\d{3})\)?[\s|-]?(\d{3})-?'
                     r'(\d\d)-?(\d\d)\s?\(?(доб.)?\s?(\d{4})?\)?')
substr_pattern = r'+7(\1)\2-\3-\4 \5\6'
for contact in contacts_list[1:]:
    contact[5] = pattern.sub(substr_pattern, contact[5]).strip()

# Сортировка контактов по ФИО, группировка по ФИ, объединение информации.
sorted_contacts = sorted(contacts_list[1:], key=lambda x: x[:3])
contacts_list[1:] = sorted_contacts
grouped_contacts = []
for _, group in groupby(sorted_contacts, key=lambda x: x[:2]):
    group_list = list(group)
    if len(group_list) > 1:
        # Если сгруппировано больше, чем 2 контакта, то берутся только первые два.
        contact = list(map((lambda x, y: x if x == y else (x if len(x) >= len(y) else y)), *group_list[:2]))
        # print(group_list)  # Результат по "склеенным" контактам.
    else:
        # Если в группе лишь один контакт, то его нужно вынуть из вложенного списка.
        contact = group_list[0]
    grouped_contacts.append(contact)
contacts_list[1:] = grouped_contacts

# Запись нового файла в формате CSV
with open(os.path.join(module_dir, 'phonebook.csv'), "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',', lineterminator='\n')
    datawriter.writerows(contacts_list)

print('Модифицированная телефонная книга записана в файл', os.path.join(module_dir, 'phonebook.csv'))
