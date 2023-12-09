import os

def save_to_file(phonebook, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for entry in phonebook:
            file.write(';'.join(entry) + '\n')

def load_from_file(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip().split(';') for line in file]

def add_entry(phonebook, surname, name, patronymic, phone_number):
    phonebook.append([surname, name, patronymic, phone_number])

def find_entry(phonebook, search_query):
    return [entry for entry in phonebook if search_query in entry]

def delete_entry(phonebook, search_query):
    phonebook[:] = [entry for entry in phonebook if search_query not in entry]

def print_phonebook(phonebook):
    for entry in phonebook:
        print(' '.join(entry))

# Основная программа
phonebook_filename = 'phonebook.txt'
phonebook = load_from_file(phonebook_filename)

while True:
    action = input("Введите действие (добавить, найти, показать, удалить, выход): ").lower()
    if action == 'добавить':
        surname = input("Введите фамилию: ")
        name = input("Введите имя: ")
        patronymic = input("Введите отчество: ")
        phone_number = input("Введите номер телефона: ")
        add_entry(phonebook, surname, name, patronymic, phone_number)
        save_to_file(phonebook, phonebook_filename)
    elif action == 'найти':
        search_query = input("Введите характеристику для поиска: ")
        found_entries = find_entry(phonebook, search_query)
        print_phonebook(found_entries)
    elif action == 'показать':
        print_phonebook(phonebook)
    elif action == 'удалить':
        search_query = input("Введите характеристику для удаления записи: ")
        delete_entry(phonebook, search_query)
        save_to_file(phonebook, phonebook_filename)
        print("Запись удалена.")
    elif action == 'выход':
        break
    else:
        print("Неверное действие.")
