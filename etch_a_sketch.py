# Build an Etch a Sketch
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

# 往前
def forward():
    t.forward(10)

# 往後
def backward():
    t.backward(10)
  
# 逆時針
def counter_clockwise():
    new_heading = t.heading() + 10
    t.setheading(new_heading)

# 順時針
def clockwise():
    new_heading = t.heading() - 10
    t.setheading(new_heading)

# 狀態清除
def clear():
    t.reset()
    t.penup()
    t.home()
    t.pendown()
    
"""
Spec:
W = Forwards 往前
S = Backwards 網後
A = Counter-Clockwise 逆時鐘
D = Clockwise 順時鐘
"""

# 用screen監聽。
screen.listen()

# 設定key的鍵，設定好之後，就可以帶入function。
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

# 點擊螢幕以後，螢幕自動關閉。
screen.exitonclick()


    