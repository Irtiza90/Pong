from turtle import Screen
from components import Score, Deco, Ball, Paddle, time_sleep


screen = Screen()
screen.bgcolor('black')
screen.title('Pong')
screen.setup(width=800, height=600)

Deco.show_intro()

screen.tracer(0)

bar1 = Paddle((350, 0))
bar2 = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()

screen.onkeypress(bar1.up, key='Up')
screen.onkeypress(bar1.down, key='Down')
screen.onkeypress(bar2.up, key='w')
screen.onkeypress(bar2.down, key='s')

reset_pos = lambda: (ball.reset_pos(), bar1.reset_pos(), bar2.reset_pos())
game_is_on = True


while game_is_on:
    ball.move_ball()

    ball_x, ball_y = ball.pos()

    if ball_y > 280 or ball_y < -280:
        ball.bounce('y')

    elif ball.distance(bar1) < 50 and ball_x > 320 or ball.distance(bar2) < 50 and ball_x < -320:
        ball.bounce('x')

    # Detect when A Bar Missed The Ball

    # For Bar 1 (On Right Side)
    # Resetting position of bar 1 & 2 after someone scores a point
    if ball_x > 380:
        reset_pos()
        score.b1_score()

    # For Bar 2 (On Left Side)
    elif ball_x < -380:
        reset_pos()
        score.b2_score()

    screen.update()        
    time_sleep(0.050)

