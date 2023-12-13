HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
ranbom - добавляет случайную задачу на сегодня."""

PANDOM_TASK = "найти жизнь"

tasks = {

}

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("ведите для отображения:")
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print("такой даты нет:")
    elif command == "add":
        date = input("дата:")
        task = input("Введите название задачи: ")
        if date in tasks:
            tasks[date].append(task)
        else:
            tasks[date] = [task]
        print("Задача", task, "добавлена на дату", date)
    elif command == "random":
        if "сегодня" in tasks:
            tasks["сегодня"].append(PANDOM_TASK)
        else:
            tasks["сегодня"] = []
            tasks["сегодня"].append(PANDOM_TASK)
    else:
        print("Неизвестная команда")
        break

print("До свидания!")