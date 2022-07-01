operandoA = 3
operandoB = 2
suma = operandoA + operandoB
# print('Resultado de la suma:', suma)
print(f'Resultado de la suma {suma}')

resta = operandoA - operandoB
print(f'El resultado de la resta: {resta}')
multiplicacion = operandoA * operandoB
print(f'El resultado de la multiplicacion: {multiplicacion}')
division = operandoA / operandoB
print(f'El resultado de la división: {division}')
divisionint = operandoA // operandoB
print(f'El resultado división tipoo int: {divisionint}')
modulo = operandoA % operandoB
print(f'Resultado residuo(módulo): {modulo}')
exponente = operandoA ** operandoB
print(f'El resultado del exponente: {exponente}')

# Ejercicio
# alto=int(input("Proporciona el alto: "))
# ancho=int(input("Proporciona el ancho: "))
ancho = 2
alto = 2
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f'Area: {area}')
print(f'Perímetro: {perimetro}')

# Operadores de asignación


miVariable = 10
print(miVariable)
miVariable = miVariable + 2
print(miVariable)
# Incremento con reasignación
miVariable += 30
print(miVariable)
miVariable /= 2
print(miVariable)
miVariable *= 20
print(miVariable)

# Operadores de comparación
a = 3
b = 2
# Igual
resultado = a == b
print(f"El resultado es: {resultado}")
# Diferentes
resultado = a != b
print(f"El resultado es: {resultado}")
# Mayor que
resultado = a > b
print(f"El resultado es: {resultado}")

# Ejercicio Par/Impar
# numero=int(input("Por favor ingrese un número: "))
numero = 12
if numero % 2 == 0:
    print(numero, " Es par")
else:
    print(numero, " No es par")

# Ejercicio Edad

# edad=int(input("Por favor ingrese su edad: "))
edad = 18
if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

# Operadores de lógicos

x = True
y = True
resultado = x and y
print(resultado)
resultado = x or y
print(resultado)
resultado = not a
print(resultado)

#Ejercicio operador AND

rango = int(input("INgrese un numero entre 0 y 5: "))
if rango >= 0 and rango <= 5:
    print(f"El valor {rango} está dentro de Rango")
else:
    print(f"El valor {rango} está dentro de Rango")

#Ejercicio operador OR

vacaciones = True
diaDescanso=False
if vacaciones or diaDescanso:
    print('Puede asistir al juego')
else:
    print("Tiene deberes por hacer")

edas = int(input("Ingrese tu edad: "))
if edas >= 20 and edas <= 30:
    print(f"La edad {edas} está dentro de los 20's y los 30's")
else:
    print(f"La edad {edas} no está dentro de los 20's ni  los 30's")

#Ejercicio Numero Mayor
    numero1=int(input("Proporciona el número1: "))
    numero2=int(input("Proporciona el número2: "))
    if numero1 > numero2:
        print(f"El numero mayor es: {numero1}")
    else:
        print(f"El numero mayor es: {numero2}")


nameLibro=input("Proporciona el nombre del Libro: ")
idLibro=int(input("Proporciona el Id: "))
precioLibro= float(input("Proporciona el precio (2 decimales): "))
envioLibro=bool(input(" Indica si el envío es gratuito (True/False): "))
print(f'''
Nombre: {nameLibro}
id: {idLibro}
Precio: {precioLibro}
Envío gratuito?: {envioLibro}
''')
