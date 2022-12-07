import turtle
window=turtle.Screen()
window.title("turtles")
turtle.shape("turtle")
turtle.color("black")
for i in range (4):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
window.mainloop()
