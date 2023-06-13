import file_operation
import Note
import ui

number = 2  # минимальное количество символов в заметке


def add():
    note = ui.create_note(number)
    array = file_operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    print("Заметка добавлена")


def show_all_notes():
    try:
        array = file_operation.read_file()
        for notes in array:
            print(Note.Note.map_note(notes))
            print("\n")
    except Exception:
        print('\nНет заметок\n')


def show_by_date():
    date = input('Введите дату в формате dd.mm.yyyy: ')
    logic = True
    array = file_operation.read_file()
    for notes in array:
        if date in Note.Note.get_date(notes):
            print(Note.Note.map_note(notes))
            print('\n')
            logic = False
    if logic == True:
        print("Заметок с такой датой не существует")


def show_by_id():
    try:
        array = file_operation.read_file()
        print('\n')
        for notes in array:
            print('id: ' + Note.Note.get_id(notes))
    except Exception:
        print('\nЗаметок с таким id не существует\n')
    id = input("Введите id заметки: ")
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            print('\n')
            print(Note.Note.map_note(notes))
            logic = False
    if logic == True:
        print("Заметок с таким id не существует")


def delete_by_id():
    show_all_notes()
    id = input("Введите id заметки: ")
    logic = True
    array = file_operation.read_file()
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            array.remove(notes)
            print("Заметка удалена")
            file_operation.write_file(array, 'a')
    if logic == True:
        print('Заметки с таким id не существует')


def edit_by_id():
    show_all_notes()
    input_from_user = input("Введите id заметки: ")
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if input_from_user == Note.Note.get_id(notes):
            note = ui.create_note(number)
            Note.Note.set_title(notes, note.get_title())
            Note.Note.set_body(notes, note.get_body())
            Note.Note.set_date(notes)
            print('Заметка изменена')
            logic = False
    if logic == True:
        print('Заметки с таким id не существует')
    file_operation.write_file(array, 'a')
