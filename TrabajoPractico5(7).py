"""Trabajo Práctico # 7
Interceptar Mensajes Cifrados
El agente 0069 lleva años utilizando un método de codificación de mensajes secretos.
Si X es el mensaje original, éste se codifica en dos etapas:
1. X se transforma en X' reemplazando cada sucesión de caracteres consecutivos
que no sean vocales por su imagen especular.
X' se transforma en la sucesión de caracteres X'' obtenida al ir tomando sucesivamente:
el primer carácter de X', luego el último, luego el segundo, luego el penúltimo, etc.
Por ejemplo, para X = "Bond, James Bond", resultan:
X' = "BoJ ,dnameB sodn"
y
X'' = "BnodJo s, dBneam"
Lo que el pobre agente 0069 no sabe es que el señor Fon Noiman ha analizado algunos
mensajes cifrados y ha dado con el mecanismo que está utilizando. Lo único que le
queda a Fon Noiman es hacer el programa que, dado un mensaje cifrado, lo descifre.
Entrada
Un mensaje cifrado según el algoritmo anterior. El agente 0069 utiliza un teclado inglés,
por lo que ninguna vocal tendrá tilde y no tiene ñ.
Salida
Se mostrará el mensaje cifrado leído de la entrada y a continuación aparecerá "=>"entre
dos espacios y el mensaje original descifrado.
Entrada de ejemplo
Ejemplos:
BnodJo s, dBneam
aueoi
E. .n.ualn cnhuag aMda rle
Aauirnedleiua nBo
Salida de ejemplo
BnodJo s, dBneam => Bond, James Bond
aueoi => aeiou
E. .n.ualn cnhuag aMda rle => En un lugar de la Mancha...
Aauirnedleiua nBo => Aureliano Buendi"""

mensaje="Bond, James Bond"

#1. X se transforma en X' reemplazando cada sucesión de caracteres consecutivos
#que no sean vocales por su imagen especular.
def invertir_cadena(cadena):
    return cadena[::-1]
#primerEstapa
def prima_encode(mensaje):
    i=0
    primer_encode=""
    vocales="aeiou"
    desde=0
    while i<len(mensaje):
        while i <len(mensaje) and mensaje [i]not in vocales:
            i+=1
        hasta = i
        i +=1
        auxiliar= mensaje[desde+1:hasta]
        primer_encode=primer_encode + mensaje[desde]+ auxiliar [::-1]
        desde= hasta
    if mensaje[-1]in vocales:
        primer_encode=primer_encode + mensaje [-1]
        return primer_encode

def segundo_encode(mensaje):
    i=0
    k=len(mensaje)-1
    second_encode=""
    while i<k:
        second_encode=second_encode+mensaje[i]+ mensaje[k]
        i= i +1
        k= k-1
    return second_encode

def cifrar(mensaje):
    mensaje1=prima_encode(mensaje)
    mensaje2=segundo_encode(mensaje1)
    return mensaje2


cripto= "Bons, James Bond"

print(cifrar(cripto))

def descifra1(mensaje):
    parte1=""
    parte2=""
    i=0
    k=0
    t=len(mensaje)-1
    while i <len (mensaje)-1:
        a=mensaje[i]
        b=mensaje[i+1]
        parte1 = parte1 + a
        parte2 = b + parte2
        i = i +2
    descifra= parte1+parte2
    return descifra

def descrifrado(mensaje):
    texto1=descifra1(mensaje)
    texto2=segundo_encode(texto1)
    return texto2