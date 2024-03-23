'''CURSO PROGRAMACION ATS'''


'''Operadores aritméticos'''
resultado = 10 + 5
print(resultado)
print(type(resultado))
#opciones de lo mismo
n1 = 18
n2 = 5
resultado = n1 / n2
print(resultado)
print(type(resultado))
#modulo
res = n1 % n2
print(res)
#exponenciacion
n3 = 2
n4 = 4
res = n3**n4
print(res)
#prioridad de los operadores
resultado = 3**3 * (13/5 - (2*4))
print(resultado)

#
n1 = 10
n2 = 5
text = "resultado:"
suma = n1/n2*(1+(10/5))

print(text, suma)

#Salidas
nombre = "Titi"
edad = 29
print("hola",nombre,"tienes",edad,"años")
print("hola {} tienes {} años".format(nombre,edad))
print(f"hola {nombre} tienes {edad} años")

#Entrada de datos
nombre = input("digite su name: ")   #cadena
print(f"Que onda {nombre}")
#numericos int y float
num = float(input("ponga un n°: "))  #cambiar int x float(enteros y decimales)
print(f"el n° es {num + 3}")


'''FUNCIONES INTEGRADAS'''
#pasar n entero/decimal a cadena
n = str(10.94)
print(n)
print(type(n))
#pasar entero a Binario y hexadecimal
m = hex(10)             #cambiar fnes: BIN Y HEX
print(m)
print(type(m))
#Valores bin y hex a enteros
c = int("0b1010",2)
print(c)
d = int("0xa",16)
print(d)
#valor absoluto
n = abs(4)
print(n)
#round (redondear)
n = round(5.4)
print(n)
#len (cuenta caracteres de una cadena)
a = len("la calor")
print(a)

#operadores relacionales
resultado = 10 != 20
print(resultado)
print(type(resultado))

#combinacion operaciones aritmeticas + relacionales
a = 2
b = 4
c = 6
res = a+b == c
print(res)

#operadores lógicos
a = 10
b = 12
c = 13
d = 10
resultado = ((a>b) or (a<c)) and ((a==c) or (a>=b))
print(resultado)
resultado = not(a==d) or (b>c)
print(resultado)
#operadores de asignacion
a = 10  #valor inicial
a += 5  #suma en asignacion
a -= 10 #resta ...
a *= 2  # mult
a /= 5  # division
a **= 3 # potencia
a %= 3  #modulo
print(a)

#intercambiar valores de 2 variables
a = float(input("a es:"))      #int y float son opcionales, sino serian str con texto
b = float(input("b es:"))

a , b = b , a
print(f" the new valor for a is:{a}")
print(f" the new valor for b is:{b}")

#CIRCUNFERENCIA ingresar radio y reportar Area y longitud
r = float(input("el radio es: "))
import math            #pi se hace con import math math.pi o con 3.14
l = 2*r*math.pi
a = math.pi*r**2

print(f"longitud es {l:.2f}")
print(f"área es {a:.2f}")

#EJERCICIO compras con descuento
#compras:
c1 = float(input("precio c1:"))
c2 = float(input("precio c2:"))
c3 = float(input("precio c3:"))
#15% desc
Total = c1+c2+c3            #total es precindible
descuento = Total*0.15
precio_final = Total - descuento          #tiene guion bajo para que me acepte la variable

print(f" el precio final a pagar es de ${precio_final:.2f}")

#CONDICIONALES
a = int(input("digite un num: "))
if a>0:
    print("el numero es positivo")
elif a==0:
    print("el n° es 0")
else:
    print("El n° es negativo")

'''Condicionales combinados'''
edad = int(input("digite su edad: "))

if 0<edad<100:                    #es = a edad>0 and edad<100:
    print("edad correcta")
    if edad>=18:
        print("es mayor de edad")
    else:            #puede ir if 0<edad<18 pero no hace falta
        print("es menor de edad")
elif edad>=100:
    print("Probablemente este muerto")
else:
    print("Edad incorrecta")


'''Progama para saber
 si 2 n° son pares o no'''
