condicion = True

if condicion == False:
     print('Condición verdadera')
elif condicion == False:
    print('Condicion falsa')
else:
    print('Condición desconocida')


numero= int(input('Proporciona un numero entre 1 y 3: '))
numeroTexto=''
if numero == 1:
    numeroTexto= 'Numero 1'
elif numero == 2:
    numeroTexto= 'Numero 2'
elif numero == 3:
    numeroTexto = 'Numero 3'
else:
    numeroTexto ='Valor Fuera de Rango'

print(f'El número ingresado es:  {numero} - {numeroTexto}')


mes= int(input("Ingresa el mes del año: "))
estacion= None
if mes == 1 or mes == 2 or mes == 12:
    estacion='Invierno'
elif mes == 3 or mes==4 or mes==5:
    estacion= 'Primavera'
elif mes== 6 or mes== 7 or mes==8:
    estacion='Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion= 'Otoño'
else:
    estacion='Mes incorrecto'

print(f'Para el mes {mes} la estación es {estacion}')

edad= int(input('Proporciona tu edad'))
mensaje= None
if edad >= 0 and edad <10:
    mensaje= 'La infancia es increible....'
elif edad >=10 and edad <20:
    mensaje= 'Muchos cambios y mucho estudio'
elif edad >=20 and edad <30:
    mensaje= 'Amor y comienza el trabajo...'
else:
    mensaje='Etapa de vida no reconocida'

print(f'Para la edad de {edad} años la frase es... --  {mensaje} --')

print(f'Para el mes {mes} la estación es {estacion}')

nota= int(input('Proporciona un valor entre 0 y 10'))
notaFinal= None
if nota>= 9 and nota<11:
    notaFinal= 'A'
elif nota >= 8 and nota <9:
    notaFinal= 'B'
elif nota >=7 and nota <8:
    notaFinal= 'C'
elif nota >=6 and nota <7:
    notaFinal= 'D'
elif nota >= 0 and nota <6:
    notaFinal = 'F'
else:
    notaFinal='Valor desconocido'

print(notaFinal)