import turtle

window = turtle.Screen()
window.bgcolor("light blue")
window.setup(width=800, height=800)
t=turtle.Turtle()

def draw_rectangle(self,side_length_x=250, side_height_y=125):
    self.penup()
    self.color("white")
    self.pensize(8)
    self.setposition(x=-150, y=150)
    for _ in range(2):
        self.pendown()
        self.forward(side_length_x)
        self.right(90)
        self.forward(side_height_y)
        self.right(90)

def draw_triangle(self,side_length=200):
    self.penup()
    self.color("magenta")
    self.pensize(8)
    self.setposition(x=125, y=-125)
    for _ in range(3):
        self.pendown()
        self.right(120)
        self.forward(side_length)
        self.right(120)
        self.penup()

#def rotate_triangle(self, side_length=200):
    #self.penup()
    #self.color("orange")
    #self.pensize(8)
    #for _ in range(8):
        #self.pendown()
        #self.right(120)
        #self.forward(side_length)
    #self.penup()

#rotate_triangle(t)

Loops and Turtle

from turtle import Turtle, Screen

# Initialize the screen
wn = Screen()
wn.bgcolor("white")
wn.title("Square Repeating Around 360 Degrees")

# Initialize the turtle
t = Turtle()
t.speed(0)  # Set the turtle speed to the maximum

# Repeat drawing the square around 360 degrees
for _ in range(36):  # 36 iterations for 10 degrees each (360 / 36 = 10)
    # Draw the square
    for _ in range(3):
        t.pensize(8)
        t.forward(100)
        t.right(120)
    
    # Rotate the turtle by 10 degrees for the next square
    t.right(10)

# Keep the window open until clicked
wn.exitonclick()

#draw_triangle(t)
#draw_rectangle(t)




turtle.mainloop()