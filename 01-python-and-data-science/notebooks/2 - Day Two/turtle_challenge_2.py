import turtle

window = turtle.Screen()
window.bgcolor("orange")
window.setup(width=800, height=800)
t = turtle.Turtle()

# Challenge 2: Circles in a Grid with One Missing

def draw_triangle(self,side_length=200):
    self.pendown()
    self.color("magenta")
    self.pensize(8)
    for _ in range(3):
        self.pendown()
        self.right(120)
        self.forward(side_length)
        self.right(120)
        self.penup()

draw_triangle(t)
    
# DON'T TOUCH THIS
turtle.mainloop()