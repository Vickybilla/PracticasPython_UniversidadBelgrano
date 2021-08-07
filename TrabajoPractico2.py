"""Trabajo práctico #2
Adivinar el número:
El juego consiste en adivinar un número de 3 dígitos. El programa
deberá permitir al usuario ingresar un número, si este número es
menor o mayor que el número a adivinar se deberá mostrar el
mensaje adecuado y permitir el ingreso de un nuevo número. Se
permitirán sólo 3 intentos. Si el número coincide con el número a
adivinar, el programa termina y mostrará el mensaje adecuado"""

from random import randint

def adivinar_numero(numero):
    numero_pc = randint(000,1000)
    if numero == numero_pc:
        return True,print(" Adivinaste el Número")
    else:
        return False,print(" No adivinaste," ,numero_pc, "era el número a adivinar")

"""

resultado = None
intentos = 3
while intentos and not resultado:
    intentos -= 1
    try:
        numero = int(input("ingresa un numero: "))
        resultado = 1
        for i in range(numero, 1, -1):
            resultado = resultado * i
    except ValueError:
        print("La entrada es incorrecta: escribe un numero entero")

if (resultado):
    print(resultado)"""


intentos = 3
print(intentos)
num_usuario = print(input(" Ingrese un número de tres cifras  "))
while intentos>3:
    intentos-=1
    num_usuario = print(input(" Ingrese un número de tres cifras  "))
    
print(intentos)




