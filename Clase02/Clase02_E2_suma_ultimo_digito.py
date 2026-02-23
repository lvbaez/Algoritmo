#Ingresar por teclado dos números (suponer que el usuario siempre cargará números enteros y positivos) 
#y muestre en pantalla el primer dígito (el que está más a la derecha) de la suma de ambos
a= int(input("Ingresar el primer número: "))
b= int(input("Ingresar el segundo número: "))

suma = a + b
ud = suma % 10

print("El primer dígito de la derecha de",a,"+",b,"es:", ud)

