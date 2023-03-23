import random

def welcome():# This just for compiling in console or terminal
    print("Welcome to ROCK PAPER SCISORS GAME!!!\n")
    print("You will play with a computer, try to win\n")
    print("*******************************************\n")

def select_random_position(lista):
    value = random.choice(lista)
    print(value)
    return value

def user_option(lista):

    value = int(input("Select 1.rock, 2.paper or 3.scisors\n"))
    if value == 1:
        value = 'rock'
    if value == 2:
        value = 'paper'
    if value == 3:
        value = 'scisors'
    if value not in lista:
        return False
    return value


def main():
    welcome()
    option_list = ["rock","paper","scisors"]
    dict_win = {'rock':'paper','paper':'scisors','scisors':'rock'}
    lifes_users = 3
    lifes_computer = 3
    while True:
        if lifes_users == 0 or lifes_computer == 0:
            break
        random_value = select_random_position(option_list)
        user_value = user_option(option_list)
        if user_value == False:
            print("Invalid Answer, try again")
            continue
        if random_value == user_value:
            print("No one win this")
        else:
            for key in dict_win:
                if random_value == dict_win[key] and user_value == key:
                    lifes_users -= 1
                    print("Buena para el computador ==> ",random_value)
                    print("\nUser : ",lifes_users, "\nComputer : ", lifes_computer)
                    break
                elif random_value == key and user_value == dict_win[key]:
                    lifes_computer -=1
                    print("Buena para el usuario ==> ", user_value)
                    print("\nUser : ",lifes_users, "\nComputer : ", lifes_computer)
                    break
    if lifes_computer > lifes_users:
        print("Gano el Computador!!!")
    elif lifes_users > lifes_computer:
        print("Gano el Usuario!!!")
    else:
        print("Empate :c")

main()
