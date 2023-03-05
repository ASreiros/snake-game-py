from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.start()

    def start(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.new_score()

    def new_score(self):
        self.clear()
        self.score += 1
        text = "Score: " + str(self.score)
        self.write(text, move=False, align="center", font=('Arial', 18, 'normal'))


