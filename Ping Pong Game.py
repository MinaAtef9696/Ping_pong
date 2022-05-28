#import turtle module
import turtle
wind = turtle.Screen()
wind.title("Ping Pong App")
wind.bgcolor("black")
wind.setup(width=800 , height=600)
wind.tracer(0)  #Stops the window from updating automatically

#madrb 1
madrab1=turtle.Turtle() # create turtle object
madrab1.speed(0)   # control speed of madrab
madrab1.shape("square") # shape of madrab
madrab1.color("blue") # color of madrab
madrab1.shapesize(stretch_wid=5,stretch_len=1) # size of madrb
madrab1.penup() # no drawing when madrb moving
madrab1.goto(-350, 0) # postion of madrb
#madrb 2
madrab2=turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1) #default 20pixel height * 20pixels width
madrab2.penup()
madrab2.goto(350, 0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0) # ball start from the middle of screen
ball.dx=0.2  # ball move by 2.5 on x and Y cordinate
ball.dy=0.2

#Score
score1= 0
score2= 0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1 : 0 Player 2 : 0" , align="center" , font=("courier",24,"normal"))

#function
def madrab1_up():
    y=madrab1.ycor()     # get y cordinate of madrab 1
    y+=20                # increase y by 20 pixels
    madrab1.sety(y)

def madrab1_down():
    y=madrab1.ycor()
    y-=20
    madrab1.sety(y)

def madrab2_up():
    y=madrab2.ycor()
    y+=20
    madrab2.sety(y)

def madrab2_down():
    y=madrab2.ycor()
    y-=20
    madrab2.sety(y)

#keyboard_Binding
wind.listen()  # tell the window to expect keyboard input
wind.onkeypress(madrab1_up,"w")
wind.onkeypress(madrab1_down,"s")

wind.onkeypress(madrab2_up,"Up")
wind.onkeypress(madrab2_down,"Down")


#main game loop
while True:
    wind.update() # update the screen when the loop run

    #move tha ball
    ball.setx(ball.xcor() + ball.dx) # ball start from 0 and every time loops run --->+2.5 x axis
    ball.sety(ball.ycor() + ball.dy) # ball start from 0 and every time loops run --->+2.5 y axis

    #border check    Top border =+300px    bottom border=-300px    ball size=20px
    if ball.ycor() > 290: # if ball at top border
        ball.sety(290) # set y cordinate at 290
        ball.dy *=-1 # reverse direction by make 2.5 to -2.5

    if ball.ycor() < -290: # ball size is 20 pixels 290+10=300 so we choose 290 = end of y cordinate
        ball.sety(-290)
        ball.dy *=-1

    if ball.xcor() > 390:  # if ball at top right border
        ball.goto(0,0)  # return ball to middle of screen
        ball.dx *= -1  # reverse direction by make 2.5 to -2.5
        score1+=1
        score.clear()
        score.write("Player 1 : {} Player 2 : {}".format(score1,score2), align="center", font=("courier", 24, "normal"))


    if ball.xcor() < -390:  # if ball at top left border
        ball.goto(0,0)  # return ball to middle of screen
        ball.dx  *= -1  # reverse direction by make 2.5 to -2.5
        score2 += 1
        score.clear()
        score.write("Player 1 : {} Player 2 : {}".format(score1, score2), align="center",font=("courier", 24, "normal"))

        # tsadom madrab and ball

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1


