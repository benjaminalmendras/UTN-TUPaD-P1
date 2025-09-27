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
print()

# Ejercio 2
print("Ejercicio 2")

lista_2 = []

for i in range(5):
    producto = input(f"Ingrese el producto num. {i + 1}: ")
    producto = producto.lower
    lista_2.append(producto)
    
print("Lista ordenada: ")
print(sorted(lista_2))

eliminar = input("Ingrese el producto que desea eliminar: ")
eliminar = eliminar.lower

if eliminar in lista_2:
    lista_2.remove(eliminar)
    print("Producto eliminado. Lista actualizada:", lista_2)
else:
    print("El producto no está en la lista.")

print("Lista Actualizada: ")
print(sorted(lista_2))
print()

# Ejercicio 3
print("Ejercicio 3")

lista_3 = []
lista_3_par = []
lista_3_impar = []

for i in range(15):
    num_3 = random.randint(1, 100)
    lista_3.append(num_3)
    
for i in range(len(lista_3)):
    if lista_3[i] % 2 == 0:
        lista_3_par.append(lista_3[i])
    else:
        lista_3_impar.append(lista_3[i])
    
print("Lista Completa: ")
print(lista_3)
print("Lista de Pares: ")
print(lista_3_par)
print("La cantidad de elementos pares es de: ", len(lista_3_par))
print("Lista de Impares: ")
print(lista_3_impar)
print("La cantidad de elementos impares es de: ", len(lista_3_impar))
print()

# Ejercicio 4
print("Ejercicio 4")

datos_4 = [1, 3, 5, 3, 7, 1, 9, 5, 3]
lista_4 = []

for i in range(len(datos_4)):
    if datos_4[i] not in lista_4:  
        lista_4.append(datos_4[i])

print("Lista sin repetidos:")
print(lista_4)
print()

# Ejercicio 5
print("Ejercicio 5")

lista_5 = []
nombres = ["Juan", "Alfredo", "Joaquin", "Roberto", "Germán", "Luquitas", "Jazmín", "Romina", "Victoria", "Sofía", "Valentina"]
apellidos = ["Almendras", "Pérez", "Rodriguez", "Gonzalez", "Gallardo", "Allende", "Montes", "Gómez", "Fernández", "López"]

menu_opc_5 = "Menú de Opciones \n"
menu_opc_5 += "1- Agregar un nuevo estudiante \n"
menu_opc_5 += "2- Eliminar un Estudiante\n"
menu_opc_5 += "0- Salir y mostrar lista completa\n"
menu_opc_5 += "Ingresar opción: "

for i in range(8):
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    nom_completo = nombre + " " + apellido
    lista_5.append(nom_completo)

opc = -1
while opc != 0:
    opc = int(input(menu_opc_5))
    if opc == 1:
        nombre_nuevo = input("Ingrese el nombre completo a agregar: ")
        nombre_nuevo = nombre_nuevo.title
        lista_5.append(nombre_nuevo)
        print("Estudiante agregado!")
        
    elif opc == 2:
        nombre_a_eliminar = input("Ingresar el nombre completo a eliminar: ")
        nombre_a_eliminar = nombre_a_eliminar.title
        if nombre_a_eliminar in lista_5:
            lista_5.remove(nombre_a_eliminar)
            print("Alumno Eliminado!")
        else:
            print("Error! Ese alumno no está en la lista ")
    
    elif opc == 0:
        print("Lista Completa: ")
        for alumno in lista_5:
            print("-", alumno)
    
    else:
        print("Opción Incorrecta!")

print()

# Ejercicio 6
print("Ejercicio 6")

lista_6 = [1, 2, 3, 4, 5, 6, 7]
lista_6 = [lista_6[-1]] + lista_6[:-1]

print(lista_6)
print()

# Ejercicio 7
print("Ejercicio 7")

lista_7 = []
cont_min = 0
cont_max = 0
mayor_amplitud_termica = None
dia_mayor_amplitud = None

for i in range(7):
    temp_min = round(random.uniform(-5, 20), 2)
    temp_max = round(random.uniform(21, 40), 2)
    lista_7.append([temp_min, temp_max])

for i in range(len(lista_7)):
    cont_min += lista_7[i][0]
    cont_max += lista_7[i][1]
    amplitud_termica = lista_7[i][1] - lista_7[i][0]
    if amplitud_termica > mayor_amplitud_termica or mayor_amplitud_termica is None:
        mayor_amplitud_termica = amplitud_termica
        dia_mayor_amplitud = i + 1 

prom_min = round(cont_min / 7, 2)
prom_max = round(cont_max / 7, 2)

print("Temperaturas de la semana (mín, máx):", lista_7)
print("El promedio de las mínimas:", prom_min)
print("El promedio de las máximas:", prom_max)
print("La mayor amplitud térmica fue de", mayor_amplitud_termica, "°C en el día", dia_mayor_amplitud)
print()

