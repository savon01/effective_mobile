import csv
import os
from typing import List, Dict


def display_entries(entries: List[Dict[str, str]], page_size: int = 10) -> None:
    """
    Выводит записи справочника постранично.

    :param entries: Список записей справочника.
    :param page_size: Размер страницы (по умолчанию 10).
    :return: None
    """
    page = 0
    while True:
        start = page * page_size
        end = start + page_size
        page_entries = entries[start:end]

        if not page_entries:
            print("Записи закончились.")
            break

        for i, entry in enumerate(page_entries, start=1):
            print(
                f"{i}. {entry['Фамилия']} {entry['Имя']} {entry['Отчество']} - {entry['Организация']} - Рабочий: {entry['Рабочий_телефон']} - Сотовый: {entry['Сотовый_телефон']}")

        print(f"Страница {page + 1}")
        action = input(
            "Введите 'в для следующей страницы, 'н' для предыдущей страницы, или любую другую клавишу для возврата в главное меню: ")
        if action.lower() == 'в':
            page += 1
        elif action.lower() == 'н' and page > 0:
            page -= 1
        else:
            break


def add_entry(entries: List[Dict[str, str]], filename: str) -> None:
    """
    Добавляет новую запись в справочник.
    :param entries: Список записей справочника.
    :param filename: Имя файла для сохранения записей.
    :return: None
    """
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    organization = input("Введите организацию: ")
    work_phone = input("Введите рабочий телефон: ")
    mobile_phone = input("Введите сотовый телефон: ")

    entry = {
        'Фамилия': last_name,
        'Имя': first_name,
        'Отчество': middle_name,
        'Организация': organization,
        'Рабочий_телефон': work_phone,
        'Сотовый_телефон': mobile_phone
    }

    entries.append(entry)
    save_entries(entries, filename)
    print("Запись успешно добавлена.")


def edit_entry(entries: List[Dict[str, str]], filename: str) -> None:
    """
    Редактирует запись в справочнике.

    :param entries: Список записей справочника.
    :param filename: Имя файла для сохранения записей.
    :return: None
    """
    index = int(input("Введите индекс записи для редактирования: ")) - 1

    if 0 <= index < len(entries):
        entry = entries[index]
        print("Текущая запись:")
        print(
            f"{entry['Фамилия']} {entry['Имя']} {entry['Отчество']} - {entry['Организация']} - Рабочий: {entry['Рабочий_телефон']} - Сотовый: {entry['Сотовый_телефон']}")

        entry['Фамилия'] = input("Введите новую фамилию (оставьте пустым, чтобы оставить текущее): ") or entry[
            'Фамилия']
        entry['Имя'] = input("Введите новое имя (оставьте пустым, чтобы оставить текущее): ") or entry['Имя']
        entry['Отчество'] = input("Введите новое отчество (оставьте пустым, чтобы оставить текущее): ") or entry[
            'Отчество']
        entry['Организация'] = input("Введите новую организацию (оставьте пустым, чтобы оставить текущее): ") or entry[
            'Организация']
        entry['Рабочий_телефон'] = input("Введите новый рабочий телефон (оставьте пустым, чтобы оставить текущее): ") or \
                                   entry['Рабочий_телефон']
        entry['Сотовый_телефон'] = input("Введите новый сотовый телефон (оставьте пустым, чтобы оставить текущее): ") or \
                                   entry['Сотовый_телефон']

        save_entries(entries, filename)
        print("Запись успешно отредактирована.")
    else:
        print("Неверный индекс записи.")


def search_entries(entries: list) -> None:
    """
    Ищет записи в справочнике по заданным ключевым словам или значениям.

    :param entries: Список записей справочника.
    :return: None
    """
    search_criteria = input("Введите значение для поиска через запятую (например, 'Фамилия,Имя'): ").split(',')
    search_criteria = [criterion.strip() for criterion in search_criteria]

    results = []
    for entry in entries:
        if all(any(criterion.lower() in str(value).lower() for value in entry.values()) for criterion in
               search_criteria):
            results.append(entry)

    if results:
        for i, entry in enumerate(results, start=1):
            print(
                f"{i}. {entry['Фамилия']} {entry['Имя']} {entry['Отчество']} - {entry['Организация']} - Рабочий: {entry['Рабочий_телефон']} - Сотовый: {entry['Сотовый_телефон']}")
    else:
        print("Записи не найдены.")


# Функция для сохранения записей в файл
def save_entries(entries: List[Dict[str, str]], filename: str) -> None:
    """
    Сохраняет записи справочника в файл CSV.

    :param entries: Список записей справочника.
    :param filename: Имя файла для сохранения записей.
    :return: None
    """
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Фамилия', 'Имя', 'Отчество', 'Организация', 'Рабочий_телефон',
                                                  'Сотовый_телефон'])
        writer.writeheader()
        writer.writerows(entries)


def load_entries(filename: str) -> List[Dict[str, str]]:
    """
    Загружает записи справочника из файла CSV.

    :param filename: Имя файла для загрузки записей.
    :return: Список записей справочника.
    """
    if os.path.exists(filename):
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    else:
        return []
