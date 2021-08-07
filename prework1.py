"""tipo"""
"""def tipo_de_dato(mi_dato, tipo):
    if tipo is str or tipo == float:
        return True
    elif tipo == int or tipo == bool:
        return False
        
print(tipo_de_dato(9,int))"""
"""def tipo_de_dato(mi_dato):
    if isinstance(mi_dato,float)or isinstance(mi_dato,str):
        return True
    elif isinstance(mi_dato,int)or isinstance(mi_dato,bool):
        return False


print(tipo_de_dato("9.1"))"""

"""def funcion(numero):
    numero += 3
    mi_lista = [numero]

    mi_lista.append(numero**2)

    return 'mi_lista'

llamado = funcion(20)    
print(llamado)


def lista_par_impar(lista):
    lista_pares=[]
    lista_impares=[]
    for n in lista:
        if n%2==0:
            lista_pares.append(n)
            print(lista_pares)
        else:
            lista_impares.append(n)
            print(lista_impares)
    return lista_pares,lista_impares

listamezclada=[1,5,6,8,4,14,56,3]
print(lista_par_impar(listamezclada))

list = [36, 35, 36, 39.5, 40, 44, 53, 25, 80, 42]
print(sorted(list))
def contador(lista):
    cont=0
    for n in lista:
        cont+=1
    return cont

def sumatoria(lista):
    suma_lista=0
    for n in lista:
        suma_lista+=n
    return suma_lista
medi=[2536, 2137, 2448, 2121 ,2622]
def media (lista):
    med =sumatoria(lista)/contador(lista)
    return med

print(media(medi))
print(contador(list),sumatoria(list),media(list))

def cuadrado_de_suma(num1, num2):
    resultado_de_suma = sumando(num1, num2)
    return resultado_de_suma **2

def perimetro_circulo(radio):
    pi=3.1416
    perim =2*pi*radio
    return perim

animales = ['ballena', 'elefante', 'gallina']

mi_diccionario = {x:len(x) for x in animales}
print(mi_diccionario)

def difference(num):
    diff=0
    if num <17:
        diff=num-17
    else:
        diff=(num-17)*2
    return abs(diff)
def near_thousand(num):
    return bool(num >=100 and num<=1000)


print(near_thousand(1001))

def suma_tres(a,b,c):
    if a ==b and a==c:
        result=(a+b+c)*3
    else:
        result=a+b+c 
    return result
list = [4, 35, 36,4, 44, 53, 25, 4, 42]
def cuenta_cuatro(lista):
    return lista.count(4)

print(cuenta_cuatro(list))
Escribí una función que reciba un número y un listado de números (en ese orden) 
y devuelva True si el número pertenece a la lista.
 Si el número no se encuentra presente,
  la función debe incluirlo al final de la lista y devolverla.
def check(num,list):
    if num in list:
        return True
    else:
        list.append(num)
        return list
def concat_string(list):
    string="".join(list)
    return string

def stop_248(list):
    pares_list=[]
    for n in list :
        if n %2 ==0 and n !=2 and n !=4 and n !=8 :
            pares_list.append(n)
    return (pares_list)

lista=[1, 2, 3, 4, 2]    
def repetidos(lista):
    for n in lista:
        print(lista)
        return(lista.count(n))
        
print(repetidos(lista))

def repetidos(lista):
    if len(lista) == len(set(lista)):
        return False
    else:
        return True

def repetidos(lista):
    return(len(lista) != len(set(lista)))

def primos(numero):
    if numero == 0 or numero == 1 or numero == 4:
        return False
    for x in range(2, int(numero/2)):
        if numero % x == 0:
            return False
    return True

def unicos(lista):
    listanueva= []
    for x in lista:
        if x not in listanueva:
            listanueva.append(x)
    return listanueva

def lista_de_unicos(lista):
    listanueva= []
    for x in lista:
        if x not in listanueva:
            listanueva.append(x)
    return sorted(listanueva)

list=[[1, 3, 2, 4, 5]]
print(unicos(list))



pilas=[20,0,1,9,0,3,5,0,0]

def borrar_ceros(lista):
    con=lista.count(0)
    for x in range(con):
        lista.remove(0)
    return lista

print(borrar_ceros(pilas))

def borrar_ceros_list(lista):
    lista_sin_cero=[]
    for x in lista:
        if x !=0:
            lista_sin_cero.append(x)
    return lista_sin_cero

print(borrar_ceros_list(pilas))
def cuadrados():
    lista=[]
    for i in range (1,31):
        lista_elevada = i**2
        lista.append(lista_elevada)
    return lista
Escribí una función que, dado un número,
 devuelva una lista con los los números impares comprendidos entre 0
  y ese número (sin incluirlo). 
  Como condición, la función se debe construir con una lista por comprensión."""

pilas=[20,21,47] 

def impares(numero):
    return [x for x in range(0,numero)if x %2 != 0]
    
print(impares(pilas))

