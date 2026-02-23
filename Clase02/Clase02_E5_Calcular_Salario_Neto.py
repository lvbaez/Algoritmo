#Ingresar el salario bruto (en guaraníes) de un trabajador, y que calcule los impuestos que debe 
# pagar; considerando que su seguro médico a IPS es del 5.5% del salario bruto, y que su pago por 
# jubilación al MEF es del 16% de su salario bruto.

sb = float(input("Ingresar el salario bruto en Gs: "))
ips = sb * 5.5 / 100
jubilacion = sb * 0.16
sn = sb - ips - jubilacion

print("-------------Cálculos-------------")
print("El descuento de IPS es:", ips, "Gs")
print("El descuento de Hacienda es:", jubilacion, "Gs")
print("El salario neto es:", sn, "Gs")
