import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Bendera Indonesia")

# Create a turtle object
bendera = turtle.Turtle()

# Draw the red part of the flag
bendera.penup()
bendera.goto(-150, 0)
bendera.pendown()
bendera.color("red")
bendera.begin_fill()
for _ in range(2):
    bendera.forward(300)
    bendera.right(90)
    bendera.forward(100)
    bendera.right(90)
bendera.end_fill()

# Draw the white part of the flag
bendera.penup()
bendera.goto(-150, -100)
bendera.pendown()
bendera.color("white")
bendera.begin_fill()
for _ in range(2):
    bendera.forward(300)
    bendera.right(90)
    bendera.forward(100)
    bendera.right(90)
bendera.end_fill()

# Hide the turtle and display the window
bendera.hideturtle()
turtle.done()
