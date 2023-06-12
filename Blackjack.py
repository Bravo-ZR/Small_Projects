import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card(cards):
    x = random.choice(cards)
    return x

user_cards = [draw_card(cards), draw_card(cards)]

computer_cards = [draw_card(cards), draw_card(cards)]

def check(computer_cards):
    total = sum(computer_cards)
    if total < 17:
        return 2
    else:
        return 0

def counter(user_cards, computer_cards):
    total_user = sum(user_cards)
    total_computer = sum(computer_cards)

    if total_user > 21 or total_computer == 21:
        return False
    elif total_user == 21 or total_computer > 21:
        return True
    else:
        return 0

def draw_counter(user_cards,computer_cards):
    total_user = sum(user_cards)
    total_computer = sum(computer_cards)

    if total_user < total_computer:
        return False
    elif total_computer < total_user:
        return True


print(f"Your Cards: {user_cards}")
print(f"Computer's Cards: {computer_cards}")
a = counter(user_cards, computer_cards)
b = check(computer_cards)

if a == 0:
    perm = input("Do you want another card? 'y' or 'n': ")

    if perm == 'y':
        x = draw_card(cards)
        if x == 11:
            user_cards.append(1)
        else:
            user_cards.append(x)
        if sum(user_cards) > 21:
            print('You lost!') 
    if b == 2:
        computer_cards.append(draw_card(cards))

    print(f"Your Cards: {user_cards}")
    print(f"Computer's Cards: {computer_cards}")

else:
    pass
a = counter(user_cards, computer_cards)

if not draw_counter(user_cards, computer_cards) and a == True:
    print('You Win!')
elif draw_counter(user_cards, computer_cards) and a == False:
    print('You Lost!')
elif a == True:
    print('You Win!')
elif a == False:
    print('You Lost!')