# Calcular el área de un triángulo conocidos sus tres lados
a = 5
b = 5
c = 7

t = (a + b + c) / 2 #fórmula de semiperímetro
s = (t * (t - a) * (t - b) * (t - c)) ** 0.5 #fórmula de área

print("El área del triángulo es:", s)
