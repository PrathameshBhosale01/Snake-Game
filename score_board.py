from turtle import Turtle,Screen
from food import Food


# tim=Turtle()
# tim.penup()
# tim.sety(280)
# tim.write("Score:",align="center",font=("Arial",24,"normal"))


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0,250)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()




    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", align="center", font=("courier", 24, "normal"))


    # def game_over(self):
    #      self.goto(0,0)
    #      self.write("GAME OVER", align="center", font=("courier", 24, "normal"))

    def reset(self):
        if self.score> int(self.high_score):

            self.high_score=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()

    def increase_score(self):
        self.score+=1
        self.color("white")
        self.clear()
        self.update_scoreboard()
        self.hideturtle()

    def show_start_message(self):
        self.goto(0, 0)
        self.write(
            "Press any key to start",
            align="center",
            font=("Arial", 18, "normal")
        )





