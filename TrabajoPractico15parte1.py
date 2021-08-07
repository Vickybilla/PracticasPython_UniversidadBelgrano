"""Trabajo práctico 15
En los juegos de naipes, una carta tiene dos atributos: un valor (1,2,3,4,5,6,7,8,9,10,J,Q,K) y
un palo (♠, ♣,♥, ♦). En un programa, el valor puede ser representado como un número del
1 al 13, y el palo como un carácter ('T','D','C','P'). Una carta puede ser representada como
una tupla de dos elementos: (valor,palo), por ejemplo: (5,'T') representa la carta 5 de trébol.
El as se representa por 1, y la J,Q, y K como 11, 12, 13. En el juego de póker, una mano
tiene 5 cartas, lo que en un programa vendría a ser un conjunto de cinco tuplas, por
ejemplo:
mano = {(1, 'P'), (1, 'C'), (1, 'T'), (13, 'D'), (12, 'P')}"""


import random

def generarMazo():
    mazo= []
    for nro in range (1,14):
        for palo in ["T","P","D","C"]:
            mazo.append((nro,palo))
    return mazo

def generarMano(mazo):
    mano = set()
    while len(mano)<=5:
        mano.add(random.choice(mazo)) 
    return mano

mazoDeCartas = generarMazo()
mano = generarMano(mazoDeCartas)
#print(mano)
#lista = list(mano)
#random.shuffle(lista)

"""1) Un full es una mano en que tres cartas tienen el mismo valor, y las otras dos tienen otro
valor común. Por ejemplo, A♠ A♥ 6♣ A♦ 6♦ es un full (tres ases y dos seis), pero 2♣
A♥ Q♥ A♦ 6♦ no. Escriba una función que indique si la mano es un full.
>>> mano1 = {(1, 'P'), (1, 'C'), (6, 'T'), (1, 'D'), (6, 'D')}
>>> mano2 = {(2, 'T'), (1, 'C'), (12, 'C'), (1, 'D'), (6, 'D')}
>>> esFull(mano1)
True
>>> esFull(mano2)
False"""

def es_full (mano):
    manodict=dict(mano)
    palocolor=list(set(manodict.values()))




"""2) Un color es una mano en que todas las cartas tienen el mismo palo. Por ejemplo, 8♠ K♠
4♠ 9♠ 2♠ es un color (todas las cartas son picas), pero Q♣ A♥ 5♥ 2♥ 2♦ no lo es.
Escriba la función que indique si la mano es un color:
>>> mano1 = {(8, 'P'), (13, 'P'), (4, 'P'), (9, 'P'), (2, 'P')}
>>> mano2 = {(12, 'T'), (1, 'C'), (5, 'C'), (2, 'C'), (2, 'D')}
>>> esColor(mano1)
True
>>> esColor(man2)
False"""

mano1 = {(8, 'P'), (13, 'P'), (4, 'P'), (9, 'P'), (2, 'P')}

def es_color(mano):
    manodict=dict(mano)
    palocolor=list(set(manodict.values()))
    if len(palocolor)==1 :
        return True
    else:
        return False

print(es_color(mano1))

"""
3) Una escalera es una mano en que las cartas tienen valores consecutivos. Por ejemplo, 4♠
7♥ 3♥ 6♣ 5♣ es una escalera (tiene los valores 3, 4, 5, 6 y 7), pero Q♣ 7♥ 3♥ Q♥ 5♣ no
lo es.
Escriba la función que indique si la mano es una escalera:
>>> mano1 = {(4, 'P'), (7, 'C'), (3, 'C'), (6, 'T'), (5, 'T')}
>>> mano2 = {(12, 'T'), (7, 'C'), (3, 'C'), (12, 'C'), (5, 'T')}
>>> esEscalera(mano1)True
>>> esEscalera(mano2)
False"""


mano1a = {(4, 'P'), (7, 'C'), (3, 'C'), (6, 'T'), (5, 'T')}
mano2 = {(12, 'T'), (7, 'C'), (3, 'C'), (12, 'C'), (5, 'T')}


def es_escalera(mano):
    manodict=dict(mano)
    manosort=sorted(manodict.keys())
    isescalera= list(range(min(manosort),min(manosort)+5))
    if isescalera == manosort:
        return True
    else:
        return False


print(es_escalera(mano2))

"""4) Una escalera de color es una escalera en la que todas las cartas tienen el mismo palo. Por
ejemplo, 4♦ 7♦ 3♦ 6♦ 5♦ es una escalera de color (son sólo diamantes, y los valores 3, 4,
5, 6 y 7 son consecutivos).
Escriba la función que indique si la mano es una escalera de color:
>>> mano1 = {(4, 'P'), (7, 'C'), (3, 'C'), (6, 'T'), (5, 'T')}
>>> mano2 = {(8, 'P'), (13, 'P'), (4, 'P'), (9, 'P'), (2, 'P')}
>>> mano3 = {(4, 'D'), (7, 'D'), (3, 'D'), (6, 'D'), (5, 'D')}
>>> esEscaleraDeColor(mano1)
False
>>> esEscaleraDeC(mano2)
False
>>> es_escalera_de_color(mano3)
True"""

def es_escalera_color (mano):
    if es_escalera(mano)and es_color(mano):
        return True
    else:
        return False



mano4 = {(5, 'P'), (6, 'P'), (7, 'P'), (4, 'P'), (3, 'P')}
print(es_escalera_color(mano4))