inversion1 = float(input("Por favor ingrese la inversion de la persona #1: "))


inversion2 = float(input("Por favor ingrese la inversion de la persona #2: "))


inversion3 = float(input("Por favor ingrese la inversion de la persona #3: "))


totalinversion = inversion1 + inversion2 + inversion3

porcentaje1 = (inversion1/totalinversion) * 100
porcentaje2 = (inversion2/totalinversion) * 100
porcentaje3 = (inversion3/totalinversion) * 100


print("De la inversion total de "+"$",totalinversion, 
"la persona 1 invirtio"+"$",inversion1," que corresponde a el ",porcentaje1,"%")

print("De la inversion total de "+"$",totalinversion, 
"la persona 2 invirtio"+"$",inversion2," que corresponde a el ",porcentaje2,"%")

print("De la inversion total de "+"$",totalinversion, 
"la persona 3 invirtio"+"$",inversion3," que corresponde a el ",porcentaje3,"%")
