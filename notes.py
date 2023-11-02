import argparse
import json
import os
from datetime import datetime

NOTES_FILE = "notes.json"


def get_notes():
    try:
        if os.path.exists(NOTES_FILE):
            with open(NOTES_FILE, "r", encoding = 'utf-8') as file:
                return json.load(file)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    return []


def save_notes(notes):
    try:
        with open(NOTES_FILE, "w", encoding='utf-8') as file:
            json.dump(notes, file)
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")


def add_note(title, msg):
    notes = get_notes()
    note_id = len(notes) + 1
    timestamp = str(datetime.now())
    note = {"id": note_id, "title": title, "msg": msg, "timestamp": timestamp}
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")


def list_notes(date = None):
    notes = get_notes()
    if date:
        notes = [note for note in notes if date in note["timestamp"]]
    for note in notes:
        print(
            f'ID: {note["id"]}\nЗаголовок: {note["title"]}\nСообщение: {note["msg"]}\nВремя: {note["timestamp"]}\n')


def edit_note(note_id, new_title, new_msg):
    notes = get_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = new_title
            note["msg"] = new_msg
            note["timestamp"] = str(datetime.now())
            save_notes(notes)
            print("Заметка успешно отредактирована")
            return
    print("Заметка не найдена")


def delete_note(note_id):
    notes = get_notes()
    new_notes = [note for note in notes if note["id"] != note_id]
    if len(new_notes) != len(notes):
        save_notes(new_notes)
        print("Заметка успешно удалена")
    else:
        print("Заметка не найдена")


def main():
    parser = argparse.ArgumentParser(description = "Консольное приложение заметки")
    subparsers = parser.add_subparsers(dest = "command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("-title", required=True, help = "Заголовок заметки для добавления")
    add_parser.add_argument("-msg", required=True, help = "Текст заметки")

    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("-date", help = "Фильтрация по дате")

    edit_parser = subparsers.add_parser("edit")
    edit_parser.add_argument("id", type = int, help = "ID заметки для редактирования")
    edit_parser.add_argument("-title", required = True, help="Новый заголовок заметки")
    edit_parser.add_argument("-msg", required = True, help = "Новое тело заметки")

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type = int, help = "ID заметки для удаления")

    args = parser.parse_args()

    if args.command == "add":
        add_note(args.title, args.msg)
    elif args.command == "list":
        list_notes(args.date)
    elif args.command == "edit":
        edit_note(args.id, args.title, args.msg)
    elif args.command == "delete":
        delete_note(args.id)
    else:
        parser.print_help()
        print()
        while True:
            command = input(
                '[1] - Добавить заметку\n'
                '[2] - Просмотреть все заметки\n'
                '[3] - Редактировать заметку\n'
                '[4] - Удалить заметку\n'
                '[0] - Выход\n'
                'Выберите действие: ')
            if command == "1":
                title = input("Введите заголовок заметки: ")
                msg = input("Введите текст заметки: ")
                add_note(title, msg)
            elif command == "2":
                date = input(
                    "Введите дату заметки (или нажмите Enter, чтобы пропустить): ")
                list_notes(date if date else None)
            elif command == "3":
                note_id = int(input("Введите ID заметки: "))
                title = input("Введите новый заголовок заметки: ")
                msg = input("Введите новый текст заметки: ")
                edit_note(note_id, title, msg)
            elif command == "4":
                note_id = int(input("Введите ID заметки: "))
                delete_note(note_id)
            elif command == "0":
                break
            else:
                print(f"Неизвестная команда: {command}")


if __name__ == "__main__":
    main()
