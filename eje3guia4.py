"""Diseñar una función que determine si una lista de nùmeros enteros está ordenada de menor
a mayor y cada número i entre el 1 y n aparece exactamente i veces

Ejemplo = 
para n= 5
esTelescopio(5,[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5])-->verdadero"""

def lista_telescopio(n):
    listaaux = []
    n=5
    for i in range(n+1):
        for num in range(i):
            listaaux.append(i)
    return listaaux

def es_telescopio(num,lista):
    lista_ordenada=sorted(lista)
    return lista_telescopio(num)==lista_ordenada

numero1 =5
lista1=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
numero2 = 4
lista2=[1,2,2,3,6,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,3]

print(es_telescopio(numero2,lista2))
