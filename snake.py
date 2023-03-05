from turtle import Turtle


class Snake:

    def __init__(self):
        self.start_x = 0
        self.start_y = 0
        self.segments = []
        self.create_snake()
        self.move_distance = 20
        self.head = self.segments[0]

    def create_snake(self):
        for n in range(3):
            new_turtle = Turtle(shape="square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(x=self.start_x, y=self.start_y)
            self.start_x -= 20
            self.segments.append(new_turtle)

    def move(self):
        for n in range(len(self.segments) - 1, 0, -1):
            position = self.segments[n - 1].pos()
            self.segments[n].goto(position)
        self.head.forward(self.move_distance)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
