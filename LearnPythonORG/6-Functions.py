#Functions in python are defined using the block keyword "def", followed with the function's name as the block's name
def my_function():
    print("Hello From My Function!")

my_function() #invoco la funcion/ tambien con print(myf..())


#arguments (variables passed from the caller to the function)
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

my_function_with_args('santi', 'ok')

#return - return a value to the caller
def sum_two_numbers(a, b):
    return a + b
    
print(sum_two_numbers(1, 5)) #6
#Invoco la fn en una variable
x = sum_two_numbers(1,2) 
print(x) #3


'''Exercise
In this exercise you'll use an existing function, and while adding your own to create a fully functional program.

Add a function named list_benefits() that returns the following list of strings: "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

Add a function named build_sentence(info) which receives a single argument containing a string and returns a sentence starting with the given string and ending with the string " is a benefit of functions!"

Run and see all the functions work together!'''

# Modify this function to return a list of strings as defined above
def list_benefits():
    return []

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return ""

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()  #guarda la lista en esta variable
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

#solution
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


