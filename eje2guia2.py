"""Ejercicio2:
Diseña un programa que solicite la lectura de un número entre 0 y 10 (ambos inclusive).
Si el usuario teclea un número fuera del rango válido, el programa solicitará nuevamente 
la introducción del valor cuantas veces sea menester."""

nro = int(input(" ingrese un número entre 0 y 10 :  "))

while nro < 0 or nro >10:
    print (" El número ingresado no se encuentra dentro del rango ")
    nro=int(input("Ingrese un número entre 0 y 10:  "))

if nro in range (1,10):
    print("felicitaciones, cumpliste la consigna!!")