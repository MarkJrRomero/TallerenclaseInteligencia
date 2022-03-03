taller1 = float(input("Por favor ingrese la nota del taller 1: "))
taller2 = float(input("Por favor ingrese la nota del taller 2: "))
taller3 = float(input("Por favor ingrese la nota del taller 3: "))

examen = float(input("Por favor ingrese la nota del examen: "))

proyectofinal = float(input("Por favor ingrese la nota del proyecto final: "))

promediotalleres = (taller1+taller2+taller3)/3



porcentaje50 = 50 * promediotalleres / 100
porcentaje30 = 30 * examen / 100
porcentaje20 = 20 * proyectofinal / 100

notafinal = porcentaje50 + porcentaje30 + porcentaje20

print("Del promedio de los talleres ",promediotalleres, "el 50% es",porcentaje50,)

print("De la nota del examen ",examen, "el 30% es",porcentaje30,)

print("De la nota del examen ",proyectofinal, "el 20% es",porcentaje20,)

print("La nota final es ",notafinal,)
