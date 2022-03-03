base = float(input("Por favor ingrese su sueldo base: "))


ventas = float(input("Por favor ingrese el total de ventas que realizo: "))


comision = 15 * ventas / 100

total = base + comision

print("Su sueldo base es "+"$",base,)

print("De las ventas totales de "+"$",ventas, 
"la comision del 15% "+"es",comision,)

print("Su sueldo total mas comisiones es "+"$",total,)
