# Pong in Python 3
# By @ThePowerty
import turtle
import winsound
import time

# Configuración de la ventana
wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=1000, height=600)
wn.tracer(0)

# Jugador A
player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape('square')
player_a.color('white')
player_a.shapesize(stretch_wid=6, stretch_len=1)
player_a.penup()
player_a.goto(-450, 0)

# Jugador B
player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape('square')
player_b.color('white')
player_b.shapesize(stretch_wid=6, stretch_len=1)
player_b.penup()
player_b.goto(450, 0)

# Bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

# Puntuaciones

score_a = 0
score_b = 0

score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write('Player A: 0  Player B: 0', align="center", font=("Courier", 24, "normal"))


# Funciones de movimiento de jugadores

def player_a_up():
    y = player_a.ycor()
    if y < 240:
        player_a.sety(y + 20)

def player_a_down():
    y = player_a.ycor()
    if y > -240:
        player_a.sety(y -20)

def player_b_up():
    y = player_b.ycor()
    if y < 240:
        player_b.sety(y + 20)

def player_b_down():
    y = player_b.ycor()
    if y > -240:
        player_b.sety(y - 20)

# Controles del teclado
wn.listen()

wn.onkeypress(player_a_up, 'w')
wn.onkeypress(player_a_down, 's')

wn.onkeypress(player_b_up, 'Up')
wn.onkeypress(player_b_down, 'Down')

player = ""
winner = turtle.Turtle()
winner.speed(0)
winner.color('white')
winner.penup()
winner.hideturtle()
winner.goto(0, 0)

# Bucle principal
while True:
    wn.update()

    # Mover al bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Colision con bordes
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score.clear()
        score.write(f'Player A: {score_a}  Player B: {score_b}', align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.write(f'Player A: {score_a}  Player B: {score_b}', align="center", font=("Courier", 24, "normal"))


    # Choque de bola con las palas
    if (ball.xcor() > 430 and ball.xcor() < 450) and (ball.ycor() < player_b.ycor() + 50 and ball.ycor() > player_b.ycor() - 50):
        ball.setx(430)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (ball.xcor() < -430 and ball.xcor() > -450) and (ball.ycor() < player_a.ycor() + 50 and ball.ycor() > player_a.ycor() - 50):
        ball.setx(-430)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Obtener ganador
    if score_a == 5:
        player = "Player A"
        winner.write(f'¡El ganador es: {player}!', align="center", font=("Courier", 24, "normal"))
        time.sleep(7)
        break
    elif score_b == 6:
        player = "Player B"
        winner.write(f'¡El ganador es: {player}!', align="center", font=("Courier", 24, "normal"))
        time.sleep(7)
        break
