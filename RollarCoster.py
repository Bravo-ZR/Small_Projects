import time

def wait(x):
    time.sleep(x)

bill = 0

print('Hello, Welcome to the Rollarcoster.')
wait(2)

print('Adult Tickets are 20tk')
wait(2)

print('Kid Tickets are 10tk')

wait(2)

print('People who are having midlife crisis between the age of 45-55 are free of charge.')

height = int(input('What is your height(cm): '))
wait(2)

if height >= 120:
    print('You can ride the Rollarcoster.')
    wait(2)

    age = int(input('How old are you?: '))
    wait(1)
    photo = input('Do you want a photo(Y/N): ')
    
    if age <= 18:
        bill = 10
    elif age > 18 and age < 45:
        bill = 20
    elif age >= 45 and age <= 55:
        bill = 0
    if photo == 'Y':
        bill += 5
        print(f"Your total bill is {bill}tk")
    else:
        print(f"Your total bill is {bill}tk")

    wait(5)

else:
    print('Sorry you have to grow taller to be able to ride the Rollarcoster.')
