##### Building Snake Game #########
##### Demos from turtle: python -m turtledemo ####
### Steps of building snake game: ###
## 1.Create a snake body ##
# Make 3 squares on the screen, all lined up next to each other #
## 2.Move the snake ##
# How to move the snake continuously  (only forward) #
## 3.Control the snake ##
# How to control the snake using keyboard controls (up / left / down / right) #
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.25)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with the wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.reset()
            snake.reset()

# for seg in segments:
#     seg.forward(20)
#
# segments[0].left(90)
# screen.update()
# time.sleep(1)
# segment_1 = Turtle(shape="square")
# segment_1.color("white")
#
# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto(-20, 0)
#
# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_3.goto(-40, 0)

screen.exitonclick()

######################## 21 st day: Building Snake Game ##########################
#### Class Inheritance ####
#
#
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale, exhale.")
#
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#
#     def breathe(self):
#         super().breathe()
#         print("Doing this underwater.")
#
#     def swim(self):
#         print("Moving in water.")
#
#
# nemo = Fish()
# # nemo.swim()
# nemo.breathe()
# # print(nemo.num_eyes)
##### Slicing #####
# piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
# print(piano_keys[2:5])
# ## prints ['c', 'd', 'e']
# print(piano_keys[2:])
# ## prints ['c', 'd', 'e', 'f', 'g']
# print(piano_keys[:5])
# ## prints ['a', 'b', 'c', 'd', 'e']
# print(piano_keys[2:5:2])
# ## prints ['c', 'e']
# print(piano_keys[::2])
# ## prints ['a', 'c', 'e', 'g'] (skips every second object in list)
# print(piano_keys[::-1])
# ## prints ['g', 'f', 'e', 'd', 'c', 'b', 'a'] (reverses order)
# ## Slicing is also work for tuples ##