num1 = int(input("digite 1 num: "))
num2 = int(input("digite otro num: "))

if num1%2==0 and num2%2==0:
    print(f"{num1} y {num2} son pares")
elif num1%2==0 and num2%2!=0:
    print(f"{num1} es par y {num2} es impar")
elif num1%2!=0 and num2%2==0:
    print(f"{num1} es impar y {num2} es par")
else:
    print(f"{num1} y {num2} son impares")

#progama q pida 3 n° y q determine cual es el mayor

n1 = int(input("num 1 -> "))
n2 = int(input("num 2 -> "))
n3 = int(input("num 3 -> "))

if n1>=n2 and n1>=n3:
    print(f"el {n1} es el mayor de todos")
elif n3<=n2>=n1:
    print(f"el {n2} es el mayor de todos")
elif n1<=n3>=n2:                            #no va ELSE xq podria tomar otras resultados
    print(f"el {n3} es el mayor de todos")

'''Hacer programa q pida 1 caracter
 y determine si es una vocal o no'''

letra = input("Digite una letra: ").lower()

if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
    print(f"{letra} es una vocal")
else:
    print(f"{letra} no es una vocal")
#.LOWER cualq vocal en MAY p ej 'A' me da NO VOCAL... solucion .lower
#.UPPER transforma a mayuscula
ejemplo = input("digite minuscula: ").upper()
print(ejemplo)

'''Programa q simule 1 CALCULADORA con sus 4 op básicas.
El usuario debe especificar la operacioon con el promer caracter del nombre de la op.

S, s = Suma
R, r = Resta
M, m, P, p = Multiplicacion
D, d = Division
'''

n1 = float(input("valor n1: "))
n2 = float(input("valor n2: "))

operador = input("digite tipo operacion: ").upper()

if operador == 'S':
    print(f"\nLa suma es {n1+n2}")
elif operador=='R':
    print(f"\nLa resta es {n1-n2}")     #se puede hacer suma=n1+n2 ejemplo en multipl:
elif operador=='P' or operador=='M':
    mult = n1*n2
    print(f"\nLa multiplicacion es {mult:.2f}")
elif operador=='D':
    print(f"\nLa division es {n1/n2:.2f}")
else:
    print("\noperacion incorrecta")

'''Programa que simula un CAJERO c un saldo inicial de 1000$ y
que tenga el sigte menu:
'''
saldo = 1000

print("\t<<<MENU>>>")       #\t me da 4 espacios o una tabulacion p q salga menu cmo titulo
print("1.Ingresar dinero en la cuenta")         #Menu
print("2.Retirar dinero de la cuenta")
print("3.Mostrar dinero de la cuenta")
print("4. Salir")
opcion = int(input("Digite una opcion: "))

print()                 #Este print me da un salto de linea

if opcion == 1:
    ingreso = float(input("Cuánto dinero desea ingresar: "))
    saldo += ingreso
    print(f"Dinero en la cuenta: ${saldo}")
elif opcion==2:
    retiro = float(input("ingrese monto a retirar: "))
    if retiro>saldo:
        print("Usted no tiene esa guita")
    else:
        saldo -= retiro
        print(f"Dinero en la cuenta: ${saldo}")
elif opcion==3:
    print(f"Dinero en la cuenta: ${saldo}")
elif opcion==4:
    print("Gracias por utilizar este cajero")
else:
    print("Opcion incorrecta")


    '''#LISTAS (class list)'''

