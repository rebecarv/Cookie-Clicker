#Cookie CLicker

import turtle

wn = turtle.Screen()
wn.title("Cookie Clicker")
wn.bgcolor("black")

wn.register_shape("cookie.gif")

cookie = turtle.Turtle()
cookie.shape("cookie.gif")

clicks = 0

text = turtle.Turtle()
text.hideturtle()
text.color("white")
text.penup()
text.goto(0, 200)
text.write(f"Clicks: {clicks}", align="center", font=("Verdana", 40, "normal"))

def clicked(x, y):
    global clicks 
    clicks += 1
    text.clear()
    text.write(f"Clicks: {clicks}", align="center", font=("Verdana", 40, "normal"))

cookie.onclick(clicked)

wn.mainloop()