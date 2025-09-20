# Trabajo Practico N 1
# Estructuras Secuenciales

print("Resolucion Ejercicio 1")
print()
print("Hola mundo!")
print()
print("Resolucion Ejercicio 2")
print()
nombre = input("Ingrese su nombre: ")
print("Hola", nombre, "!")
print("Resolucion Ejercicio 3")
print()
n = input("Ingrese su nombre: ")
a = input("Ingrese su apellido: ")
e = input("Ingrese su edad: ")
l = input("Ingrese su lugar de Residencia: ")
print("Soy ", n ,"", a, ",tengo ", e, " años y vivo en ", l)
print()
print("Resolucion Ejercicio 4")
print()
radio = float(input("Ingrese el radio de un circulo: "))
area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio
print()
print("Resolucion Ejercicio 5")
print()
segundos = int(input("Ingrese la cantidad de segundos a convertir en horas: "))
horas = round((segundos / 3600), 2)
print(segundos, " segundos equivalen a: ", horas, " horas")
print()
print("Resolucion Ejercicio 6")
print()
num = input("Ingrese el numero para imprimir la tabla de multiplicar: ")
for i in range(num):
    l = i + 1
    re = num * i
    print(num, " x ", l, "= ", re)
print()
print("Resolucion Ejercicio 7")
bandera = False
bandera1 = False
while bandera == False:
    num1 = int(input("Ingrese un numero entero mayor al cero"))
    if num1 > 0:
        bandera = True
while bandera1 == False:
    num2 = int(input("Ingrese otro numero entero mayor al cero"))
    if num2 > 0:
        bandera = True
suma = num1 + num2
divi = num1 / num2
multi = num1 * num2
resta = num1 - num2

print("La Suma de estos dos numeros es: ", suma)
print("La Division de estos dos numeros es: ", divi)
print("La Multiplicacion de estos dos numeros es: ", multi)
print("La Resta de estos dos numeros es: ", resta)
print()
print("Resolucion Ejercicio 8")
print()
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
imc = peso / (altura ** 2)
print("IMC = ", imc)
print()
print("Resolucion Ejercicio 9")
print()
celsius = float(input("Ingrese la temperatura en celsius para convertir en Fahrenheit: "))
fahrenheit = (9/5) * celsius + 32
print(celsius, " grados celsius equivalen a ", fahrenheit, "grados fahrenheit")
print()
print("Resolucion Ejercicio 10")
print()
nume1 = float(input("Ingrese el numero 1: "))
nume2 = float(input("Ingrese el numero 2: "))
nume3 = float(input("Ingrese el numero 3: "))
prom = ( nume1 + num2 + nume3) / 3
print("El promedio es ", prom)