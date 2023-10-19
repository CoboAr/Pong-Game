from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super ().__init__ ()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.increase_speed =0.1
    def move(self):
        newx=self.xcor()+self.x_move
        newy=self.ycor()+self.y_move
        self.goto(newx,newy)

    def bounce_y(self):
        self.y_move = self.y_move * -1

    def bounce_x(self):
        self.x_move = self.x_move * -1
        self.increase_speed *= 0.9

    def restart(self):
        self.home()
        self.increase_speed = 0.1
        self.x_move = self.x_move * -1


