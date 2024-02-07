import turtle
import time

t = turtle.Turtle()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

t.speed(0)

for i in range(200):
    t.fd(i)
    t.rt(56)
    t.width(i)
    t.color(colors[i % len(colors)])

time.sleep(5)
