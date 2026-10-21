tasks = []


def add_task(task):
    if not task.strip():
        print("Нельзя добавить пустую задачу!")
        return

    tasks.append({
        "name": task,
        "done": False
    })
    print("Задача успешно добавлена!")


def clear_tasks():
    if not tasks:
        print("Список задач уже пуст!")
        return

    confirm = input("Удалить все задачи? (да/нет): ")

    if confirm.lower() == "да":
        tasks.clear()
        print("Все задачи удалены!")
    else:
        print("Удаление отменено!")


def show_tasks():
    if not tasks:
        print("Список задач пуст!")
        return

    print("\n--- СПИСОК ЗАДАЧ ---")

    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['name']}")


def delete_task(number):
    if not tasks:
        print("Список задач пуст!")
        return

    if 1 <= number <= len(tasks):
        removed = tasks.pop(number - 1)
        print(f"Удаление завершено: {removed['name']}")
        print(f"Осталось задач: {len(tasks)}")
    else:
        print("Ошибка! Задачи с таким номером нет.")

def complete_task(number):
    if 1 <= number <= len(tasks):
        tasks[number - 1]["done"] = True
        print("Задача выполнена!")
    else:
        print("Неверный номер задачи!")


def main():
    while True:
        print("\n===== TODO APP =====")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Удалить задачу")
        print("4. Выполнить задачу")
        print("5. Очистить все задачи")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Название задачи: ")
            add_task(name)

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            show_tasks()
            try:
                number = int(input("Номер задачи: "))
                delete_task(number)
            except ValueError:
                print("Введите число!")

        elif choice == "4":
            show_tasks()
            try:
                number = int(input("Номер задачи: "))
                complete_task(number)
            except ValueError:
                print("Введите число!")

        elif choice == "5":
            clear_tasks()

        elif choice == "6":
            print("До свидания!")
            break

        else:
            print("Неверный выбор!")


if __name__ == "__main__":
    main()