import random

print("Trabajo Práctico 5")
print()

# Ejercicio 1
print("Ejercicio 1")

lista_1 = []
suma_notas_1 = 0
mas_alta = None
mas_baja = None

for i in range(10):
    nota = random.randint(1, 10) 
    suma_notas_1 += nota
    lista_1.append(nota)

    if i == 0:
        mas_alta = nota
        mas_baja = nota
    else:
        if nota > mas_alta:
            mas_alta = nota
        if nota < mas_baja:
            mas_baja = nota

prom = suma_notas_1 / 10

for i in range(len(lista_1)):
    print("La nota del Estudiante", i + 1, "es: ", lista_1[i])
    
print("El promedio de estas notas es: ", round(prom, 2))
print("La nota más baja es: ", mas_baja)
print("La nota más alta es: ", mas_alta)
