import turtle as t
import time
from snake import Snake
from food import Food
from score import Score

# Screen setup

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Weaver's Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()  # will appear automatically since it's init
score = Score()

start = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


while start:
    screen.update()
    time.sleep(0.1)
    snake.move()

# detect food
    if snake.head.distance(food) < 15:  # can put objects in side attribute
        food.morefood()
        snake.extend()
        score.addpoint()

# detect wall
    if snake.head.xcor() < -285 or snake.head.xcor() > 285 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score.resetscore()
        snake.reset()

# detect tail
    for segments in snake.snakebody[1:]:  # check if snakehead contacts segments of snake after the first loop or growth
        if snake.head.distance(segments) < 10:
            score.resetscore()
            snake.reset()



screen.exitonclick()
