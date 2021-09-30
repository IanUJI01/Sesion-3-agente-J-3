from turtle import *

turt = Turtle()

l = int(input('Introduce el lado del triangulo: '))

altura = 3**0.5/2*l
print(altura)
turt.forward(l/2)
turt.goto(0,altura)
turt.goto(-l/2,0)
turt.home()
turt.penup()
turt.goto(-l/3,-30)
cent_y = altura/3
turt.penup()
turt.goto(0,cent_y)
turt.dot()
turt.goto(-l/4,-20)
turt.write('Las coordenadas del centroide son: (0,{0})'.format(round(cent_y,2)))
