#Dictionaries
#data type similar to arrays, but works with keys and values instead of indexes

#Crear un dictionary
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

#Otra forma de hacer lo mismo:
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

#Iterating over dictionaries
#a != de listas. No mantienen el orden -> son desordenados. X eso no tienen indice.

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

#Removing a value
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
#del
del phonebook["John"]
print(phonebook)
# .pop(key)
phonebook.pop("Jack")
print(phonebook)



'''Exercise
Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook. '''
phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
# your code goes here(solucionado)
phonebook["Jake"] = 938273443  
del phonebook["Jill"]  

# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")  
