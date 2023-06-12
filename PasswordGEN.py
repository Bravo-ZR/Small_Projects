#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

letter_main = []
symbols_main = []
number_main = []

for n in range(nr_letters):
    letter_choice = random.choice(letters)
    letter_main.append(letter_choice)

for n in range(nr_symbols):
    symbol_choice = random.choice(symbols)
    symbols_main.append(symbol_choice)

for n in range(nr_numbers):
    number_choice = random.choice(numbers)
    number_main.append(number_choice)


letter_main.extend(symbols_main + number_main)
random.shuffle(letter_main)

password = ''.join(letter_main)
print(f"Your password is: {password}")





