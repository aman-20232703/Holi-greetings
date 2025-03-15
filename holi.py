import turtle
import random
turtle.bgcolor("white")
t=turtle.Turtle()
t.speed("fastest")
t.penup()

turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color

t.setheading(220)
t.forward(300)
t.setheading(0)
dots=91

for current_dots in range(1,dots):
    t.color(random_color())
    t.dot(20)
    t.forward(50)
    if current_dots % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)
        
t.penup()
t.goto(-240,0)
t.pendown()
t.write("Happy Holi",font=("Times New Roman",70,"bold"))
turtle.exitonclick()