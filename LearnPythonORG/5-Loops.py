'''FOR '''
#For in... en listas, sets, etc.
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

'''Range function'''
# Prints out the numbers 0,1,2,3,4. (i=0 hasta n-1)
for x in range(5):
    print(x)

# Prints out 3,4,5 (i=3 hasta n-1)
for x in range(3, 6):
    print(x)

# Prints out 3,5,7. (i=3, hasta n-1, con paso=2)
for x in range(3, 8, 2):
    print(x)


'''WHILE '''
# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

'''"break" and "continue" statements'''
# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even(par)
    if x % 2 == 0:
        continue
    print(x)

'''Else'''
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

'''Exercise
Loop through and print out all even numbers from the numbers list in the same order they are received. Don't print any numbers that come after 237 in the sequence. '''

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]
#Mi solucion
for number in numbers:                      
    if (number % 2 == 1) or (number > 237):
        continue
    print(number)

#Resolucion Curso(La consigna era no imprimir nada mas luego de q aparezca un '237')
for number in numbers:
    if number == 237:
        break

    if number % 2 == 1:
        continue

    print(number)



