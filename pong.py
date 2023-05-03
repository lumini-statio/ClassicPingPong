import turtle

window = turtle.Screen()
window.title('PingPong')
window.bgcolor('black')
window.setup(width = 800, height = 600)
window.tracer(0)

#configurando jugadorA
jugadorA = turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape('square')
jugadorA.color('white')
jugadorA.penup()
jugadorA.goto(-350,0)
jugadorA.shapesize(stretch_wid=5,stretch_len=1)


#configurando jugadorB
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape('square')
jugadorB.color('white')
jugadorB.penup()
jugadorB.goto(350,0)
jugadorB.shapesize(stretch_wid=5,stretch_len=1)


#configurando la pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape('square')
pelota.color('white')
pelota.penup()
pelota.goto(0,0)
pelota.dx = 1.8
pelota.dy = 1.8


#division de cancha
division = turtle.Turtle()
division.color('white')
division.goto(0,400)
division.goto(0,-400)


#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
contA = 0
contB = 0
pen.write(f'jugador A: {contA}       jugador B: {contB}', align = 'center', font=('Courier', 24, 'normal'))


#funciones
def jugadorA_up():
    y = jugadorA.ycor()
    y += 20
    jugadorA.sety(y)
    
def jugadorA_down():
    y = jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)

def jugadorB_up():
    y = jugadorB.ycor()
    y += 20
    jugadorB.sety(y)
    
def jugadorB_down():
    y = jugadorB.ycor()
    y -= 20
    jugadorB.sety(y)


#teclado
window.listen()

#jugadorA
window.onkeypress(jugadorA_up, 'w')
window.onkeypress(jugadorA_down, 's')

#jugadorB
window.onkeypress(jugadorB_up, 'Up')
window.onkeypress(jugadorB_down, 'Down')


while True:
    window.update()
    
    pelota.setx(pelota.xcor()+pelota.dx)
    pelota.sety(pelota.ycor()+pelota.dy)
    
    #techo y piso
    if pelota.ycor() > 290:
        pelota.dy *= -1
        
    if pelota.ycor() < -290:
        pelota.dy *= -1
        
        
        
    #bordes laterales
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        contA += 1
        pen.clear()
        pen.write(f'jugador A: {contA}       jugador B: {contB}', align = 'center', font=('Courier', 24, 'normal'))
    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        contB += 1
        pen.clear()
        pen.write(f'jugador A: {contA}       jugador B: {contB}', align = 'center', font=('Courier', 24, 'normal'))
        
    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
        and (pelota.ycor() < jugadorB.ycor() + 50
        and pelota.ycor() > jugadorB.ycor() - 50)):
        pelota.dx *= -1
        
    if ((pelota.xcor() < -340 and pelota.xcor() > -350)
        and (pelota.ycor() > jugadorA.ycor() - 50
        and pelota.ycor() < jugadorA.ycor() + 50)):
        pelota.dx *= -1                            