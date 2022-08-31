# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''


print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
print('ingrese un numero')
num_1 = int(input())
print('ingrese segundo numero')
nume_2 = int(input())
print('ingrese tercer numero')
num_3 = int(input())

if (num_1 % 2) == 0:
    print('numero 1 es par')
else:
    print('numero 1 es impar')

if (nume_2 % 2) == 0:
    print('numero 2 es par')
else:
    print('numero 2 es impar')

if (num_3 % 2) == 0:
    print('numero 3 es par')
else:
    print('numero 3 es impar')
