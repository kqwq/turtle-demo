"""
Turtle docs
basic: http://www.pythonsandbox.com/docs/turtle
all commands: https://docs.python.org/3/library/turtle.html
"""

import turtle

def make_star(start_x, start_y, size):
    t.setpos(start_x, start_y)
    t.pendown()
    t.begin_fill()
    for c in range(8): # draw each edge of the star
        t.color('black')
        t.forward(size)
        t.left(135)
        t.forward(size)
        t.right(90)
    t.color('yellow') # fill it in with yellow
    t.end_fill()
    t.penup()

def make_pumpkin(start_x, start_y, size):

    # Draw ovals (ellipses)
    for i in [-2,2,-1,1,0]:
        t.setheading(0)
        t.setpos(start_x + i * size * 0.3, start_y + abs(i) * size * 0.05)
        r = size - size * 0.02 * abs(i * i) # ellipse radius
        t.left(45)
        t.pendown()
        for loop in range(2):      # Draws 2 halves of ellipse
            t.color('gray')
            t.begin_fill()
            t.circle(r,90)    # Long curved part
            t.circle(r/6,90)  # Short curved part
            t.color('#EDAC3B') # pumpkin orange
            t.end_fill()
        t.penup()

    # Go to top
    t.setheading(90)
    t.forward(size * 1.5)

    # Draw stem
    t.color('#AAC461') # green stem
    t.pendown()
    t.begin_fill()
    t.circle(1 * size, 20) # ) right
    t.left(90)
    t.forward(0.1 * size) # - top
    t.left(90)
    t.circle(-1 * size, 20) # ) left
    t.left(90)
    t.forward(0.1 * size) # _ bottom
    t.end_fill()
    t.penup()    

# turtle setup
t = turtle.Turtle()
t.speed(5)

# format: x position, y position, size
make_star(0, 0, 20)
make_star(100, 100, 30)
make_pumpkin(150, 30, 20)
make_star(0, -160, 15)
make_star(260, -50, 17)
make_pumpkin(-150, -30, 40)

# hide turtle cursor
t.hideturtle()