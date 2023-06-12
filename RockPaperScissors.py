rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
import time

moves = [rock,paper,scissors]

player_move = int(input('0(Rock),1(Paper),2(Scissors): '))

computer_move = random.randint(0,2)

if player_move == computer_move:
    print('Draw!')
    print(f'''Player move:
    {moves[player_move]}

    Computer move:
    {moves[computer_move]}
    ''')
elif player_move != computer_move:
    if player_move == 0 and computer_move == 1:
        print("You lost!")
        print(f'''Player move:
        {moves[player_move]}

        Computer move:
        {moves[computer_move]}
        ''')
    elif player_move == 1 and computer_move == 2:
        print("You lost!")
        print(f'''Player move:
        {moves[player_move]}

        Computer move:
        {moves[computer_move]}
        ''')
    elif player_move == 2 and computer_move == 0:
        print("You lost!")
        print(f'''Player move:
        {moves[player_move]}

        Computer move:
        {moves[computer_move]}
        ''')
    else:
        print("You win!")
        print(f'''Player move:
        {moves[player_move]}

        Computer move:
        {moves[computer_move]}
        ''')



time.sleep(4)


