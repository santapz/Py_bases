'''Usar comillas simples y dobles.
 Conviene la "" cuando queremos poner ''
 ej:'''
astring = "Hello world!"
print("single quotes are ' '")

#len() - Contar caracteres
print(len(astring)) 

#.index - busca el indice del primer caracter
astring = "Hello world!"
print(astring.index("o"))

#Imprme el valor del indice dado
astring = "Hello world!"
print(astring[3]) #l

#Imprimir un pedazo del str
astring = "Hello world!"
print(astring[0:2]) #He 
print(astring[:2])  #He 
print(astring[2:])  #llo world!

#Negative
print(astring[3:-2]) #lo worl

# n : n-1 (most programming languages do this)
print(astring[3:7]) #lo w   

#from 3 to 7 skipping one character. This is extended slice syntax.
#The general form is [start:stop:step].
astring = "Hello world!"
print(astring[3:7:1]) #lo w

#Reverse a String
astring = "Hello world!"
print(astring[::-1]) #!dlrow olleH

#Escape Characters --> https://www.w3schools.com/python/gloss_python_escape_characters.asp
# \'  Single Quote
# \\ 	Backslash
# \n 	New Line
# \r 	Carriage Return
# \t 	Tab
# \b 	Backspace
# \f 	Form Feed
# \ooo 	Octal value
# \xhh 	Hex value

#uppercase and lowercase,
astring = "Hello world!"
print(astring.upper())
print(astring.lower())

#Ver si comienza o termina con algo en particular
astring = "Hello world!"
print(astring.startswith("Hello")) #True
print(astring.endswith("asdfasdfasdf")) #False

#.split - divide una str y retorna una lista
astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords) #['Hello', 'world!']


'''Exercise
Try to fix the code to print out the correct information by changing the string.'''

s = "Hey there! what should this string be?"   #solution: s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))