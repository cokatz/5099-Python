#
import turtle

def draw_multicolor_square(animal, size):
    """Make animal draw a multi-color square of given size."""
    for color in ["red", "purple", "hotpink", "blue"]:
        animal.color(color)
        animal.forward(size)
        animal.left(90)

wn = turtle.Screen()             # Set up the window and its attributes
wn.setup(800, 800)
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set some attributes
tess.pensize(3)

size = 20                        # Size of the smallest square
for _ in range(16):
    draw_multicolor_square(tess, size)
    size += 10                   # Increase the size for next time
    tess.forward(10)             # Move tess along a little
    tess.right(18)               # and give her some turn

wn.mainloop()
turtle.done()                    # needed in my SPyder