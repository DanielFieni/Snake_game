from turtle import Screen
from snake import Snake;
from food import Food;
from scoreboard import Scoreboard;
import time;

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# CREATE A SNAKE BODY
snake = Snake()
# CREATE SNAKE FOOD
food = Food()
# CREATE A SCOREBOARD
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down') 
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    # MOVE THE SNAKE
    snake.move()

    # DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # DETECT COLLISION WITH WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.restart_score()
        snake.restart_snake()
    
    # DETECT COLLISION WITH TAIL
    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.restart_score()
            snake.restart_snake()        
                
screen.exitonclick()
