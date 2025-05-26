from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"{self.l_score} : {self.r_score}", align=ALLIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALLIGNMENT, font=FONT)

    def create_new_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def create_new_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()