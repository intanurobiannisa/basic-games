from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.penup()
        # self.speed("fastest")
        self.goto(position)
        # self.showturtle()

    def right(self):
        if self.xcor() < 340:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())
        else:
            self.goto(self.xcor(), self.ycor())

    def left(self):
        if self.xcor() > -340:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())
        else:
            self.goto(self.xcor(), self.ycor())


