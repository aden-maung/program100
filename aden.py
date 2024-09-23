import turtle
import time
import random

delay = 0.2
wn = turtle.Screen()
wn.title('oray')
wn.bgcolor('white')
wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(-10)
head.shape('circle')
head.color('green')
head.penup()
head.goto(0,0)
head.direction = 'stop'

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)

segments = []

#function
def go_up():
    head.direction = 'up'

def go_down():
    head.direction = 'down'

def go_left():
    head.direction = 'left'

def go_right():
    head.direction = 'right'


def move():
    if head.direction == 'up':
         y = head.ycor()
         head.sety(y + 20)

    elif head.direction == 'down':
         y = head.ycor()
         head.sety(y - 20)

    elif head.direction == 'left':
         x = head.xcor()
         head.setx(x - 20)

    elif head.direction == 'right':
         x = head.xcor()
         head.setx(x + 20)

#keyboard binding
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


#mainloop
while True:
    wn.update()
    if head.distance(food) < 20:
        #move the food
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(random.randint(-290,290),random.randint(-290,290))
        new_segment = turtle.Turtle()
        new_segment.speed(-1)
        new_segment.shape('square')
        new_segment.color('green')
        new_segment.penup( )
        segments.append(new_segment)
    

    for index in range (len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()
    time.sleep(delay)

wn.mainloop()