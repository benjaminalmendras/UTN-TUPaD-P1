from statistics import mode, median, mean
import random
print()
print("Actividad 1")
print()
edad = int(input("Ingrese su edad: "))
if edad > 0 and edad > 18:
    print("Es mayor de edad ")
print()
print()
print("Actividad 2")
print()
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
print()
print()
print("Actividad 3")
print()
numero =int(input("Ingrese un numero Par: "))
if numero % 2 != 0:
    print("Por favor ingrese un numero par!")
else:
    print ("Ha ingresado un número par")
print()
print()
print("Actividad 4")
print()
edad1 = int(input("Ingrese su edad: "))
if edad1 >= 0 and edad1 < 12:
    print("Categoría: Niño/a")
elif edad1 >= 12 and edad1 <18:
    print("Categoría: Adolescente")
elif edad1 >= 18 and edad1 < 30:
    print("Categoría: Adulto/a Joven")
elif edad1 >= 30:
    print("Categoría: Adulto/a")
print()
print()
print("Actividad 5")
print()
passwd = input("Ingrese una contraseña(entre 8 y 14 caracteres)")
longitud_passwd = len(passwd)
if longitud_passwd >= 8 and longitud_passwd <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
print()
print()
print("Actividad 6")
print()
numeros_aleatorios = [random.randint(1, 100)for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana and mediana > moda:
    print("Tiene Sesgo Positivo")
elif media < mediana and mediana < moda:
    print("Tiene Sesgo Negativo")
elif media == moda and mediana == moda:
    print("Sin Sesgo")
print()
print("Actividad 7")
print()
vocales = "aeiouAEIOU"
frase = input("Ingrese una frase: ")
if frase[-1] in vocales:
    cad = frase
    cad += "!"
    print(cad)
else:
    print(frase)
print()
print()
print("Actividad 8")
print()
nombre2 = input("Ingrese su nombre: ")
menu = "Menú de Opciones\n"
menu += "1- Nombre en Mayúsculas \n"
menu += "2- Nombre en Minúsculas \n"
menu += "3- Primera letra Mayúscula y el resto en Minúscula \n"
opcion = int(input(menu))
if opcion == 1:
    print(nombre2.upper)
elif opcion == 2:
    print(nombre2.lower)
elif opcion == 3:
    print(nombre2.title)
else:
    print("Ingresó una opción incorrecta!")
print()
print()
print("Actividad 9")
print()
magnitud = float(input("Ingrese la magnitud de un terremoto: "))
print("Categoría Segun Escala de Ritcher")
if magnitud < 3:
    print("Muy Leve / Imperceptible")
elif magnitud >= 3 and magnitud < 4:
    print("Leve / Ligeramente Imperceptible") 
elif magnitud >=4 and magnitud < 5:
    print("Moderado")   
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte")
elif magnitud > 7:
    print("Extremo")
print()
print()
print("Actividad 10")
print()
hemisferio = input("En que Hemisferio estas? Contestar Usando N o S")
hemisferio = hemisferio.lower
mes = int(input("Ingrese el mes en el que está: "))
año = int(input("Ingrese el Año en el que está: "))
dia = int(input("Ingrese el Día en el que está: "))
if len(hemisferio) > 1 or mes > 12 or dia > 31 or año > 2025:
    print("Ingresó mal los datos!")
elif (dia >= 21 and mes == 12 ) or mes == 1 or mes == 2 or (dia <= 20 and mes == 3) and hemisferio == "n":
    print("Su estación es INVIERNO")
elif (dia >= 21 and mes == 12 ) or mes == 1 or mes == 2 or (dia <= 20 and mes == 3) and hemisferio == "s":
    print("Su estación es VERANO")
elif (dia >= 21 and mes == 3 ) or mes == 4 or mes == 5 or (dia <= 20 and mes == 6) and hemisferio == "n":
    print ("Su estación es PRIMAVERA")
elif (dia >= 21 and mes == 3 ) or mes == 4 or mes == 5 or (dia <= 20 and mes == 6) and hemisferio == "s":
    print ("Su estación es OTOÑO")
elif (dia >= 21 and mes == 6 ) or mes == 7 or mes == 8 or (dia <= 20 and mes == 9) and hemisferio == "n":
    print ("Su estación es VERANO")
elif (dia >= 21 and mes == 6 ) or mes == 7 or mes == 8 or (dia <= 20 and mes == 9) and hemisferio == "s":
    print ("Su estación es INVIERNO")
elif (dia >= 21 and mes == 9 ) or mes == 10 or mes == 11 or (dia <= 20 and mes == 12) and hemisferio == "n":
    print ("Su estación es OTOÑO")
elif (dia >= 21 and mes == 9 ) or mes == 10 or mes == 11 or (dia <= 20 and mes == 12) and hemisferio == "s":
    print ("Su estación es PRIMAVERA")
print()

