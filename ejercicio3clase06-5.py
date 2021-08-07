"""Diseña un programa que lea un número por teclado y muestre por pantalla el mensaje 
<<El número es negativo>> sólo si el número es menor que 0, en otro caso mostrar el número"""

numero= int(input("Ingrese un número  "))

if numero <0:
    print("<<El número es negativo>>")
elif numero == 0:
    print("0 no es positivo ni negativo")
else:
    print(numero)
