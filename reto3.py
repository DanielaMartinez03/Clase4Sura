#Edad entre 0 y 14 Niño
#edad entre 14 y 28 Joven
#edad entre 28 -62 Adulto
#edad entre 60 - 100 Adulto Mayor


Edad = int(input("Digite su edad: "))


#PROCESO
if Edad>=0 and Edad<14:
    print( f'Usted es Niño') #SALIDA
elif Edad>=14 and Edad<28 :
    print(f'Usted es Joven') #SALIDA
elif Edad>=28 and Edad<60 :
    print(f'Usted es Adulto') #SALIDA
elif Edad>=60 and Edad<=150 :
    print(f'Usted es Adulto Mayor') #SALIDA
else:
    print(f'Edad ingresada no válida') #SALIDA