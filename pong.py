
import turtle #to add graphics n stuff
import winsound
import time

# Function to display countdown
def display_countdown():
    countdown = turtle.Turtle()
    countdown.speed(0)
    countdown.color("yellow")
    countdown.penup()
    countdown.hideturtle()
    countdown.goto(0, 0)

    countdown.write("3", align="center", font=("Courier", 36, "normal"))
    time.sleep(1)
    countdown.clear()

    countdown.write("2", align="center", font=("Courier", 36, "normal"))
    time.sleep(1)
    countdown.clear()

    countdown.write("1", align="center", font=("Courier", 36, "normal"))
    time.sleep(1)
    countdown.clear()

    countdown.write("Go!", align="center", font=("Courier", 36, "normal"))
    time.sleep(1)
    countdown.clear()

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)

display_countdown()

win.tracer(0)
turtle.bgpic("pongbg1.png")

#Score - we get a point when the ball goes off the screen
score_a = 0
score_b = 0

#Paddle A (left)
paddle_a=turtle.Turtle()
paddle_a.speed(0) #speed of animation - sets speed to max possible speed
paddle_a.shape("square") #built-in
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #turtles draw lines as they are moving, but we don't need that
paddle_a.goto(-350,0)

#Paddle B (right)
paddle_b=turtle.Turtle()
paddle_b.speed(0) #speed of animation - sets speed to max possible speed
paddle_b.shape("square") #built-in
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() #turtles draw lines as they are moving, but we don't need that
paddle_b.goto(350,0)

#Ball
ball=turtle.Turtle()
ball.speed(0) #speed of animation - sets speed to max possible speed
ball.shape("circle") #built-in
ball.color("white")
ball.penup() #turtles draw lines as they are moving, but we don't need that
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2 #everytime the ball moves it moves by 0.4 px, dx= xcoord; dy=y coord
#x=0.4 y=0.4 - moves up diagonally

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(20, 260)
pen.write("Player A: 0     Player B: 0", align = "center", font=("Courier",24,"normal"))

#function
def paddle_a_up():
    y = paddle_a.ycor() #return's objs current y coordinate - builtin
    y +=30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #return's objs current y coordinate - builtin
    y -=30
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #return's objs current y coordinate - builtin
    y +=30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() #return's objs current y coordinate - builtin
    y -=30
    paddle_b.sety(y)

#Keyboard binding
win.listen() #listens for keyboard inputs
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up") #arrow keys for paddle b
win.onkeypress(paddle_b_down,"Down")

max_score = 5

#Main game loop - every game needs it
while True:
    win.update()
    #Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border checking - comparing the ball's y coord - once it hits the border, it has to bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverses the direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        winsound.PlaySound("point.wav", winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}     Player B: {}".format(score_a,score_b), align = "center", font=("Courier",24,"normal"))

    if ball.xcor() < -390:
        winsound.PlaySound("point.wav", winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}     Player B: {}".format(score_a,score_b), align = "center", font=("Courier",24,"normal"))


    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 90 and ball.ycor() > paddle_b.ycor() - 90):
        winsound.PlaySound("pongw.wav", winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 90 and ball.ycor() > paddle_a.ycor() - 90):
        winsound.PlaySound("pongw.wav", winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *= -1    

    #Winner
    if score_a == max_score or score_b == max_score:
        # Clear the screen
        win.clear()
        winsound.PlaySound("win.wav", winsound.SND_ASYNC)

        # Display the winner
        winner = "Player A" if score_a == max_score else "Player B"
        win.title(f"{winner} Wins!")
        win.bgcolor("black")

        # Display the winning message
        win_msg = turtle.Turtle()
        win_msg.speed(0)
        win_msg.color("yellow")
        win_msg.penup()
        win_msg.hideturtle()
        win_msg.goto(0, 0)
        win_msg.write(f"{winner} Wins!", align="center", font=("Courier", 36, "normal"))
        break
# Close the turtle graphics window when clicked
win.exitonclick()
