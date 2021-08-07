"""La ley de Chargaff dice que en el ADN de un organismo la cantidad de Adenina es la 
misma que la de Tiamina, y la de Citosina es la misma que la de Guanina. Dada una 
secuencia de nucleótidos del estilo de ATTACCAGTACA... podemos comprobar si cumple
dicha ley de la siguiente forma:
a=(Na-Nt)/(Na+Nt)   c=Nc-Ng/Nc+Ng
Contamos la cantidad de A, T, C y G presentes en la cadena y calculamos los coeficientes
donde NX indica la cantidad de nucleótidos del tipo X presentes en la secuencia.
Partiremos de una cadena que contiene una cantidad indeterminada de caracteres, que 
solo pueden ser A, T, G ó C. Calcula a partir de dicha cadena los coeficientes a y c"""
#ingresar la cadena
#validar cadena

def cadena_Valida(sec):
    cadena_valida = "aAcCgGtT"
    valida=True
    for c in sec:
        if c not in cadena_valida:
            valida=False
            print(valida)
    return valida  

def coeficiente_a(a,t):
    a_=(a-t)/(a+t)  
    return(a_)

def coeficiente_c(c,g):
    c_=(c-g)/(c+g)  
    return(c_)
    
cadena_atcg = input("Ingrese su secuencia de nucleòtidos con los caracteres apropiados ").upper()

validez= cadena_Valida(cadena_atcg)
while (not validez):
    print("Estas ingresando un caracter no válido, sòlo puedes ingresar A,C,G,T ")
    cadena_atcg = input("Ingrese su secuencia de nucleòtidos con los caracteres apropiados ").upper()

lista_nucleotidos= list(cadena_atcg)


adenina = lista_nucleotidos.count("A")
tiamina= lista_nucleotidos.count("T")
citosina = lista_nucleotidos.count("C")
guadina= lista_nucleotidos.count("G")

coe_a= coeficiente_a(adenina,tiamina)

coe_c = coeficiente_c(citosina,guadina)

print(adenina,tiamina,citosina,guadina)
print("el coeficiente a de la secuencia ", cadena_atcg ,"es",coe_a, "y el coeficiente c es  ", coe_c  )