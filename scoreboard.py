from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.x = 0
        self.y = 270
        self.start()

    def start(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(self.x, self.y)
        self.new_score()

    def new_score(self):
        self.clear()
        self.score += 1
        text = "Score: " + str(self.score)
        self.write(text, move=False, align="center", font=('Arial', 12, 'normal'))
