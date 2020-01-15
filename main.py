def menu():
    user_input = ''
    while True:
        print('1) Addition')
        print('2) Subtraction')
        print('3) Multiplication')
        print('Division 4)')
        try:
            user_input = int(input('Enter operation number: '))

        except ValueError as ex:
            print(ex)


def add():
    pass


def subtract():
    pass


def multiply():
    pass


def division():
    pass