redes = int(input("Total alumnos de redes: "))
contabilidad = int(input("Total alumnos de contabilidad: "))
diseño = int(input("Total alumnos de diseño: "))

totalalumnos = redes + contabilidad + diseño


porcentajeredes = (redes/totalalumnos) * 100
porcentajecontabilidad = (contabilidad/totalalumnos) * 100
porcentajediseño = (diseño/totalalumnos) * 100


print("El total de alumnos es ",totalalumnos,)

print("El porcentaje de alumnos de redes es ",porcentajeredes,"%")

print("El porcentaje de alumnos de contabilidad es ",porcentajecontabilidad,"%")

print("El porcentaje de alumnos de diseño es ",porcentajediseño,"%")
