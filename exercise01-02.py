#   숫자맞추기 아닌 단어맞추기
import random

random_list = ['abc','banana','apple','blue','airplane','korea','intel','tv','dog','sky']
computer_index = random.randint(1,10)

print(f'List is {random_list}.\nWhat word did the computer choose? :')

while True:
    try:
        usr_word = input('choose word : ')
        if (usr_index := random_list.index(usr_word)):
            if computer_index > usr_index:
                print('more rear')
            elif computer_index < usr_index:
                print('more front')
            else:
                print(f'That\'s Right!!! computer choose [{usr_word}]!')
                break
    except:
        print('nothing word... exit!')
        break
