print("hi")

HELP = """
Hey, I'm your assistant.
I'll help you get used to my app.
These are commands you can put in
-help - print program help.
-add - add a task to the list (ask the user for the task name).
-show - print all added tasks.
"""

tak = {
    
}

ran = True

while ran:
    command = input("command: ")
    if command == "help":
        print(HELP)
    elif command == "add":
        date = input("date: ")
        tas = input("Enter a task name: ")
        if date in tak:
            tak[date].append(tas)
        else:
            tak[date] = [tas]
        print("Task", tas, "added to date", date)
    elif command == "show":
        date = input("ведите для отображения:")
        if date in tak:
            for tas in tak[date]:
                print('- ', tas)
        else:
            print("такой даты нет:")
    else:
        print("Unknown team")
        break
