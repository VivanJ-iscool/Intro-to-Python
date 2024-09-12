import turtle
import datetime
sam=turtle.Turtle()
sam.shape('arrow')

currentMinute=datetime.datetime.now().minute
currentHour=datetime.datetime.now().hour

sam.penup()
sam.goto(0,-180)
sam.pendown()
sam.pencolor("blue")
sam.circle(180)

sam.pencolor("red")

sam.penup()
sam.goto(0,0)
sam.setheading(90)#Point to the top-12 o'clock
sam.right(currentHour*360/12)
sam.pendown()
sam.forward(100)

sam.penup()
sam.goto(0,0)
sam.setheading(90)#Point to the top-0 minute
sam.right(currentMinute*360/60)
sam.pendown()
sam.forward(150)

sam.getscreen().update()