# Ejercicio 8
print("Ejercicio 8")

lista_8 = []
cont_mat1 = 0
cont_mat2 = 0
cont_mat3 = 0

for i in range(5):
    mat_1 = random.randint(1, 10)
    mat_2 = random.randint(1, 10)
    mat_3 = random.randint(1, 10)
    lista_8.append([mat_1, mat_2, mat_3])
    
for i in range(len(lista_8)):
    cont_estudiante = lista_8[i][0] + lista_8[i][1] + lista_8[i][2]
    prom_estudiante = round(cont_estudiante / 3, 2)
    cont_mat1 += lista_8[i][0]
    cont_mat2 += lista_8[i][1]
    cont_mat3 += lista_8[i][2]
    
    print("El promedio del estudiante", i + 1, "es: ", prom_estudiante)

prom_mat_1 = round(cont_mat1 / 5, 2)
prom_mat_2 = round(cont_mat2 / 5, 2)
prom_mat_3 = round(cont_mat3 / 5, 2)

print("El promedio de la primera materia es: ", prom_mat_1)
print("El promedio de la segunda materia es: ", prom_mat_2)
print("El promedio de la tercera materia es: ", prom_mat_3)
print()

#Ejercicio 9
print("Ejercicio 9")
print()
print("Ta Te Ti")

lista_9 = []
band_gano = False

for i in range(3):
    lista_9.append(["-", "-", "-"])

print("Tablero")
print()
print(lista_9[0][0], lista_9[0][1], lista_9[0][2])
print(lista_9[1][0], lista_9[1][1], lista_9[1][2])
print(lista_9[2][0], lista_9[2][1], lista_9[2][2])
print()

while not band_gano:
    for i in range(9):
        if i % 2 == 0:
            print(" Turno de X")
            ficha = "X"
        else:
            print(" Turno de O")
            ficha = "O"

        fila = int(input("Ingrese fila (0-2): "))
        while fila > 2 or fila < 0:
            fila = int(input("Error! Ingrese fila (0-2): "))
        col = int(input("Ingrese columna (0-2): "))
        while col > 2 or col < 0:
            col = int(input("Error! Ingrese columna (0-2): "))

        if lista_9[fila][col] == "-":
            lista_9[fila][col] = ficha
        else:
            print("Turno Perdido! Casilla ocupada!")

        print("Tablero")
        print(lista_9[0][0], lista_9[0][1], lista_9[0][2])
        print(lista_9[1][0], lista_9[1][1], lista_9[1][2])
        print(lista_9[2][0], lista_9[2][1], lista_9[2][2])

        if (lista_9[0][0] == lista_9[0][1] == lista_9[0][2] != "-" or
            lista_9[1][0] == lista_9[1][1] == lista_9[1][2] != "-" or 
            lista_9[2][0] == lista_9[2][1] == lista_9[2][2] != "-" or 
            lista_9[0][0] == lista_9[1][0] == lista_9[2][0] != "-" or
            lista_9[0][1] == lista_9[1][1] == lista_9[2][1] != "-" or
            lista_9[0][2] == lista_9[1][2] == lista_9[2][2] != "-" or
            lista_9[0][0] == lista_9[1][1] == lista_9[2][2] != "-" or
            lista_9[2][0] == lista_9[1][1] == lista_9[0][2] != "-"):

            print()
            print("Ganó", ficha)
            band_gano = True
            break

print("Juego Terminado!")
print()

# Ejercicio 10
print("Ejercicio 10")
print()

lista_10 = [[0 for j in range(7)] for i in range(4)] 
cantidad_por_prod_por_semana = [0, 0, 0, 0]
cantidad_ventas_por_dia = [0, 0, 0, 0, 0, 0, 0]
i_dia_mas_vendido = -1
mayor_dia = -1
mayor_prod = -1
i_prod_mas_vendido = -1

for i in range(4):
    for j in range(7):
        venta = round(random.uniform(20, 250),2)
        lista_10[i][j] = venta
        cantidad_por_prod_por_semana[i] += venta
        cantidad_ventas_por_dia[j] += venta

for i in range(len(cantidad_por_prod_por_semana)):
    if mayor_prod <= cantidad_por_prod_por_semana[i]:
        mayor_prod = cantidad_por_prod_por_semana[i]
        i_prod_mas_vendido = i
    print("El total vendido del Producto", (i + 1), "es de: ", cantidad_por_prod_por_semana[i])
    
for i in range(len(cantidad_ventas_por_dia)):
    if mayor_dia <= cantidad_ventas_por_dia[i]:
        mayor_dia = cantidad_ventas_por_dia[i]
        i_dia_mas_vendido = i
        
print("El día con más ventas fue el día ", (i_dia_mas_vendido + 1))
print("El producto más vendido fue el Producto", (i_prod_mas_vendido + 1))