#Enero. Febrero, Marzo = Invierno
#Marzo, Abril, Mayo = Primavera
#Julio, Agosto, Septi = Verano
#Oct. Nov Dic = Otoño
#digitar el mes con teclado y devuelva la estacion 
Mes = input("Digite el mes del año: ").lower()


#PROCESO
if (Mes == "enero" or Mes == "febrero" or Mes == "marzo"):
    print( f'Estamos en Invierno') #SALIDA
elif (Mes == "sbril" or Mes == "mayo" or Mes == "junio"):
    print(f'Estamos en Primavera') #SALIDA
elif (Mes == "julio" or Mes == "agosto" or Mes == "septiembre"):
    print(f'Estamos en Verano') #SALIDA
elif (Mes == "octubre" or Mes == "noviembre" or Mes == "diciembre"):
    print(f'Estamos en Otoño') #SALIDA
else:
    print(f'Opción no válida') #SALIDA