# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.
def sum_to(n):
    sum = 0 
    for value in range(1, n+1):
        sum += value
    print(sum)

sum_to(50)

#2 Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.
def largest(num):
    return max(num)

print(largest([10, 9, 8, 7, 62, 5, 4, 3, 2, 1]))

#3 Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.
def occurrences(str1, str2):
    return str1.count(str2)

print(occurrences('fleep floop', 'e'))   # returns 2

#*4 Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.
    #The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.
    #What *args allows you to do is take in more arguments than the number of formal arguments that you previously defined. 
    #With *args, any number of extra arguments can be tacked on to your current formal parameters 
    #We use *args and **kwargs as an argument when we are unsure about the number of arguments to pass in the functions.
def product(*args):
    num = 1
    for x in args:
        num *= x
    return num

print(product(-1, 4)) # returns -4
print(product(2, 5, 5)) # returns 50
print(product(4, 0.5, 5)) # returns 10.0