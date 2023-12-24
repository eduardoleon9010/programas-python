"""
Este programa realiza varias acciones:

Obtiene la fecha actual usando la librería datetime y muestra el día actual.
Solicita al usuario ingresar dos números enteros.
Ejecuta tres ciclos for utilizando la función range() con los números ingresados por el usuario:
El primer ciclo itera desde 0 hasta el primer número ingresado.
El segundo ciclo itera desde el primer número ingresado hasta el segundo número ingresado.
El tercer ciclo itera desde el primer número ingresado hasta el segundo número ingresado, pero con
incrementos de 1 (es igual al segundo ciclo).
Solicita al usuario ingresar el nombre de una empresa, convierte ese nombre a minúsculas y luego 
itera sobre cada carácter de ese nombre, imprimiendo cada carácter en una línea independiente.
Finaliza mostrando "Fin".
Este programa hace uso de ciclos for para iterar sobre rangos de números, imprimirlos 
y recorrer cada carácter de una cadena ingresada por el usuario.
"""

from datetime import date
hoy = date.today()                #Fecha actual
print("Hoy es el dia: ", hoy)
print()
print("TALLER 5 CICLOS ITERATIVOS CON LA SENTENCIA FOR")
print()
num_1=int(input("Digite el primer numero; "))
num_2=int(input("Digite el segundo numero (mayor); "))
print("Ciclos para el primer numero")
for i in range(num_1):
    print(i)
print('Fin del ciclo')

print()
print("Ciclo desde el primero hasta el segundo numero")
for i in range(num_1,num_2):
    print(i)
print('Fin de ciclo')

print()
print("Ciclo desde el primero hasta el segundo numero con incrementos de 2")
for i in range(num_1,num_2):
    print(i)
print('Fin de ciclo')

print()
empresa=input("Digite nimnre de una empresa: ")
empresa=empresa.lower()
for character in empresa:
    print(character)
print("Fin del ciclo")

print()
print("Fin")
