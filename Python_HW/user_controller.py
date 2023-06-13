import function
import ui


def run():
    input_from_user = ''
    while input_from_user != '0':
        ui.menu()
        input_from_user = input().strip()
        if input_from_user == '1':
            function.show_all_notes()
        if input_from_user == '2':
            function.add()
        if input_from_user == '3':
            function.edit_by_id()
        if input_from_user == '4':
            function.show_by_date()
        if input_from_user == '5':
            function.show_by_id()
        if input_from_user == '6':
            function.delete_by_id()
        if input_from_user == '0':
            ui.exit()
            break
