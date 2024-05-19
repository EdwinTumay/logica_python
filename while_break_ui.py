import random
import turtle

ventana = turtle.Screen()
ventana.title("Carrera de tortugas")
ventana.bgcolor('lightblue')
ventana.setup(width=800, height=600)

tortuga1 = turtle.Turtle()
tortuga1.shape("turtle")
tortuga1.color("red")
tortuga1.penup()
tortuga1.goto(-300,100)

tortuga2 = turtle.Turtle()
tortuga2.shape("turtle")
tortuga2.color("blue")
tortuga2.penup()
tortuga2.goto(-300,0)

meta = 300

while True:
    avance_tortuga_1 = random.randint(1,20)
    avance_tortuga_2 = random.randint(1,20)

    tortuga1.forward(avance_tortuga_1)
    tortuga2.forward(avance_tortuga_2)

    print(f"El caracol 1 avanza {avance_tortuga_1} para un total de {tortuga1.xcor()}")
    print(f"El caracol 1 avanza {avance_tortuga_2} para un total de {tortuga2.xcor()}")
    print(f"---------------------------------")

    if tortuga1.xcor() >= meta or tortuga2.xcor() >= meta:
        break

if tortuga1.xcor() > tortuga2.xcor():
    print("El caracol 1 ha ganado")
elif tortuga1.xcor() > tortuga2.xcor():
    print("El caracol 2 ha ganado")
else:
    print("Esto es un empate")
ventana.exitonclick()