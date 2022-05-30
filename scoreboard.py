from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.stage = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.stage}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER")

    def increase_score(self):
        self.stage += 1
        self.clear()
        self.update_scoreboard()
