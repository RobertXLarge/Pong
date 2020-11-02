import turtle

#ventana
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

#Marcador
marcador1 = 0
marcador2 = 0

#Player 1
Player1 = turtle.Turtle()
Player1.speed(0)
Player1.shape("square")
Player1.shapesize(stretch_wid = 5, stretch_len = 1)
Player1.color("red")
Player1.penup()
Player1.goto(-350, 0)

#Player 2
Player2 = turtle.Turtle()
Player2.speed(0)
Player2.shape("square")
Player2.shapesize(stretch_wid = 5, stretch_len = 1)
Player2.color("red")
Player2.penup()
Player2.goto(350, 0)

#Pelota
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("Blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5


#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.color("black")
pen.write("Jugador A: 0         Jugador B: 0", align="center", font=("courier", 20, "normal"))

#Funnciones
def Player1_up():
    y = Player1.ycor()
    y += 40
    Player1.sety(y)

def Player1_down():
    y = Player1.ycor()
    y += -40
    Player1.sety(y)

def Player2_up():
    y = Player2.ycor()
    y += 40
    Player2.sety(y)

def Player2_down():
    y = Player2.ycor()
    y += -40
    Player2.sety(y)

#teclado
wn.listen()
wn.onkey(Player1_up, "w")
wn.onkey(Player1_down, "s")
wn.onkey(Player2_up, "Up")
wn.onkey(Player2_down, "Down")


while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Colision bordes Y
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    #Colosion bordes X
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        marcador1 += 1
        pen.clear()
        pen.write("Jugador A: {}         Jugador B: {}".format(marcador1,marcador2), align="center", font=("courier", 20, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        marcador2 += 1
        pen.clear()
        pen.write("Jugador A: {}         Jugador B: {}".format(marcador1,marcador2), align="center", font=("courier", 20, "normal"))

    #Colision jugadores
    if ((ball.xcor() > 340 and ball.xcor() < 350) and 
    (ball.ycor() < Player2.ycor() + 50 and 
    ball.ycor() > Player2.ycor() - 50)):
        ball.dx *= -1
    
    if ((ball.xcor() < -340 and ball.xcor() > -350) and 
    (ball.ycor() < Player1.ycor() + 50 and 
    ball.ycor() > Player1.ycor() - 50)):
        ball.dx *= -1