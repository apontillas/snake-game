from turtle import Screen
import time
from snake import Snake
from food import Food, COLORS
from score import Score
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Larong Ahas')
screen.tracer(0)

food = Food()
score = Score()
snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collison with food
    if snake.head.distance(food) < 15:
        score.inc_score()
        food.refresh()
        snake.extend()

    #Detect collision with walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

   #Detect collison with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

    #Milestones 10
    if score.score % 10 == 0 and score.score != 0:
        for segment in snake.segments:
            segment.color(random.choice(COLORS))
    else:
        for segment in snake.segments:
            segment.color('white')

screen.exitonclick()