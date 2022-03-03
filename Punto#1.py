inversion = float(input("Por favor ingrese la inversion total: "))

Administración = 35 * inversion / 100
Sistemas = 25 * Administración / 100
Telecomunicaciones = 10 * Sistemas / 100

restante = inversion - (Telecomunicaciones + Sistemas + Administración)

Contabilidad = restante




print("De la inversion total de "+"$",inversion, "el 10% que es "+"$",Telecomunicaciones," sera entregada a telecomunicaciones.")
print("De la inversion total de "+"$",inversion, "el 10% que es "+"$",Sistemas," sera entregada a sistemas.")
print("De la inversion total de "+"$",inversion, "el 10% que es "+"$",Administración," sera entregada a administracion.")
print("De la inversion total de "+"$",inversion, "el 10% que es "+"$",Contabilidad," sera entregada a contabilidad.")