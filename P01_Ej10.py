from turtle import *

turt = Turtle()

centroX_1 = int(input('Introduce la coordenada X del centro del primero circulo: '))
centroY_1 = int(input('Introduce la coordenada Y del centro del primero circulo: '))

radio_1 = int(input('Introduce el radio del primer circulo: '))

centroX_2 = int(input('Introduce la coordenada X del centro del segundo circulo: '))
centroY_2 = int(input('Introduce la coordenada Y del centro del segundo circulo: '))

radio_2 = int(input('Introduce el radio del segundo circulo: '))

punto_x = int(input('Introduce la coordenada X del punto: '))
punto_y = int(input('Introduce la coordenada Y del punto: '))

turt.penup()
turt.goto(centroX_1, centroY_1)
turt.forward(radio_1)
turt.pendown()
turt.left(90)
turt.color("red")
turt.circle(radio_1)

turt.penup()
turt.goto(centroX_2, centroY_2)
turt.penup()
turt.forward(radio_2)
turt.pendown()
turt.left(90)
turt.color("blue")
turt.circle(radio_2)

turt.penup()
turt.goto(punto_x,punto_y)
if turt.distance(centroX_1,centroX_2)<=radio_1 and turt.distance(centroY_1,centroY_2)<=radio_2:
    turt.color("purple")
    print('morado')
else:
    if turt.distance(centroX_1,centroX_2)<=radio_1 and turt.distance(centroY_1,centroY_2)>radio_2:
        turt.color("red")
        print('rojo')
    else:
        if turt.distance(centroX_1,centroX_2)>radio_1 and turt.distance(centroY_1,centroY_2)<=radio_2:
            turt.color("blue")
            print('azul')
        else:
            turt.color("black")
            print('negro')
    
    
turt.pendown()
turt.dot()

