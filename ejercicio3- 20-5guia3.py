"""reemplazar por puntos las vocales de un mensaje ingresado por el usuario """


def reemplazo_vocales(msj):
    vocales="a,á,e.é,i,í,o,ó,u,ú"
    for vocal in vocales:
        msj=msj.replace(vocal," . ")
    print(msj)

mensaje=input("Ingrese su palabra o frase para jugar ahorcado ").lower()

reemplazo_vocales(mensaje)