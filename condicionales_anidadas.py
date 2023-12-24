"""
Este programa realiza las siguientes tareas:

Obtiene la fecha actual utilizando la librería datetime y muestra el día actual.
Solicita al usuario ingresar tres valores enteros A, B y C.
Compara si los tres valores son iguales (equilátero), si dos de ellos son iguales 
(isósceles) o si todos son diferentes (escaleno), y muestra un mensaje con el tipo 
de triángulo según la comparación realizada.
Solicita al usuario ingresar un animal.
Convierte el nombre del animal a mayúsculas.
Compara el animal ingresado con tres opciones: "PERRO", "GATO" y "OSO". Según la 
coincidencia, imprime un mensaje que describe algunas características del animal 
ingresado.
Finaliza el programa mostrando "Fin".
El programa interactúa con el usuario para recibir tres valores enteros 
y un nombre de animal, luego realiza comparaciones basadas en los valores ingresados
y muestra mensajes dependiendo de las coincidencias encontradas en las comparaciones
"""

from datetime import date
hoy = date.today()                #Fecha actual
print("Hoy es el dia: ", hoy)
print()
print("EJERCICIO DE LAS CLASES DE TRIANGULOS")
a=int(input("Digite el valor A: "))
b=int(input("Digite el valor B: "))
c=int(input("Digite el valor C: "))

if a==b and a==c and b==c:
    print("EL TRIANGULO ES EQUILATERO")
else:
    if a==b or b==c or a==c:
        print("EL TRIANGULO ES ISOCELE")
    else:
        print("El triangulo es Escaleno")
print()
animal=input("Digite un animal: ")
animal=animal.upper()
if animal=="PERRO":
    print("Este animal es el mejor amigo del hombre:", animal)
elif animal=="GATO":
    print("Este animal persigue ratones: ", animal)
elif animal=="OSO":
    print("Este animal vive en el polo norte: ", animal)
print()
print("Fin")
