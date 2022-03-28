from turtle import Turtle
from time import sleep as time_sleep


class Paddle(Turtle):
    def __init__(self, cord: tuple[float, float]):
        super(Paddle, self).__init__(shape="square")
        self.penup()
        self.color('white')

        self.x, self.y = cord

        self.goto(self.x, self.y)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        if self.ycor() < 260:
            y_cor = self.ycor() + 20
            self.sety(y_cor)

    def down(self):
        if self.ycor() > -240:
            y_cor = self.ycor() - 20
            self.sety(y_cor)

    def reset_pos(self):
        self.goto(self.x, self.y)


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__(shape='circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

        # print(self.pos())

    def bounce(self, ball_direction):
        # Change ball's direction in the y axis
        if ball_direction == 'y':
            self.y_move *= -1
        # Will change the ball's direction on the x axis
        else:
            self.x_move *= -1
            self.ball_speed *= 0.09
    
    def reset_pos(self):
        time_sleep(0.3)

        self.ball_speed = 0.1

        self.goto(0, 0)
        self.bounce('x')


class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__(visible=False)
        self.color('white'), self.penup()
        
        self.bar1_score = 0
        self.bar2_score = 0
        
        self.font = ('Courier', 60, 'bold')
        
        self.update_score()

    def update_score(self):            
        self.goto(100, 200)
        self.write(self.bar2_score, align='center', font=self.font)
        self.goto(-100, 200)
        self.write(self.bar1_score, align='center', font=self.font)

    def b1_score(self):
        self.bar1_score += 1
        self.update_score()

    def b2_score(self):
        self.bar2_score += 1
        self.update_score()


class Deco:
    # Creates 4 Turtles and assigns it to all of the variables
    def show_intro():
        FONT = ('Courier', 60, 'bold')

        t1, t2, logo, logo_underline, line_u, line_d = [Turtle(visible=False) for _ in range(6)]

        line_u.pencolor("white"), line_d.pencolor("white")

        logo_underline.pensize(4)
                
        for turtle in t1, t2, logo, logo_underline:  
            pen_color = ""  
                        
            if turtle is t1: pen_color = 'aqua'
            elif turtle is t2: pen_color = "black"
            else: pen_color = "white"
            
            
            if turtle in (logo, logo_underline): # If turtle is one of 
                turtle.penup()
            
            elif turtle in (t1, t2):
                turtle.pensize(10)
                turtle.speed('fast')
            
            turtle.pencolor(pen_color)
        
        logo.sety(-120)
        logo.setx(20)
        logo.write(arg='PONG!', align='center', font=FONT)

        for _ in range(1):
            for turtle in (t1, t2):
                turtle.circle(radius=80)
                time_sleep(1)

        t1.clear(), t2.clear(), logo.clear()
        
        logo.sety(0)
        logo.write(arg='PONG!', align='center', font=FONT)

        logo_underline.goto(logo.xcor() - 120, logo.ycor())
        logo_underline.pendown()

        for _ in range(10):
            logo_underline.forward(20)
            time_sleep(0.06)

        time_sleep(1)
        logo.clear(), logo_underline.clear()


        # Drawing a line in the center
        line_u.seth(90)
        line_d.seth(270)


        while line_u.ycor() < 300 and line_u.ycor() > -300:
            line_u.forward(10)
            line_d.forward(10)
            time_sleep(0.04)

        logo.goto(0, 0)

        # DRAWING THE SCORE

        score_t = Turtle(visible=False)

        score_t.pencolor("white")
        score_t.penup()
        score_t.goto(100, 200)
        score_t.write(0, font=FONT)
        score_t.goto(-100, 200)
        score_t.write(0, font=FONT)
        time_sleep(0.800)
        score_t.clear()
