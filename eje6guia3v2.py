"""Ejercicio 6:
Escribir un programa que retorne el número que le corresponde a una letra en mayúscula 
de acuerdo al teclado telefónico (ver figura)
Ejercicio 7:
Escribir un programa que ingrese un número telefónico como un string y convierta los
caracteres a el dígito correspondiente, ejemplo:
1-800-FLOWERS ---> 1-800-3569377"""


dic_teclado = {0:" ",1: "*",2:"abc",3: "def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

def roseta_telefonica (caracter,dic_teclado):
    valores=dic_teclado.values()
    simbolo=""
    for valor in valores:
        if caracter in valor:
            simbolo = str(dic_teclado[valor])
    return simbolo


def roseta_telefonica_2 (caracter,dic_teclado):
    clave=""
    for (num,letra) in dic_teclado.items():
        if caracter in letra:
            clave = num
    return clave



#programa principal
tel_teclado = input(" Ingrese el número al que desea llamar ").lower()

cadena_en_lista = tel_teclado.split("-")

salida=""


for caracter in cadena_en_lista [2]:
    salida= salida + str(roseta_telefonica_2(caracter,dic_teclado))
salida = caracter[0] + "-" + caracter[1] + "-" + salida  
print(salida)


