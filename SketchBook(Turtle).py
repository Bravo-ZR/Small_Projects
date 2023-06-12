import turtle 

class Movement:
    def __init__(self, bot) -> None:
        self.object = bot
    def forward(self):
        self.object.forward(10)
    def backward(self):
        self.object.backward(10)
    def left(self):
        self.heading = self.object.heading()
        self.object.setheading(self.heading + 10)
    def right(self):
        self.heading = self.object.heading()
        self.object.setheading(self.heading - 10)   
    def clear(self):
        self.object.clear()
        self.object.penup()
        self.object.home()
        self.object.pendown()

bot = turtle.Turtle()

movement = Movement(bot)

screen = turtle.Screen()


screen.listen()
screen.onkeypress(key='w', fun= movement.forward)
screen.onkeypress(key='a', fun= movement.left)
screen.onkeypress(key='s', fun= movement.backward)
screen.onkeypress(key='d', fun= movement.right)
screen.onkeypress(key='c', fun= movement.clear)



screen.listen()
screen.exitonclick()