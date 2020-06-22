def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_name():
    print('Please, remind me of your name below.')
    name = input()
    print(f'What a great name you have, {name}')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(f"Your age is {age}; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your knowledge.")
    print("What is 1+1?")
    print("1. -1")
    print("2. 1")
    print("3. 69")
    print("4. None")
    answer = int(input())
    if answer == 2:
        print("Wow, what a smart boy.")
    else:
        print("Please, try again.")


def end():
    print('It was nice getting to know you. Goodbye')


greet('Robo-Bill', '2020')
remind_name()
guess_age()
count()
test()
end()
