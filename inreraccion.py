"""
Este programa realiza las siguientes acciones:

Obtiene la fecha actual utilizando la librería datetime y muestra el día actual.
Solicita al usuario ingresar dos números enteros.
Realiza operaciones matemáticas básicas con los números ingresados: suma, resta, multiplicación y división.
Muestra los resultados de estas operaciones.
Finaliza el programa mostrando "Fin".
El programa interactúa con el usuario para obtener dos números, realiza operaciones aritméticas con 
estos números y muestra los resultados correspondientes.
"""

from datetime import date
hoy = date.today()                #Fecha actual
print("Hoy es el dia: ", hoy)
n1 = int(input("Digite el primer numero: "))
n2 = int(input("Digite el segundo numero: "))
suma=n1+n2
resta=n1-n2
producto=n1*n2
division=n1/n2
print("La suma es = ",suma )
print("La resta es = ",resta )
print("La multiplicacion es = ",producto )
print("La division es = ",division)
print("Fin")
