def menu():
    user_input = ''
    numbers = []
    while True:
        print('1) Addition')
        print('2) Subtraction')
        print('3) Multiplication')
        print('Division 4)')
        try:
            user_input =int(input('Enter operation number: '))
            if user_input == 1:
                while not user_input == 0:
                    user_input = int(input('Enter any number not zero to add on to your equation: '))
                    if user_input != 0:
                        numbers.append(user_input)
                else:
                    print('The answer is {}'.format(add(numbers)))
            elif user_input == 2:
                while not user_input == 0:
                    user_input = int(input('Enter any number not zero to add on to your equation: '))
                    if user_input != 0:
                        numbers.append(user_input)
                else:
                    print('The answer is {}'.format(subtract(numbers)))
			elif user_input == 3:
				while not user_input == 0:
                    user_input = int(input('Enter any number not zero to add on to your equation: '))
                    if user_input != 0:
                        numbers.append(user_input)
					else:
					print('The answer is {}'.format(multiply(numbers))
        except ValueError as ex:
            print(ex)


def add(all_numbers):
    full_prob = 0
    for z in all_numbers:
        full_prob += z
    return full_prob


def subtract(all_numbers):
    full_prob = 0
    for z in all_numbers:
        full_prob -= z
    return full_prob


def multiply(all_numbers):
    full_prob = 0
    for z in all_numbers:
        full_prob *= z


def division():
    pass


menu()
print('Hello World!')