"""Realizar un programa que calcule eldesglose en billetes y modenas de una cantidad exacta de euros. 
Hay billetes de 500,200,100,50,20,10 y 5 euros y monedas de 2 y 1 euros. 
Por ejemplo, si deseamos conocer el desglose de 434, el programa mostrará por pantalla el siguiente resultado: 
2 billetes de 200 euros, 1 billete de 20 euros,1 billete de 10 euros. 2 monedas de 2 euros"""

monto = int(input("Ingresa el monto a desglosar "))

b500 = monto // 500
b500resto = monto % 500
b200 = b500resto// 200
b200resto = b500resto% 200
b100 = b200resto // 100
b100resto = b200resto % 100
b50 = b100resto // 50
b50resto = b100resto % 50
b20 = b50resto // 20
b20resto = b50resto% 20
b10 = b20resto// 10
b10resto = b20resto% 10
b5 = b10resto // 5
b5resto = b10resto% 5
m2 = b5resto // 2
m2resto = b5resto % 2
m1 = m2resto // 1
m1resto = m2resto % 1

if b500 >= 1:
    print(str(b500) + " billete" + ('s' if (b500) > 1 else '') + " de 500")
if b200 >= 1:
    print(str(b200) + " billete" + ('s' if (b200) > 1 else '') + " de 200")
if b100 >= 1:
    print(str(b100) + " billete" + ('s' if (b100) > 1 else '') + " de 100")
if b50 >= 1:
    print(str(b50) + " billete" + ('s' if (b50) > 1 else '') + " de 50")
if b20 >= 1:
    print(str(b20) + " billete" + ('s' if (b20) > 1 else '') + " de 20")
if b10 >= 1:
    print(str(b10) + " billete" + ('s' if (b10) > 1 else '') + " de 10")
if b5 >= 1:
    print(str(b5) + " billete" + ('s' if (b5) > 1 else '') + " de 5")
if m2 >= 1:
    print(str(m2) + " moneda" + ('s' if (m2) > 1 else '') + " de 2")
if m1 >= 1:
    print(str(m1) + " moneda" + ('s' if (m1) > 1 else '') + " de 1")