lista = ['Lunes','Martes','Mierc','Jueves','Viernes']
print(lista[-1])
print(lista[0:4])
#Funcion len para contar elementos
lista = ["R","Sol",23,5.54,False,[23,"h"],0]
print(len(lista))
#agregar datos al final
lista = [1,2,3]
lista.append(4)
lista.append("mmm")
#agregar datos en lugar especifico
lista = [1,2,3,5]  #Falta 4
lista.insert(3,4)
#agregar varios elementos al FINAL
lista = [1,2,3]
lista.extend([4,5,6])
#sumar elementos
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1 + lista2
print(lista3)
#Buscar en lista
lista = [1,2,3,'titi']
print(3 in lista)   #da true o false
#Buscar en qué INDICE esta el elemento
lista = [1,2,3,'titi']
print(lista.index("titi"))
#Contar elementos repetidos
lista = [1,2,3,'titi',5,5.6,1,"titi",2,1]
print(lista.count("titi"))
print(lista.count(10))   # 0 xq no hay
#Eliminar x indice
lista = [1,2,3,"sol"]
lista.pop()     #vacio toma el ultimo valor
print(lista)
lista.pop(1)
#Eliminar x elemento
lista = [1,2,3,"sol"]
lista.remove("sol")
#Eliminar toda la lista
lista = [1,2,3,"sol"]
lista.clear()
print(lista)
#Revertir orden
lista = [1,2,3,"sol"]
lista.reverse()
print(lista)
#Multiplicar
lista = [1,2,3,"sol"]*2
print(lista)
#ordenar ascendentemente
lista = [3,5,-4,0,-1,7]
lista.sort()
print(lista)
#ordenar descendentemente
lista.sort(reverse=True)
print(lista)
'''# print(len(lista)) te muestra la cantidad de indices que tiene la lista, en este caso, 5
# lista.append(valor) agrega un valor de cualquier tipo, al final la lista
# lista.insert(indice,valor) esto agrega un valor a un lugar determinado de la lista.
# lista.extend([]) concatena la lista con otra lista
# Las listas se pueden sumar
# Se puede preguntar si hay un valor en la lista, ejemplo
# print(3 in lista), el resultado se da en un valor booleano
# (lista.index(valor)) indice donde esta el valor
# (lista.count(valor)) cuantas veces se repite el valor en la lista
# (lista.pop(indice)) se elimina el valor indicando el indice
# lista.remove(valor) se elimina el valor
# lista.clear se borra toda la lista
# lista.sort se ordena la lista de menor a mayor
# lista.sort(reverse=true) mayor a menor'''

    #TUPLAS (class tuple)
'''Son listas Inmutables'''

tupla = (4,0,"dog",[1,2,3],5.6)
print(tupla.index(4))   #el 1ro q encuentra, xq se repite el 4
print(4 in tupla)
print(tupla[2])
print(tupla.count(0))
print(len(tupla))
#transformar Tupla en Lista y viceversa
tupla = (4,0,"dog",[1,2,3],5.6)
lista = list(tupla)
print(lista)
print(tupla)        #sigue ahí, solo se crea una 2da variable 'lista'
#lista a tupla
lista = [4,0,"dog",[1,2,3],5.6]
tupla = tuple(lista)
print(lista)
print(tupla)

    #CONJUNTOS (Class set)... 
'''Elemenos se agregan de mandera desordenada y sin duplicados.
   Se imprimen en orden aleatorio, y los duplicados(si los hay) no se muestran
   Las fn q usen apendices no sirven (.pop, .apend, .insert) 
'''
conjunto = set()                #siempre comienza con set() xq sino lo toma como diccionario
conjunto = {1,2,3,'hi',4.5,1}      #el duplicado se muerstra solo 1 vez "1"
print(conjunto)

#agregar elemento
conjunto = set()
conjunto = {1,2,3,'hi',4.5}
conjunto.add('g')       #te lo agrega en cualq lugar de la lista(desordenado)
print(conjunto)

#eliminar 1 elemento
conjunto = set()
conjunto = {1,2,3,'hi',4.5}
conjunto.discard('hi')
print(conjunto)

#eliminar_todo
conjunto.clear()
print(conjunto)

#buscar
conjunto = set()
conjunto = {1,2,3,'hi',4.5}

print('hi' in conjunto)   #buscar 1 valor   T o F
print('bye' not in conjunto)     #negacoion "no esta dentro de"

#Comenzar sin set() xq al separar con , (comas) ya lo toma como conj
#el diccionario usa : (dos puntos)
conjunto = {1,2,3,'hi',4.5}
print(conjunto)
print(type(conjunto))

