import notes

def create_note():
    note_id = input("Введите идентификатор заметки: ")
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    note = notes.create_note(note_id, title, body)
    notes.save_note(note, 'notes.csv')
    print("Заметка успешно создана.")

def read_notes():
    notes_list = notes.read_notes('notes.csv')
    if not notes_list:
        print("Список заметок пуст.")
    else:
        for note in notes_list:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Дата/время: {note['timestamp']}")
            print("--------------------------------")

def edit_note():
    note_id = input("Введите идентификатор заметки для редактирования: ")
    title = input("Введите новый заголовок заметки: ")
    body = input("Введите новый текст заметки: ")
    notes.edit_note(note_id, title, body, 'notes.csv')
    print("Заметка успешно отредактирована.")

def delete_note():
    note_id = input("Введите идентификатор заметки для удаления: ")
    notes.delete_note(note_id, 'notes.csv')
    print("Заметка успешно удалена.")

def main():
    while True:
        print("1. Создать заметку")
        print("2. Показать список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            create_note()
        elif choice == '2':
            read_notes()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Попробуйте ещё раз.")

if __name__ == '__main__':
    main()