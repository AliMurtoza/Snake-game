#imports
import turtle
import time
import random

delay = 0.1

#scores
score = 0
high_score = 0

#set up screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('yellow')
wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0);
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

segements = []

#scoreboard
sc = turtle.Turtle()
sc.speed(0);
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0, 260)
sc.write("Score: 0  High score: 0", align="center", font=("ds-digital", 24, "normal"))

      

