from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.snake_list[0].distance(food) < 15:
        food.generate_new_position()
        scoreboard.add_score()
        snake.add_snake()

    if snake.snake_list[0].xcor() > 290 or snake.snake_list[0].xcor() < -295 or snake.snake_list[0].ycor() > 295 or snake.snake_list[0].ycor() < -290:
        scoreboard.game_over()
        game_over = True

    for i in range(1,len(snake.snake_list)):
        if snake.snake_list[0].distance(snake.snake_list[i]) < 10:
            game_over = True
            scoreboard.game_over()


screen.exitonclick()