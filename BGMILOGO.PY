#_________ WELCOME ALL OF YOU ON COMPUTER SOFT SKILLS CHANNEL __________
#........................ BGMI DRAWING USING PYHON TURTLE GRAPHICS ......................


import turtle
from sketchpy import canvas
wn = turtle.Screen()
wn.setup(width=1100, height=750)
wn.title("COMPUTER SOFT SKILLS :- BGMI LOGO")
turtle.Screen().bgcolor("ROYALBLUE")
t=turtle.Turtle()

# DRAW RECTANGLE
t.color("limegreen")
def turn():
 t.left(45)
 t.forward(6)
 t.left(45)

t.color("limegreen")
t.pensize(15)
t.forward(170)
turn()
t.forward(85)
t.color("orangered")
t.forward(85)
turn()
t.forward(330)
turn()
t.forward(85)
t.color("limegreen")
t.forward(85)
turn()
t.forward(170)

t.color("white")
t.pensize(15)

#DRAW B LETTER
t.penup()
t.backward(135)
t.left(90)
t.forward(140)
t.right(90)
t.pendown()
t.forward(45)
t.right(90)
t.forward(40)
t.right(45)
t.forward(8)
t.right(45)
t.forward(35)
t.left(90)
t.forward(8)
t.left(90)
t.forward(35)
t.right(45)
t.forward(8)
t.right(45)
t.forward(40)
t.right(90)
t.forward(45)
t.right(90)
t.forward(100)

# DRAW G LETTER
t.penup()
t.right(180)
t.forward(53)
t.left(90)
t.forward(103)
t.pendown()
t.forward(25)
t.right(90)
t.forward(45)
t.right(90)
t.forward(45)
t.right(90)
t.forward(95)
t.right(90)
t.forward(45)

# DRAW M LETTER
t.penup()
t.forward(40)
t.right(90)
t.forward(95)
t.left(180)
t.pendown()
t.forward(96)
t.right(150)
t.forward(55)
t.left(120)
t.forward(55)
t.setheading(0)
t.right(90)
t.forward(96)

# DRAW I LETTER
t.penup()
t.left(90)
t.forward(40)
t.left(90)
t.pendown()
t.forward(96)
t.hideturtle()

t.penup()
t.goto(350,-85)
t.pendown()
t.color('DARKORANGE')
style = ('ARIAL BLACK',50,'bold')
t.write('BATTLEGROUNDS', font=style, align='right',move=True)
t.hideturtle()

# draw rectangle
t.penup()
t.pensize(5)
t.begin_fill()
t.color("white")
t.goto(35, -75)
t.forward(-70)
t.left(90)
t.forward(300)
t.left(90)
t.forward(-70)
t.left(90)
t.forward(300)
t.left(90)
t.end_fill()
t.hideturtle()

#.......................................

t.penup()
t.goto(-10,-140)
t.pendown()
style = ('ARIAL BLACK',35,'bold')
t.color('black')
t.write('MOBILE', font=style, align='right',move=True)
t.hideturtle()

t.penup()
t.goto(230,-140)
t.pendown()
t.color('CHARTREUSE')
style = ('myriad bold',45,'bold')
t.write('INDIA', font=style, align='right', move=True)
t.hideturtle()

#bgmi man sketch in .svg file
ab = canvas.sketch_from_svg("D:\\python\\bgmi.svg",scale=75)
ab.draw()

turtle.done()











