import turtle
# Set up the screen
window = turtle.Screen()
window.setup(width=800, height=800)

# Function to draw an N-pointed star
def draw_n_star(size, N):
    if N < 3:
        raise ValueError("Number of points (N) must be 3 or more")

    t = turtle.Turtle()
    t.speed(2)

    angle = 720 / (2*N)  #angle between 2 points
    
    for _ in range(N):
        t.forward(size)
        t.left(180 - angle)
        t.forward(size)
        t.right(360 / N)

#draw n pointed star
draw_n_star(200, 6)


# DON'T TOUCH THIS
turtle.mainloop()
