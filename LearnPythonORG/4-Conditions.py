'''CONDITIONS'''

x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True


'''The "and" and "or" boolean '''

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")


'''The "not" operator'''

print(not False) # Prints out True
print((not False) == (False)) # Prints out False


'''The "in" operator.
 Could be used to check if a specified object exists within an iterable object container, such as a list:'''

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")



'''Elif & Else'''

statement = False
another_statement = True
if statement is True:
    # do something
    pass            #pass --> operacion que no hace nada, es para poner ejemplos, como el null de js
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass


'''The 'is' operator:
    '==' is for value equality. It's used to know if two objects have the same value.
    'is' is for reference equality. It's used to know if two references refer (or point) to the same object, i.e if they're identical. Two objects are identical if they have the same memory address.'''

x = [1,2,3]
y = [1,2,3]
z = x
print(x == y) # Prints out True  (== valores. No importa el espacio en la memoria)  
print(x is y) # Prints out False (ocupan != espacios de memoria, pero == valores)
print(x is z) # Prints out True  (ocupan == espacios de memoria)



'''Staments son evaluados como T cuando:
- Poniendo una variable True o calcualada con una expresion
- Un objeto no vacío
Stament F:
- variable False o expresion F
- Objetos vacios: "", [], 0, 

'''


'''Exercise
Change the variables in the first section, so that each if statement resolves as True'''

# change this code
number = 16
second_number = 0
first_array = [1, 2, 3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

