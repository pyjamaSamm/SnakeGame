import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
# make object of class Food
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# make snake move
game_is_on = True
while game_is_on:
    # now the screen will show up with the snake body looking as if all seg are moving together
    # this is outside for loop so that the screen is updated when the entire piece has moved
    screen.update()
    # add 0.2 sec delay after each segment moves
    time.sleep(0.1)
    snake.snake_move()

    # detect collision of snake with the food
    # snake.head is actually the first segment of snake...snake_segments[0]
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.counter()

    # detect collision with wall
    if snake.head.xcor() < -285 or snake.head.xcor() > 285 or snake.head.ycor() < -285 or not snake.head.ycor() < 285:
        # game_is_on = False..instead of this we will reset
        # score.game_over()
        score.reset()
        snake.reset()

    # detect collision with tail
    # check if head collides with any segment
    for segments in snake.snake_segments[1:]:
        if snake.head.distance(segments) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
