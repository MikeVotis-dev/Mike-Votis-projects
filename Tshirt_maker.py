import turtle

def draw_tshirt():
    turtle.fillcolor('blue')  # Fill color
    turtle.begin_fill()
    turtle.forward(200)  # Draw the body
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.end_fill()

draw_tshirt()
turtle.done()