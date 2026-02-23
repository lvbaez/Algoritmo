#Programa que solicita al usuario una cantidad de horas, otra cantidad de minutos, y otra cantidad 
#de segundos (suponer que siempre se cargarán números enteros y positivos). El programa debe 
#mostrar la cantidad total de segundos para esos datos de entrada.

horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
total_segundos = (horas * 3600) + (minutos * 60) + segundos

print("La cantidad total de segundos es:", total_segundos)