from turtle import Turtle

class Snake:

    def __init__(self):
        self.snake_list = []
        for _ in range(3):
            snake = Turtle(shape='square')
            snake.color('white')
            snake.penup()
            snake.goto(x=_ * -20, y=0)
            self.snake_list.append(snake)

    def move(self):
        for i in range(len(self.snake_list) - 1, 0, -1):
            self.snake_list[i].goto(self.snake_list[i - 1].position())
        self.snake_list[0].forward(20)

    def up(self):
        if self.snake_list[0].heading() != 270:
            self.snake_list[0].setheading(90)

    def down(self):
        if self.snake_list[0].heading() != 90:
            self.snake_list[0].setheading(270)

    def right(self):
        if self.snake_list[0].heading() != 180:
            self.snake_list[0].setheading(0)

    def left(self):
        if self.snake_list[0].heading() != 0:
            self.snake_list[0].setheading(180)

    def add_snake(self):
        snake = Turtle(shape='square')
        snake.color('white')
        snake.penup()
        snake.goto(self.snake_list[-1].position())
        self.snake_list.append(snake)

