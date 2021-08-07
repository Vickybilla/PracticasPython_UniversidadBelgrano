#validar una fecha ingresada como dia, mes y aa
from fecha import nombres
dia = int(input("ingrese dia: "))
mes = int(input("ingrese mes: "))
aa = int(input("ingrese año: "))
if 1 <= mes <= 12:
    if mes == 2:
        bisiesto = aa % 4 == 0
        if bisiesto == True:
            if 1 <= dia <= 29: #1<= dia and dia <= 29
                print ("fecha correcta: ", dia,"/", nombres[mes],"/", aa )
            else:
                print ("fecha no valida")
        else:
            if 1 <= dia <= 28: #1<= dia and dia <= 28
                print ("fecha correcta")
            else:
                print ("fecha no valida")
    else:
        #abril, junio, septiembre, noviembre
        if mes in [4,6,9,11]:
            if 1 <= dia <= 30:
                print("fecha correcta")
            else:
                print ("fecha no valida")
        else:
            if 1 <= dia <= 31:
                print("fecha correcta")
            else:
                print ("fecha no valida")
else:
    print("fecha no valida")
    
'''
comenta varias lineas
'''
