import random
print("Trabajo Práctico 4")
print()
# Ejercicio 1
print("Ejercicio 1")
for i in range(101):
    print(i)
print()
# Ejercicio 2
print("Ejercicio 2 ")
numero2 = int(input("Ingrese un número entero: "))
cont_digitos = 0
if numero2 >= 0:
    numero2 = numero2
else:
    numero2 = numero2 * -1

if numero2 == 0:
    cont_digitos = 1 
else:
     while numero2 > 0:
         numero2 // 10
         cont_digitos += 1
print("La cantidad de dígitos es: ", cont_digitos)
print()
# Ejercicio 3
print("Ejercicio 3 ")
num3_1 = int(input("Ingrese el primer número: "))
num3_2 = int(input("Ingrese el segundo número: "))
iniciador = 0
final = 0
suma_3 = 0
if num3_1 == num3_2:
    suma_3 = 0
elif num3_1 > num3_2:
    iniciador = num3_2 + 1
    final = num3_1 - 1
elif num3_2 > num3_1:
    iniciador = num3_1 + 1
    final = num3_2 - 1
for i in range(iniciador, final + 1):
    suma_3 += i
print("La suma de los números comprendidos es:", suma_3)
print()
# Ejercicio 4
print("Ejercicio 4")
cont_4 = 0
num_4 = None
while num_4 != 0:
    num_4 = int(input("Ingrese un numero entero: "))
    cont_4 += num_4
print("El total acumulado es: ", cont_4)
print()
# Ejercicio 5
print("Ejercicio 5")
num_a_adivinar = random.randint(0,9)
intentos_5 = 0
num_5 = None
while num_5 != num_a_adivinar:
    num_5 = int(input("Ingrese un número entero para adivinar: "))
    intentos_5 += 1
print("La cantidad de intentos fue: ", intentos_5)
print()
# Ejercicio 6
valor = 100
for i in range(100, -1, -2):
    print(i)
print()
# Ejercicio 7
print("Ejercicio 7")
suma_7 = 0
num_7 = int(input("Ingrese un número postivo: "))
while num_7 <= 0:
    num_7 = int(input("Error! Ingrese un número positivo: "))
for i in range(0, num_7 + 1):
    suma_7 += i
print("La suma total es: ", suma_7)
print()
# Ejercicio 8
print("Ejercicio 8")
print("Ingrese 100 números enteros:")
cont_par_7 = 0
cont_impar_7 = 0
cont_positivo_7 = 0
cont_negativo_7 = 0
num_8 = None
for i in range(100):
    num_8 = int(input("Ingrese un número entero: "))
    if num_8 % 2 == 0:
        cont_par_7 += 1
    else:
        cont_impar_7 += 1
        
    if num_8 > 0:
        cont_positivo_7 += 1
    elif num_8 < 0:
        cont_negativo_7 += 1
print("Resultados:")
print("Cantidad de pares:", cont_par_7)
print("Cantidad de impares:", cont_impar_7)
print("Cantidad de positivos:", cont_positivo_7)
print("Cantidad de negativos:", cont_negativo_7)
print()
# Ejercicio 9
print("Ejercicio 9")
cont_9 = 0
for i in range(100):
    num_9 = int(input("Ingrese un número entero: "))
    cont_9 += num_9
promedio_9 = cont_9 / 100
print("El promedio entre estos 100 números es: ", round(promedio_9, 2))
print()
# Ejercicio 10
print("Ejercicio 10")
band_negativo = None
num_invertido = ""
num_a_invertir = int(input("Ingrese el numero que desea invertir: "))
if num_a_invertir < 0:
    num_a_invertir = num_a_invertir * -1
    band_negativo = True
else:
    band_negativo = False
num_str = str(num_a_invertir)
cant_digitos = len((num_str))
for i in range(cant_digitos - 1, -1, -1):
    num_invertido += num_str[i]
num_invertido = int(num_invertido)
if band_negativo == True:
    num_invertido = -num_invertido
print("El número invertido es: ", num_invertido)