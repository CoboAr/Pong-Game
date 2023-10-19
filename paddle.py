from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, tuple=()):
        super ().__init__ ()
        self.x = tuple[0]
        self.y  =tuple[1]
        self.penup ()
        self.shape ("square")
        self.color ("white")
        self.shapesize (stretch_wid=5, stretch_len=1)
        self.goto (self.x, self.y)

    def go_up_r(self):
        new_y = self.ycor () + 20
        self.goto (self.xcor (), new_y)

    def go_down_r(self):
        new_y = self.ycor () - 20
        self.goto (self.xcor (), new_y)

    def go_up_l(self):
        new_y = self.ycor () + 20
        self.goto (self.xcor (), new_y)

    def go_down_l(self):
        new_y = self.ycor () - 20
        self.goto (self.xcor (), new_y)


