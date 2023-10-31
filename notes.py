import argparse
from datetime import datetime


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
        pass
    elif args.command == "list":
        pass
    elif args.command == "edit":
        pass
    elif args.command == "delete":
        pass
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
                pass
            elif command == "2":
                date = input(
                    "Введите дату заметки (или нажмите Enter, чтобы пропустить): ")
                pass
            elif command == "3":
                note_id = int(input("Введите ID заметки: "))
                title = input("Введите новый заголовок заметки: ")
                msg = input("Введите новый текст заметки: ")
                pass
            elif command == "4":
                note_id = int(input("Введите ID заметки: "))
                pass
            elif command == "0":
                break
            else:
                print(f"Неизвестная команда: {command}")


if __name__ == "__main__":
    main()
