import turtle
import random
t = turtle.Turtle()
t.up()
t.speed(15)

def make_square(change):
  t.down()
  t.color(change)
  t.begin_fill()
  for i in range(4):
    t.forward(100)
    t.rt(90)
  t.end_fill()
  t.up()

t.goto(-300,0)
make_square("red");

t.goto(-200,0)
make_square("orange");

t.goto(-100,0)
make_square("yellow");

t.goto(0,0)
make_square("green");

t.goto(100,0)
make_square("blue");

t.goto(200,0)
make_square("indigo");

t.goto(300,0)
make_square("violet");
