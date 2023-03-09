from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.high_score = 0
        self.start()

    def start(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        file = open("highscore.txt")
        contents = file.read()
        self.high_score = int(contents)
        file.close()
        self.new_score()

    def new_score(self):
        self.clear()
        self.score += 1
        if self.score >= self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as file:
                txt = str(self.high_score)
                file.write(txt)
        text = "Score: " + str(self.score) + "    Highscore: " + str(self.high_score)
        self.write(text, move=False, align="center", font=('Arial', 18, 'normal'))

    def reset_score(self):
        self.score = -1
        self.new_score()
