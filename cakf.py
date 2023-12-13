cal = input("command: ")

try:
    a = float(input("input data:"))
    b = float(input("input data:"))
    if cal not in ('+', '-', '*'):
        raise Exception("you were running the wrong team.")

    if cal == '+':
        print(f'computational result: {a + b}')
    elif cal == '-':
        print(f'computational result: {a - b}')
    elif cal == '*':
        print(f'computational result: {a + b}')
    elif cal == '/':
        print(f'computational result: {a / b}')
except ZeroDivisionError:
    print("you can't divide by zero ")
finally:
    print("work completed ")