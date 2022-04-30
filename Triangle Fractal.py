import turtle
import random
from sys import exit

def init():
    turtle.bgcolor("#FFFFFF")

    global pen
    pen = turtle.Turtle(visible=False)

    global pen2
    pen2 = turtle.Turtle(visible=False)

    pen.speed(0); pen2.speed(0)
    pen.pu(); pen2.pu()

    global points
    points = [[-300,-250],  [0,250], [300,-250]]

    for i in range(3):
        pen.setpos(points[i])
        pen.dot(10)
    return()
    
def User_input():
    
    try:
        inp = int(input("Color? 0 = black 1 = purple 2 = green 3 = fuchsia\n>"))
    except:
        print("\nError: Yes strings crash the programme idc lol\n")
        exit()

    global colours
    colour = [
    ["#000000"], 
    ["#d16aff", "#bb44f0", "#9614d0", "#660094", "#310047", "#32349f"], 
    ["#cae6df", "#064b55", "#0a674f", "#044541", "#04192e"], 
    ["#e95670", "#b34270", "#713770", "#432f70"]]
    colours = colour[inp]

    try:
        inp = int(input("enter size of dots 0-10\n>"))
    except:
        print("\nError: Yes strings crash the programme idc lol\n")
        exit()

    global DS
    DS = inp


User_input()
init()

while True:
    point1 = points[random.randint(0,2)]
    x = (point1[0] + pen.xcor()) / 2
    y = (point1[1] + pen.ycor()) / 2

    point2 = points[random.randint(0,2)]
    x2 = (point2[0] + pen2.xcor()) / 2
    y2 = (point2[1] + pen2.ycor()) / 2

    pen.setpos(x,y)
    pen2.setpos(x2,y2)

    pen.dot(DS, colours[random.randint(0, len(colours) - 1)])
    pen2.dot(DS, colours[random.randint(0, len(colours) - 1)])

turtle.done()