from turtle import Turtle

class Game(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.draw_walls()

    def draw_walls(self):
        self.goto(-270, -270)
        self.pendown()
        for n in range(4):
            self.draw_wall()

    def draw_wall(self):
        self.forward(270*2)
        self.left(90)

    def over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align="center", font=('Arial', 24, 'normal'))