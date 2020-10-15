#**----------------------------By Enigma1997NH--------------------------------**
import turtle
import time
import math
import random

#scoring
score=0
high_score=0

wn=turtle.Screen()
wn.title("FeedtheArrow")
wn.bgcolor("silver")
wn.setup(width=650,height=650)
wn.tracer(0)

#draw border
mypen=turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pencolor("white")
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
#mypen.hideturtle()

#create player turtule
player= turtle.Turtle()
player.speed(0)
player.color("gold")
player.shape("arrow")
player.penup()
player.goto(0,0)
player.direction="stop"


#goal1
goal=turtle.Turtle()
goal.color("black")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(-100,-100)
goal.count=0
speed=0.1

#countingnumber
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("ghost white")
pen.penup()
pen.hideturtle()
pen.goto(0,-250)
pen.write("Score: 0  By : Enigma1997NH" ,align="left",font={"courier",24,"normal"})


#key function
def turnleft():
    player.left(30)
def turnright():
    player.right(30)
def increasespeed():
    global speed
    speed +=0.1
def decreasespeed():
    global speed
    speed -=0.1
def reset():
    player.goto(0,0)
    global speed
    speed = tt
def pause():
    global speed
    speed = 0.0
def resume():
    global speed
    speed = tt

#set keyboard binding
turtle.listen()
turtle.onkey(turnleft,"a")
turtle.onkey(turnright,"d")
turtle.onkey(increasespeed,"w")
turtle.onkey(decreasespeed,"s")
turtle.onkey(reset,"r")
turtle.onkey(pause,"p")
turtle.onkey(resume,"s")

while True:
    wn.update()
    player.forward(speed)

    #boundary check
    if player.xcor()>300 or player.ycor() < -300:
        player.right(180)

    if player.ycor() > 300 or player.xcor() < -300:
        player.right(180)


#checking distance
    dis=math.sqrt(math.pow(player.xcor()-goal.xcor(),2) +  math.pow(player.ycor()-goal.ycor(),2))
    if dis<20:
        goal.setposition(random.randint(-300,300),random.randint(-300,300))
        speed += 0.1
        score += 1
        if score > high_score:
            high_score = score
            pen.clear()
            pen.write("Score:  {}  By : Enigma1997NH ".format(score, high_score),align="left",font={"courier",24,"normaldd"})


wn.mainloop()
