"""Una palabra es "alfabètica" si todas sus letras estàn ordenadas alfabèticamente. 
Por ejemplo,"amor", "chino" e "himno" son palabras alfabèticas. 
Diseña un programa que sea una palabra y nos diga si es alfabètica o no"""


def palabra_alfabetica(msj):
    palabra_usuario =mensaje
    palabra_ordenada=sorted(palabra_usuario)
    palabra_ordenadastrg="".join(palabra_ordenada)
    
    if palabra_usuario==palabra_ordenadastrg:
        print("La  palabra", msj, "es alfabètica")
    else:
        print("La palabra" , msj,"no es alfabètica")
            
mensaje=input("Ingrese su palabra  y le indicaremos si es alfabètica o no:  ")

palabra_alfabetica(mensaje)