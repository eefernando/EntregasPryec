numElevar = int(input('dime el numero: '))
print('quieres elevarlo al 1.cuadrado o 2.cubo')
opcion = int(input('Escribe la opcion 1 - 2: '))


if opcion == 1 :
    print(f"El numero {numElevar} al cuadrado es: {numElevar ** 2}")
elif opcion == 2:
    print(f"El numero {numElevar} al cubo es: {numElevar ** 3}")
else:
    print('opcion incorrecta')
