#Programa que permite ingresar dos números por teclado, realizar el intercambio de números
# y mostrar en pantalla (imprimir) el resultado del intercambio. 
A=int(input("Número A: "))
B=int(input("Número B: "))

A = A + B #5 + 10 = 15
B = A - B #15 - 10 = 5
A = A - B #15 - 5 = 10

print("A después del intercambio:", A)
print("B después del intercambio:", B)
