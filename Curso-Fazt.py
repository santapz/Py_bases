# nuevo tipo de dato

n = None      #es un dato no definido aún
print(n)

#ordenar DICCIONARIO

d = {
    'name':'leo',
    'edad':18,
    'altura':1.74
}
print(d)                #Se imprime en horizontal


# crear 2 variables en una misma linea
x, book = 100, 'I Robot'        #x = 100
                                #book = 'I Robot'
print(x, book)


# Conventions - convenciones, formas tipicas de escribir variables
book_name = '100 años de soledad' #Snake Case -->Py
bookName = '1984'                 #Camel Case -->Js
BookName = 'El Principito'        #Pascal Case
#En Gral se usan mas snake y camel


#Convencion p val Constantes. con MAYUSCULAS ej valor de pi:
PI = 3.1416
MY_NAME = 'Santiago'

'''Strigs'''

#DIR() muestra todo lo q se púede hacer cn un dato

'''upper y lower hacen TODO May o min'''
c = 'SOAS'

#Aquí abajo, transformo en comentario para que no se ejecute, con #

# print(dir(c))
print(c.lower())

#TITLE hace MAY la 1° letra de cada palabra
s = 'hola mundo' #Hola Mundo
print(s.title())

#SWAPCASE--- cambia si hay 1 May a min y viceversa
c = 'hOLA'
print(c.swapcase())

#CAPITALIZE -- cambia solo la primer letra a May
t = 'hola mundo' #Hola mundo
print(t.capitalize())

#REPLACE -- reemplaza 1 parte de la cadena
c = 'hola mundo'
print(c.replace('mundo','soquete'))
#combino 2 funciones
print(c.replace('mundo','soquete').upper())



