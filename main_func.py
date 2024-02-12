from phonebook import load_entries, display_entries, add_entry, edit_entry, search_entries


def main():
    filename = 'phonebook.csv'
    entries = load_entries(filename)

    while True:
        print("\nМеню телефонного справочника:")
        print("1. Вывести записи")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Найти записи")
        print("5. Выйти")

        choice = input("Введите ваш выбор: ")

        if choice == '1':
            display_entries(entries)
        elif choice == '2':
            add_entry(entries, filename)
        elif choice == '3':
            edit_entry(entries, filename)
        elif choice == '4':
            search_entries(entries)
        elif choice == '5':
            print("Выход из телефонного справочника. До свидания!!!")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")
