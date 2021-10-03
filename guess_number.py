import random


def guess(x):
    random_number = random.randint(1, x)
    init_guess = 0
    while init_guess != random_number:
        init_guess = int(input(f'Please enter the nember between 1 to {x}: '))
        if init_guess > random_number:
            print('Sorry! your guess is so high.')
        elif init_guess < random_number:
            print('Sorry! your guess is so low')
    print(f"Yeah! your guess numer,{init_guess} is completely correct.")


guess(10)