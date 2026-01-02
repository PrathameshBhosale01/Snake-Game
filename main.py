import time
import turtle
from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score

screen=Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



snake=Snake()
food =Food()
score=Score()



screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
# screen.onkey(score.game_over(),"q")


game_is_on=True
while  game_is_on:

     screen.update()
     time.sleep(0.1)
     snake.move()
     #detect collision with food
     if snake.head.distance(food) < 17:
          food.refresh()
          snake.extend()
          score.increase_score()

     # detect collision with wall
     if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
          snake.reset()
          score.reset()

     # detect collision with food
     for segment in snake.segments[1:]:

          if snake.head.distance(segment)<10:

               score.reset()



screen.exitonclick()