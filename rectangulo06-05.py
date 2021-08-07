"""hacer un programa para permitir ingresar el alto y ancho de un rectángulo y con esos datos dibujar un rectángulo de *"""

base= int(input("Por favor ingresar base del rectángulo  "))
altura =int(input("Por favor ingresar altura del rectángulo  "))
asterisco= "*"


for a in range(altura):
    for b in range(base):
        print(asterisco,end="")
    print()


