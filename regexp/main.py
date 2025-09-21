"""
Домашнее задание к лекции 2.2 «Regular expressions» """

import csv
import re
from itertools import groupby


def list_union(input_list: list) -> list:
    """
    Функция поэлементно сравнивает вложенные списки и формирует один общий список таким образом,
    что из одинаковых по значению элементов берется первый, а из разных - тот, что длиннее
    (при одинаковой длине предпочитается элемент первого списка).
    :param: group - список из двух списков с одинаковым кол-вом элементов:
    :return: Одноуровневый список из объединенных элементов.
    """
    grouped_data = []
    if len(input_list) == 1:
        grouped_data.append(input_list[0])
    else:
        element_list = []
        for i in zip(*input_list):
            if i[0] != i[1]:
                if len(i[0]) < len(i[1]):
                    element_list.append(i[1])
                    continue
            element_list.append(i[0])
        grouped_data.append(element_list)
    return grouped_data

# Загрузка из файла CSV информации о клиентах.
with open("phonebook_raw.csv", encoding="utf-8") as f:
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
    grouped_contacts.append(*list_union(list(group)))
contacts_list[1:] = grouped_contacts

# Запись нового файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',', lineterminator='\n')
    datawriter.writerows(contacts_list)

print('Модифицированная телефонная книга записана в файл "phonebook.csv"')
