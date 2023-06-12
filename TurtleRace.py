from turtle import Turtle, Screen
import random


screen = Screen()

screen.setup(width=500, height= 400)
user_bet = screen.textinput(title='Place your bets:',prompt='Which turtle will win!')



tim1 = Turtle(shape='turtle')
tim1.color('blue')
tim2 = Turtle(shape='turtle')
tim2.color('red')
tim3 = Turtle(shape='turtle')
tim3.color('green')
tim4 = Turtle(shape='turtle')
tim4.color('yellow')

tim1.penup()
tim2.penup()
tim3.penup()
tim4.penup()

tim1.goto(x=-230, y=-50)

tim2.goto(x=-230, y=-20)

tim3.goto(x=-230, y= 20)

tim4.goto(x=-230, y= 50)

if user_bet:
    race_on = True

winner = ''

while race_on:
    tim1.forward(random.randint(0,5))
    tim2.forward(random.randint(0,5))
    tim3.forward(random.randint(0,5))
    tim4.forward(random.randint(0,5))
    if tim1.xcor() > 238:
        race_on = False
        winner = 'blue'
    if tim2.xcor() > 238:
        race_on = False
        winner = 'red'
    if tim3.xcor() > 238:
        race_on = False
        winner = 'green'
    if tim4.xcor() > 238:
        race_on = False
        winner = 'yellow'


if winner == user_bet:
    print(f"Your choice won!")
else:
    print(f"Your lost. The {winner} won!")



screen.exitonclick()