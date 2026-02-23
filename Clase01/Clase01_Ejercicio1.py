# Calcular el área de un triángulo conocidos sus tres lados

a = float(input("Ingrese el lado a: "))
b = float(input("Ingrese el lado b: "))
c = float(input("Ingrese el lado c: "))

s = (a + b + c) / 2 #fórmula de semiperímetro

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5 #fórmula de área

print("El área del triángulo es:", area)
