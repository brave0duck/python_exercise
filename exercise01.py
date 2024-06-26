#   1.2 숫자맞히기 게임 v1.2.1
import random

def guessing_game():    #   random pop number 0~100
    number = random.randint(0,100)
    return number

random_number = guessing_game()
chance = 1

for i in range(1,4):
    usr_number = input(f'Guess the number (0~100), {i} times out of 3: ')
    try:
        if( int(usr_number) > random_number):
            print('Too High')
        elif( int(usr_number) < random_number):
            print('Too low')
        elif( int(usr_number) == random_number):
            print('Just right \n exit!')
            break
    except:
        print('wrong input... exit!')
        break
else:
    print('Unfortunately, you failed')
