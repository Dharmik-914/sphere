import turtle
import time

# Setup screen
win = turtle.Screen()
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)
win.title("Bouncing Ball Game")

# Game state variables
game_started = False
game_over = False
score = 0
high_score = 0

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.color("white")
paddle.penup()
paddle.goto(0, -250)
paddle.shape("square")
paddle.shapesize(1, 5)  # Make paddle wider
paddle.hideturtle()  # Hide until game starts

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 1.5  # Reduced ball speed
ball.dy = -1.5  # Reduced ball speed
ball.hideturtle()  # Hide until game starts

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 16, "bold"))

# Start/Restart button
button = turtle.Turtle()
button.speed(0)
button.shape("square")
button.color("green")
button.shapesize(2, 8)
button.penup()
button.goto(0, 0)

# Button text
button_text = turtle.Turtle()
button_text.speed(0)
button_text.color("white")
button_text.penup()
button_text.hideturtle()
button_text.goto(0, -15)
button_text.write("START GAME", align="center", font=("Courier", 16, "bold"))

# End game score card
score_card = turtle.Turtle()
score_card.speed(0)
score_card.color("white")
score_card.penup()
score_card.hideturtle()

# Move paddle functions
def move_left():
    if game_started and not game_over:
        x = paddle.xcor()
        if x > -250:
            paddle.setx(x - 30)

def move_right():
    if game_started and not game_over:
        x = paddle.xcor()
        if x < 250:
            paddle.setx(x + 30)

# Start/Restart game function - improved click detection
def button_click(x, y):
    global game_started, game_over, score
    
    # Check if click is within button bounds
    button_x = button.xcor()
    button_y = button.ycor()
    button_width = 80  # 8 * 10 (shapesize 8 * default size 10)
    button_height = 20  # 2 * 10 (shapesize 2 * default size 10)
    
    if (button_x - button_width <= x <= button_x + button_width and 
        button_y - button_height <= y <= button_y + button_height):
        
        # Clear any existing game over message
        score_card.clear()
        
        # Reset game state
        game_started = True
        game_over = False
        score = 0
        
        # Hide button
        button.hideturtle()
        button_text.clear()
        
        # Reset and show game elements
        ball.goto(0, 0)
        paddle.goto(0, -250)
        paddle.showturtle()
        ball.showturtle()
        
        # Reset score display
        pen.clear()
        pen.write(f"Score: 0", align="center", font=("Courier", 16, "bold"))

# Show game over and score card
def show_game_over():
    global game_over, high_score
    
    game_over = True
    
    # Update high score if needed
    if score > high_score:
        high_score = score
    
    # Hide game elements
    ball.hideturtle()
    
    # Show score card
    score_card.clear()
    score_card.goto(0, 100)
    score_card.write("GAME OVER", align="center", font=("Courier", 24, "bold"))
    score_card.goto(0, 40)
    score_card.write(f"Final Score: {score}", align="center", font=("Courier", 18, "normal"))
    score_card.goto(0, -20)
    score_card.write(f"High Score: {high_score}", align="center", font=("Courier", 18, "normal"))
    
    # Display restart button
    button.goto(0, -100)
    button.showturtle()
    button_text.goto(0, -115)
    button_text.write("PLAY AGAIN", align="center", font=("Courier", 16, "bold"))

# Set up keyboard and click bindings
win.listen()
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")
win.onscreenclick(button_click)

# Main game loop
while True:
    win.update()
    
    if game_started and not game_over:
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
            show_game_over()
    
    # Add a slight delay to make it more playable
    time.sleep(0.01)
