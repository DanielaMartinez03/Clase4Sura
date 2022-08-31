#si esta entre o y 20 mtrs alarma "Bajo nivel de agua"
#Si esta entre 20 y 400 mtrs ok
#Si esta por encima de 400 mtrs alarma " Alto nivel de agua"

#ENTRADAS= VARIABLES = REFERENCIAS EN MEMORIA
nivelAgua = float(input("Digite el nivel de agua actual: "))

#PROCESO
if (nivelAgua>=0 and nivelAgua<20):
    print( f'El nivel de agua es: {nivelAgua} y este es Bajo') #SALIDA
elif (nivelAgua>=20 and nivelAgua<400):
    print(f'El nivel de agua es: {nivelAgua} y esta operando normalmente') #SALIDA
elif (nivelAgua>=400):
    print(f'El nivel de agua es: {nivelAgua} y este nivel es Alto') #SALIDA
else:
    print(f'El nivel de agua no es valido') #SALIDA

