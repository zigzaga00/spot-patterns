# a class to create Spot objects
# which can create spot patterns
# by puzz00

import colorgram
from random import shuffle
from time import sleep

class Spot(object):
    def __init__(self, size, pic, screen, turtle):
        self.size = size
        self.pic = pic
        self.screen = screen
        self.turtle = turtle
    
    def extract_colours(self):
        colours = colorgram.extract(self.pic, 30)
        rgb = [(colour.rgb.r, colour.rgb.b, colour.rgb.g) for colour in colours]
        return tuple(rgb)
    
    def rectangle(self, x, y, colours):
        palette = list(colours)
        shuffle(palette)
        columns = int(input("\nEnter the number of columns: "))
        rows = int(input("\nEnter the number of rows: "))
        spacing = int(input("\nEnter the spacing: "))
        for i in range(rows):
            self.turtle.goto(x, y)
            for j in range(columns):
                colour = palette.pop()
                self.turtle.dot(self.size, colour)
                self.turtle.fd(spacing)
                sleep(0.25)
            y += spacing
        self.screen.exitonclick()
