"""""
TIPOS DE DATOS EN PYTHON
miVariable="Hola desde Python"
print(miVariable)

x=10
y=2
z=x+y
print(z)
print (id(x))
print(id(y))
print(id(z))

#TIPO INT
x=10
print(x)
print(type(x))
#TIPO FLOAT
x=10.5
print(x)
print(type(x))
#TIPO STRING
x="HOLA MUNDO"
print(x)
print(type(x))
#TIPO BOLEAN
x=True
print(x)
print(type(x))
x=False
print(x)
print(type(x))


# MANEJO DE CADENAS EN PYTHON
# concatenación
miGrupoFavorito = "Aerosmith"
comentario = 'Mentira es ACDC'
# print("Mi grupo favorito es: "+ miGrupoFavorito + comentario)
print("Mi grupo favorito es", miGrupoFavorito, comentario)
numero1 = "1"
numeor2 = "2"
print("Suma", int(numero1) + int(numeor2))
print("Concatenación", numero1 + numeor2)

numero1 = 1
numeor2 = 2
print(numero1 + numeor2)

#Tipos de dato Booleanos(Bool)
miVariable= False
print(miVariable)
miVariable= 3>2
print(miVariable)


if miVariable:
    print("El resultado fue verdadero")
else:
    print("El resultado es falso")


#Procesar entrada de usuario
resultado=input("Escribe un mensaje: ")
print("Valor proporcionado:", resultado)
print("Fin del programa")



Numero1=int(input("Escribe el primer numero: "))
Numero2=int(input("Escribe el segundo numero: "))

resultado=Numero1+Numero2
print("El resultado es:", resultado)
"""
Dia=int(input("¿Cómo estuvo tu día (1/10): "))
if Dia > 10:
    print("Ingresa un valor menor de 10 animal")
else:
    print("Mi día estuvo", Dia, "de 10")

titulo=input("Proporciona el titulo")
autor=input("Proporciona el autor")
print("Proporciona el título:", titulo)
print("Proporciona el autor:", autor)
print(titulo, "fue escrito por", autor)


#Operadores aritmeticos

