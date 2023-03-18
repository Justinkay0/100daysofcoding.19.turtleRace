import turtle
import random

screen = turtle.Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title='Make your bet', prompt='Which turtle color would you choose to win?')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_list = []

for i in range(6):
    t = turtle.Turtle(shape='turtle')
    t.color(colors[i])
    t.penup()
    t.setposition(x=-230, y=-100 + ((i + 1) * 40))
    turtle_list.append(t)

game_running = False
if user_choice:
    game_running = True

while game_running:
    for turt in turtle_list:
        if turt.xcor() >= 230:
            game_running = False
            if turt.pencolor() == user_choice.lower():
                print(f"You are a winner!! the winning turtle is {turt.pencolor()} in color")
            else:
                print(f"You are a loser!! the winning turtle is {turt.pencolor()} in color")

        turt.forward(random.randint(0, 10))

screen.exitonclick()
