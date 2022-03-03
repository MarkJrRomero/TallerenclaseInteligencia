inversion = float(input("Por favor ingrese la inversion total: "))

Administración = 35 * inversion / 100
Sistemas = 25 * Administración / 100
Telecomunicaciones = 10 * Sistemas / 100

restante = inversion - (Telecomunicaciones + Sistemas + Administración)

Contabilidad = restante




print("Del valor dado a sitemas que es "+"$",Sistemas, "el 10% que es "+"$",Telecomunicaciones," sera entregada a telecomunicaciones.")
print("Del valor dado a administracion que es "+"$",Administración, "el 25% que es "+"$",Sistemas," sera entregada a sistemas.")
print("Del valor total de la inversion que es "+"$",inversion, "el 35% que es "+"$",Administración," sera entregada a administracion.")
print("De la inversion total de "+"$",inversion, "el restante que es "+"$",Contabilidad," sera entregada a contabilidad.")