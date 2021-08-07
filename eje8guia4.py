"""Ejercicio 8:
La empresa RawInput S.A. desea hacer una clasificación de sus clientes según su ubicación
geográfica. Para esto, analizará su base de datos de correos electrónicos con el fin obtener 
información sobre el lugar de procedencia de cada cliente.
En una dirección de correo electrónico, el dominio es la parte que va después de la arroba, 
y el TLD es lo que va después del último punto. Por ejemplo, en la dirección 
fulano.de.tal@alumnos.usm.cl, el dominio es alumnos.usm.cl y el TLD es cl.
Algunos TLD no están asociados a un país, sino que representan otro tipo de entidades. 
Estos TLD genéricos son los siguentes:
genericos = {'com', 'gov', 'edu', 'org', 'net', 'mil'}
1. Escriba la función obtenerDominios(correos) que reciba como parámetro una lista 
de correos electrónicos, y retorne la lista de todos los dominios, sin repetir, y en 
orden alfabético.
2. Escriba la función contarTld(correos) que reciba como parámetro la lista de correos 
electrónicos, y retorne un diccionario que asocie a cada TLD la cantidad de veces 
que aparece en la lista. No debe incluir los TLD genéricos.
c = ['fulano@usm.cl', 'erika@lala.de', 'li@zi.cn', 'a@a.net', 'gudrun@lala.de', 
'otto.von.d@lorem.ipsum.de', 'org@cn.de.cl', 'yayita@abc.cl', 'jozin@baz.cz', 'jp@foo.cl', 
'dawei@hao.cn', 'pepe@gmail.com', 'ana@usm.cl', 'polo@hotmail.com', 'fer@x.com', 
'ada@alumnos.usm.cl', 'dj@foo.cl', 'jan@baz.cz', 'd@abc.cl']
obtenerDominios(c) se obtiene:
['abc.cl', 'alumnos.usm.cl', 'baz.cz', 'cn.de.cl', 'foo.cl',
'hao.cn', 'lala.de', 'lorem.ipsum.de', 'usm.cl', 'zi.cn']
contarTld(c) se obtiene: {'cz': 2, 'de': 3, 'cn': 2, 'cl': 8"""

lista_correos=['fulano@usm.cl', 'erika@lala.de', 'li@zi.cn', 'a@a.net', 'gudrun@lala.de', 
'otto.von.d@lorem.ipsum.de', 'org@cn.de.cl', 'yayita@abc.cl', 'jozin@baz.cz', 'jp@foo.cl', 
'dawei@hao.cn', 'pepe@gmail.com', 'ana@usm.cl', 'polo@hotmail.com', 'fer@x.com', 
'ada@alumnos.usm.cl', 'dj@foo.cl', 'jan@baz.cz', 'd@abc.cl']


def obtenerDominios(correos):
    lista_dom=[]
    for n in lista_correos:
        dominio= n.split("@")[1]
        lista_dom.append(dominio)
    return sorted(lista_dom)
        
dom_genericos = {'com', 'gov', 'edu', 'org', 'net', 'mil'}

def contarTld(correos,genericos):
    dic_tld={}
    lista_tld=[]
    for n in correos:
        tld=n.split(".")[-1]
        if tld not in genericos:
            lista_tld.append(tld)
    for elem in lista_tld:
        if elem in dic_tld.keys():
            dic_tld[elem]=dic_tld[elem]+1
        else:
            dic_tld[elem]=1
    return dic_tld
    

print(obtenerDominios(lista_correos))

print(contarTld(lista_correos,dom_genericos))

