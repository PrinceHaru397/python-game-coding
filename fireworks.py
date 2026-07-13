import turtle
import random
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
sc = turtle.Screen()
sc.setup(500, 500)
sc.bgcolor("black")
times = 8
rot = 360 / times
for i in range(10):
  x = random.randint(-250, 250)
  y = random.randint(-250, 250)
  t.penup()
  t.goto(x, y)
  colors = ["red", "orange", "yellow", "lime", "blue", "indigo", "violet"]
  color = random.choice(colors)
  t.pendown()
  for i in range(times):
    t.color(color)
    f = random.randint(20, 50)
    t.forward(f)
    t.backward(f)
    t.right(rot)