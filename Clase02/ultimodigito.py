#Programa que sume dos numeros enteros y muestre el ultimo digito de la suma
a= int(input("Ingresar el primer número: "))
b= int(input("Ingresar el segundo número: "))

suma = a + b
ud = suma % 10

print("El primer digito de",a,"+",b,"es:", ud)