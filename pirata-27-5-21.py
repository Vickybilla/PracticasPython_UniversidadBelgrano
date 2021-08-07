""""Pirata barba Negra ( màs de 2 pasos a las izquierda o a la derecha y se cae): 
rampa para subir a su barco (5 pasos de ancho y 15 de largo")leer por teclado un valor entero.
a) si el entero es par 1 paso hacia adelante
b)si el entero es impar , pero el entero - 1 es divisible por 4, el pirata da un paso  a la derecha
c)En otro caso , el pirata da un paso a la izquierda
d)utilizar un generador de numeros pseudo aleatorios para generar un nuevo entero y repetir a la partir del paso a
Condiciones de terminacion:
** introducciòn de un nùmero negativo ( es de suponer que el pirata se durmiò sobre la rampa)
**El pirata cae por un costado de la rampa y se ahoga
**El pirata logra abordar  a salvo su barco
Haga un programa que exhiba el avance del pirata en cada paso"""

from random import randint

numero_usuario =int(input("Ingrese un nùmero para empezar su tambaleada aventura "))
while numero_usuario<0:
    print("Parece que el pirata se ha quedado dormido en la rampa  intenta despertarlo ingresando otro nùmero ")
    numero_usuario =int(input("Ingrese un nùmero para empezar su tambaleada aventura "))

pasos_izq =3 #por la posicion inicial en la tabla
pasos_der= 3
pasos_adelante=0
#considerar punto en la tabla

while pasos_adelante <15 and pasos_der<5 and pasos_izq<5:
    if numero_usuario%2 ==0:
        pasos_adelante =pasos_adelante+1
        #para el while validar que iguale o supere lo pasos_adelante >=15
        print("El pirata avanzó" ,pasos_adelante, "pasos hacia adelante")
    elif numero_usuario %2 !=0 and (numero_usuario-1)%4==0:
        pasos_der= pasos_der+1
        pasos_izq=pasos_izq-1
        #para el while validar que iguale o supere lo pasos_der>2
        print("El pirata hizo" ,pasos_der, "pasos a la derecha ")
    elif numero_usuario %2 !=0 and (numero_usuario-1)%4!=0:
        pasos_izq=pasos_izq+1
        pasos_der= pasos_der-1
        #para el while validar que iguale o supere lo pasos_izq>2
        print("El pirata hizo" ,pasos_izq, "pasos a la izquierda ")
    aleatorio=randint(-10,1000) 
    print("nùmero aleatorio",aleatorio)
    numero_usuario=aleatorio

if pasos_adelante >=15: 
    print(" Este viaje tambaleado ha sido un èxito! El Pirata llegó a su Barco!")
elif pasos_der>=5:
    print("El pirata se ha caído de la rampa por el lado derecho y se ha ahogado :(")
elif pasos_izq>=5:
    print("El pirata se ha caído de la rampa por el lado izquierdo y se ha ahogado :(") 