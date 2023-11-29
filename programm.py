import json

# Функция для чтения списка заметок из файла
def read_notes_file(file_name):
    with open(file_name, 'r') as f:
        notes = json.load(f)
    return notes

def main():
    file_name = 'notes.json'
    notes = read_notes_file(file_name)
    while True:
        print('Выберите действие:')
        print('1. Вывести все заметки')
        print('2. Вывести заметки за определенную дату')
        print('3. Вывести конкретную заметку')
        print('4. Добавить новую заметку')
        print('5. Редактировать заметку')
        print('6. Удалить заметку')
        print('7. Выход')
        choice = input('Ваш выбор: ')
        if choice == '1':
            print(notes)
        elif choice == '7':
            break

        else:
            print('Недопустимый выбор')

main()