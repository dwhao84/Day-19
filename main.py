import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400) # Unit is pixel.
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
positon = [-125, -75, -25, 25, 75, 125]
print(user_bet)
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=positon[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230: # 當x座標，已經到達230時，將跳出下列內容。
            wining_color = turtle.pencolor()
            is_race_on = False
            if wining_color == user_bet:
                print(f"You've won { wining_color } turtle is the winner!")
            else:
                print(f"You've lose! The { wining_color } turtle is the winner!")
            break
            
        # 注意縮排位置:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()