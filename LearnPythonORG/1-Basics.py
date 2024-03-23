'''PRINT
in Python 3, it is a function, and must be invoked with parentheses.'''

print("This line will be printed.")

'''INDENTATION'''
x = 1
if x == 1:
    # indented four spaces(or TAB)
    print("x is 1.")

'''VARIABLES AND TYPES
- Python is completely object oriented.
- You do not need to declare variables before using them, or declare their type. 
- Every variable in Python is an object.
'''

'''ASSIGNMENTS
can be done on more than one variable "simultaneously"'''
a, b = 3, 4
print(a, b)

'''BASIC OPERATORS
'''
#Arithmetic Operators
number = 1 + 2 * 3 / 4.0
print(number)

#Operators with Strings
helloworld = "hello" + " " + "world"
print(helloworld)
#multiplying stringS
lotsofhellos = "hello" * 10
print(lotsofhellos)

#Operators with Lists
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
# multiplication operator
print([1,2,3] * 3)


'''STRING FORMATING
Python uses C-style string formatting to create new, formatted strings. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".
'''

# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)
# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))
# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

'''Some basic argument specifiers:
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)
'''


'''Exercise
You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44'''

data = ("John", "Doe", 53.44)
format_string = "Hello"
print(format_string % data)

#Solution
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)
