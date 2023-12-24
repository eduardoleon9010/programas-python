"""
Este programa realiza las siguientes acciones:

Obtiene la fecha actual utilizando la librería datetime y muestra el día actual.
Solicita al usuario ingresar un número entero.
Realiza un ciclo controlado por contador (while) desde 1 hasta el número ingresado 
por el usuario, mostrando en cada iteración el valor del contador.
Solicita al usuario adivinar un número entre 1 y 10, y controla un ciclo hasta que 
el usuario adivine el número secreto predefinido (5). Muestra en cuántos intentos acertó.
Solicita al usuario ingresar el nombre de una amistad, convierte el nombre a 
mayúsculas y muestra cada caracter del nombre hasta que encuentra la letra "A", 
momento en el que se detiene el ciclo.
Finaliza el programa mostrando "Fin".
Este programa interactúa con el usuario para realizar ciclos controlados 
por un contador, por eventos y también muestra cómo utilizar la sentencia break para 
interrumpir un ciclo.
"""

from datetime import date
hoy = date.today()                #Fecha actual
print("Hoy es el dia: ", hoy)
print()
print("TALLER 6 CICLOS ITERATIVOS CON LA SENTENCIA WHILE")
print()
num_1=int(input("Digite el primer numero: "))

print("***Ciclo controlados por contador")
i = 1
while i <= num_1:
    print(i)
    i += 1
print('Fin del ciclo')

print()
print("***Ciclo controlado por eventos")
i = 1
numero1=5
numero2= int(input('Digite un numero de 1 a 10: '))
while numero2 != numero1:
    i += 1
    numero2 = int(input("Digite un numeros de 1 a 10: "))
print("Acertaste en el intento No.", 1)
print('Fin de ciclo')

print()
print("***Ciclo abortado con la sentencia break")
amistad=input("Digite nombre de una amistad: ")
amistas=amistad.upper()
for character in amistad:
    print(character)
    if character=="A":
        break
print("Fin del ciclo")

print()
print("Fin")
