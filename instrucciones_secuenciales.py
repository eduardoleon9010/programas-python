"""
Este programa realiza varias acciones:

Obtiene la fecha actual usando la librería datetime y muestra el día actual.
Solicita al usuario ingresar dos valores enteros A y B.
Compara A y B y muestra un mensaje dependiendo de si A es mayor o igual a B.
Define dos variables (curso_1 y curso_2) con nombres de cursos.
Compara si curso_1 es igual a "Requerimientos" y curso_2 es igual a "Algoritmos". 
Si ambas condiciones se cumplen, muestra un mensaje indicando que el usuario estudia 
programación de software; de lo contrario, muestra un mensaje diferente.
Imprime un mensaje para señalar el final del análisis del programa de formación SENA.
Solicita al usuario ingresar una oración.
Imprime la oración ingresada en mayúsculas.
Calcula y muestra la longitud de la oración ingresada.
Evalúa si la longitud de la oración es mayor a 10 caracteres y muestra un mensaje 
indicando si es mayor o menor a 10 caracteres.
Finaliza el programa mostrando "Fin".
El programa interactúa con el usuario para recibir datos, realiza 
comparaciones entre valores y cadenas, muestra mensajes y realiza algunas 
operaciones básicas con cadenas y números.
"""

from datetime import date
hoy = date.today()                #Fecha actual
print("Hoy es el dia: ", hoy)

a=int(input("Digite el valor A: "))
b=int(input("Digite el valor B: "))
if a>=b:
    print("A es mayor o igual a B")
else:
    print("A es menor que B")
print()
curso_1="Requerimientos"
curso_2="Algoritmos"
print("El curso_1 es: ", curso_1)
print("El curso_2 es: ", curso_2)
if curso_1 == "Requerimientos" and curso_2 == "Algoritmos":
    print("Usted estudia programacion de software")
else:
    print("Usted estudia otro programa deferente a programacion de software")
print()
print("*** Final del analisis del programa de formacion SENA")
print()
frase=input("Digite una oracion: ")
print("La frase en mayuscula es: ", frase.upper())
longitud=len(frase)
print("La longitud de la frase es: ", len(frase), "caracteres")
if longitud>10:
    print("La frase contiene mas de 10 caracteres")
else:
    print("La frase contiene menos de 11 caracteres")
print()
print("Fin")
