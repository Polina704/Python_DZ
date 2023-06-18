# Задача 38: 
# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

# Показывает информацию в файле
def show_data(filename):
    print("\nПП | Имя | Фамилия | Телефон")
    with open(filename, "r", encoding="utf-8") as data:
        print(data.read())
    print("")
    input('\nPress any key')

# Добавить контакт в файл
def add_data(filename):
    with open(filename, "r", encoding="utf-8") as data:
        tel_file = data.read()
    num = len(tel_file.split("\n"))
    with open(filename, "a", encoding="utf-8") as data: 
        surname = input("Введите фамилию: ")
        name = input("Введите имя: ")
        phone_number = input("Введите номер телефона: ")
        data.write(f"{num} | {surname} | {name} | {phone_number}\n")
        print(f"Добавлена запись : {num} | {surname} | {name} | {phone_number}\n")

    input('\nPress any key')

# Изменить контакт в файле
def edit_data(filename):
    print("\nПП | Имя | Фамилия | Телефон")
    with open(filename, "r", encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(" | ")
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    num = elements[0]
    if len(surname) == 0:
        surname = elements[1]
    if len(name) == 0:
        name = elements[2]
    if len(phone) == 0:
        phone = elements[3]
    edited_line = f"{num} | {surname} | {name} | {phone}"
    tel_book_lines[index_delete_data] = edited_line
    print(f"Запись - {edit_tel_book_lines}, изменена на - {edited_line}\n")
    with open(filename, "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))

    input('\nPress any key')

# Удалить контакт из файла
def delete_data(filename):
    print("\nПП | Имя | Фамилия | Телефон")
    with open(filename, "r", encoding="utf-8") as data:
        tel_book = data.read()
        print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    tel_book_lines = tel_book.split("\n")
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f"Удалена запись: {del_tel_book_lines}\n")
    with open(filename, "w", encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))

    input('\nPress any key')

def main(filename):
    my_choice = -1
    file_tel = "test.txt"

    # Создает файл если его нет в папке
    with open(file_tel, "a", encoding="utf-8") as file:
         file.write("")

    while my_choice != 0:
        print("Выберите одно из действий:")
        print("1 - Вывести инфо на экран")
        print("2 - Добавить контакт")
        print("3 - Изменить контакт")
        print("4 - Удалить контакт")
        print("0 - Выход из программы")
        action = int(input("Действие: "))
        if action == 1:
            show_data(file_tel)
        elif action == 2:
            add_data(file_tel)
        elif action == 3:
            edit_data(file_tel)
        elif action == 4:
            delete_data(file_tel)
        else:
            my_choice = 0

    print("До свидания")

main('test.txt')