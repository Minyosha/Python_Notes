import Note


def create_note(number):
    title = check_len_text_input(
        input('Введите Название заметки: '), number)
    body = check_len_text_input(
        input('Введите Описание заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print(
        "\nЗаметки. Выберите действие:\n\n1 - Вывод всех заметок из файла\n2 - Добавление заметки\n3 - Редактирование заметки\n4 - Показать заметки по дате\n5 - Показать заметку по id\n6 - Удалить заметку по id\n0 - Выход\n\nВведите номер функции: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def exit():
    print("Завершение работы программы")