#Igualdad
a = {1,2,3}
b = {3,4,5}
print(a==b)   #False
a = {1,2,3}
b = {3,1,2}     # =elementos desordenados -> True
print(a==b)

#Contar elementos
a = {1,2,3}
b = {3,4,5}
print(len(b))

#Union
a = {1,2,3}
b = {3,4,5}
c = a | b   #el 3 es duplicado x lo q no se repite
print(c) #1,2,3,4,5

#Interseccion (Elemento q comparten ambos)
a = {1,2,3}
b = {3,4,5}
c = a & b   #shift + 6
print(c)    # = 3

#Diferencia (Elem de a q no estan en b. 'a - b')
a = {1,2,3}
b = {3,4,5}
c = a - b
print(c) #1,2
d = b - a #4,5
print(d)
#Diferencia simetrica (Elem de a y b pero q no estan en ambos)
a = {1,2,3}
b = {3,4,5}
c = a ^ b    # alt + 94
print(c) #1,2,4,5

#Subconjuntos:  determinar si hay conj dentro de otro c.
a = {1,2,3}
b = {3,4,5}
c = {1,2,3,4,5}
print(a.issubset(c))  # b tambien es True
c = {1,2,3,5}
print(b.issubset(c))  #False xq no estan todos los elem de b
#Superconjunto
a = {1,2,3}
b = {3,4,5}
c = {1,2,3,5}
print(c.issuperset(a)) #T, b -> F

#Conj disconexos:  no comparten ningun elemento
a = {1,2,3}
b = {4,5}
print(a.isdisjoint(b)) # True

#Conj INMUTABLES
a = frozenset({1,2,3})
a.add(5)   
print(a)

'''DICCIONARIOS (class dict)
Desordenados. 2 elem x posicion -->clave y valor
No se duplican claves'''

diccionario = {}            #dicc vacio
print(diccionario)
print(type(diccionario))   #class 'dict' de diccionario

#Traducior colores Esp-Ing
dic = {"azul":"blue","rojo":"red","verde":"green"}
    # clave:valor
print(dic)      #muerstratodo
#un valor
dic = {"azul":"blue","rojo":"red","verde":"green"}
print(dic["azul"])
#agregar un color
dic["amarillo"] = "yellow"
print(dic)
#modificar un valor
dic["azul"] = "BLUE"
print(dic)
#Eliminar
dic = {"azul":"blue","rojo":"red","verde":"green"}
del(dic["azul"])
print(dic)

#Otros valores y listas,tupla, dicc dentro de dicc
dic = {"Juan":[30,1.90],"Maria":{"edad":25,"estatura":1.57},"Pepe":("edad:",19,"estatura:",1.70)}
print(dic)
print(dic["Maria"])

#Dorsal y jugador
equipo = {10:"Dybala",11:"Costas",7:"Ronaldo"}
print(equipo)
print(equipo[7])
print(equipo[6])   #error xq no existe
# .get para evitar error
equipo = {10:"Dybala",11:"Costas",7:"Ronaldo"}
print(equipo.get(10,"No existe el jugador con esa dorsal"))
print(equipo.get(16,"No existe el jugador con esa dorsal"))
#busqueda
print(10 in equipo)
#Mostrar todas las claves
print(equipo.keys())
#mostrar jugadores(valores)
print(equipo.values())
#mostrar_todo(clave + val)
print(equipo.items())
#contar elementos(par k:v)
print(len(equipo))
#borrar_todo
equipo.clear()
print(equipo)

'''PILAS.
se agregan elementos al final (apilar) y
se sacan del final(el ultimo q entra) se desapila'''

pila = [1,2,3]      # = lsta comun
#agrego elem al final
pila.append(4)  #apilo
pila.append(5)
print(pila)
#saco elementos
pila.pop()      #desapilo
print(pila)

#uso el retorno del valor de .pop
n = pila.pop()      # = n° 5
print(f"Saco el elemento {n}")   # n=5
print(pila)
n = pila.pop()
print(f"Saco el elemento {n}")  # n=4
print(pila)

