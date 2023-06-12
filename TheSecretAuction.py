import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
'''

print(logo)
# Main Area=============================================================
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

bidders = {}

def bidding():
    bidder = input('Your name: ')
    bid_amount = int(input('Your Bid: $'))

    bidders[bidder] = bid_amount
bidding()
clear()

#=========================================================================
#Loop area ===============================================================
loop = input('Is there any other bidder?(Y/N):').lower()

while loop == 'y':
    bidding()
    clear()
    loop = input('Is there any other bidder?(Y/N):').lower()

#=========================================================================
#Max Amount Checker ======================================================
amount = 0
name = ''

for bidder in bidders:
    amountIN = bidders[bidder]
    nameIN = bidder
    if amount <= amountIN:
        amount = amountIN
        name = nameIN

#===================================================================

print(f"The Highest Bidder is {name} and the amount is ${amount}")

