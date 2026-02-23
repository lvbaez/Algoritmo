#Ingresar por teclado, de manera separada, los valores de día, mes y año; y que muestre en pantalla 
# la fecha en el formato d/m/a.
#Por ejemplo: si d=17, m=2 y a=2026 ----> "La fecha ingresada es: 17/2/2026"
#Observaciones:
#    Podemos suponer que el usuario siempre ingresará números válidos.
#    Al emplear la función print(), aparecen espacios entre los valores y las cadenas que se muestran. 
#    Para que ello no ocurra, emplear el parámetro sep='' - son dos comillas simples). 
#    Por ejemplo: print(a,"+",b, sep='') no dejará espacios entre el valor de a, el símbolo + y el valor de b.

d=int(input("Día:"))
m=int(input("Mes:"))
a=int(input("Año"))
print("La fecha ingresada es: ",d,"/",m,"/",a,sep='')