'''COLA
estructura de dato fijo, primero en entrar y primero en irse. ejemplo cola de banco'''
# from collections import deque
# para importar la cola pero no hace falta es la misma bosta

cola = ['gonzalo','santiago','manuela','paula']
#agregar al final cola
cola.append('julia')
cola.append('mario')

print(cola)

#Sacando elementos al ppio de la cola
n = cola.pop(0)  #o cola.remove('gonzalo') mas complicado al pedo
print(f"Atendiendo a {n}")
n = cola.pop(0)
print(f"Atendiendo a {n}")
print(cola)

'''ejercicio: lista q contenga n repetidos, eliminarlos y mostrar lista'''

lista = [1,2,2,7,1,9,2]
#1 resolucion
conjunto = set(lista)
lista = list(conjunto)
#2 resolucion (mas resumida)
lista = list(set(lista))

print(lista)

'''ejercicio: programa c 2 listas. a la vez crear sigtes listas: (no debe
haber repeticiones)
1.lista palabras q aparecen en las 2 listas(todas)
2.palab aparec 1 pero no en la 2da
3. en 2da pero no 1ra
4. en ambas(repetidas)'''

l1 = [2,5,8,1,3,8,5,1,9,9,5,5]
l2 = [4,6,0,1,6,1,0,4,7,8,1,6]
#borrar repetidos
a = set(l1)
b = set(l2)
#1 lista con todas palabras
l3 = list(a | b)   #union
print(f"la lista con todas las palabras es {l3}")
#2 palab l1 pero no l2
l4 = list(a - b)    #diferencia
print(f"la lista con palab l1 pero no l2 es {l4}")                #falta dif simetrica ^
#3 palab l2 pero no l1
l5 = list(b - a)
print(f"la lista con p l2 pero no l1 es {l5}")
#4 palabras repetidas ambas l
l6 = list(a & b)    #intersecc
print(f"lista con p repetidas en ambas es {l6}")

'''Ejercicio 1 lista con noommbre señor de los anillos :
nombre,clase,raza'''

personajes = []     #crear lista vacia p ir llenando

p = {'N':'Aragorn','C':'Guerrero','R':'Dunadan del norte'}
personajes.append(p)

p = {'N':'Legolas','C':'Arquero','R':'Elfo'}
personajes.append(p)

p = {'N':'Gandalf','C':'Mago','R':'Istar'}
personajes.append(p)

print(personajes)

''' BUCLE WHILE
Se ejecuta indeterminadas veces. necesita condicion'''

import math
#sacar raiz cuadrada (debe ser un n positivo sino es un error)

num = int(input("digite n° ->"))
while num<0:
    print("Error, el num debe ser positivo")
    num = int(input("digite n° -->"))

print(f"\nLa raiz cuadrada del num es: {(math.sqrt(num)):.2f}")

# mostrar = msj 10 vces
i = 0
while i<10:
    print('hola mundo')
    i += 1
# mostrar numeros
i = 0
while i<10:
    print(i)
    i += 1

'''BUCLE FOR'
utiliza colecciones -> lista,tuple,conj,dic etc'''

#muestra 3 veces xq hay 3 elementos
for a in [1,'a',-3]:
    print('hola')
#muestra elementos de la variable i
for i in [1,'a',-3]:
    print(f'elemento: {i}')
#coleccion en otra variable
coleccion = [9,0,'z']           #puede ser otra colecc listas, tupla, etc
for b in coleccion:
    print(f"elementos: {b}")

#diccionario
c = {'sol':25,'marta':56,'pepe':89}
for i in c:
    print(f"elementos: {i}") #imprime keys
#ver valores-edades
for i in c:
    print(c[i])
#clave y valor
for i in c:
    print(f"{i} -> {c[i]}")
#lo mismo pero mas usado
for clave,valor in c.items():
    print(f"{clave} -> {valor}")

#cadena
c = "santi"
for a in c:
    print(a)
#sin saltos de linea
for a in c:
    print(f"{a}",end=".")   #puede ir espacio o no, o pto o lo q sea




















