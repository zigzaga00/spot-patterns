# creates spot patterns in the syle of damien hirst
# by puzz00

from spot import Spot
import turtle as t

# set the colormode of the turtle module to be rgb
t.colormode(255)

# instantiate a Screen and Turtle object
screen = t.Screen()
tim = t.Turtle()

# get the Turtle object ready to draw
tim.penup()
tim.speed(0)
tim.hideturtle()
tim.setheading(0)

# get data from the user regarding picture composition
x = int(input("\nEnter the x coordinate to start drawing from: "))
y = int(input("\nEnter the y coordinate to start drawing from: "))
size = int(input("\nEnter the size for each spot: "))

# instantiate a Spot object
spot = Spot(size, "spot_1.jpeg", screen, tim)

# extract colors
colours = spot.extract_colours()

spot.rectangle(x, y, colours)

