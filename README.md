import turtle
# Setup screen
win = turtle.Screen()
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.color("white")
paddle.penup()
paddle.goto(0, -250)
paddle.shape("square")
paddle.shapesize(1, 5)  # Make paddle wider

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = -3

# Scoreboard
score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 16, "bold"))

# Move paddle
def move_left():
    x = paddle.xcor()
    if x > -250:
        paddle.setx(x - 30)

def move_right():
    x = paddle.xcor()
    if x < 250:
        paddle.setx(x + 30)

# Keyboard binding
win.listen()
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")

# Main game loop
while True:
    win.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1
    
    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1
    
    # Paddle collision
    if (ball.ycor() < -240 and ball.ycor() > -250) and \
       (ball.xcor() < paddle.xcor() + 50 and ball.xcor() > paddle.xcor() - 50):
        ball.sety(-240)
        ball.dy *= -1
        score += 1
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Courier", 16, "bold"))
    
    # Bottom border - game over condition
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
        score = 0
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Courier", 16, "bold"))
