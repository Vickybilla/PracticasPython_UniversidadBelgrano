"""Ejercicio 3:
Escribir un programa que muestre, de a diez números por línea y separados por un 
blanco, todos los números entre 100 y 1000 que sean divisibles por 5 y 6"""
#número de partida 5 por seer el menor múltiplo posible de alguno de los valores dados
n = 5
#usamos contador para la posterior impresion (parte de 1)
cont=1
#rango hasta 1000 inclusive
for n in range (100,1001):
    #condición divisible entero por 5 y 6 al mismo tiempo
    if n % 5 == 0 and n % 6 == 0:
        #impresion dada por contador con un salto hasta el valor 10
        print (n, end = " ")
        #si el contador es mator o igual a 10 ...
        if cont >= 10:
            #imprimir valores
            print()
            cont =1
        else:
            #sino sumar 1 al contador hasta que sea mayor o igual a 10 e imprima los valores en una línea
            cont = cont +1
