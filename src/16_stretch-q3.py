# 3. Write a program to determine if a number, given on the command line, is prime.

# Define Prime Number: a natural number greater than 1 and it does not have any divisor other than 1 and itself

def is_prime(n):
    # n must be converted to an int - input from command line will be in the form of a string
    n = int(n)
    # removes edge case : if n is less than/equal to one, it must not be prime (has to be a natural number greater than 1):
    #   return False
    if n <= 1:
        return False
    # if n is evenly divisible by any number from 2 -> n itself, it must not be prime (can't have any divisor other than 1 and itself):
    #   return False 
    for i in range(2, n):
        if n % i == 0:
            return False  
    # otherwise n must be prime:
    #   return True                  
    return True

# get user input from command line
num = input("Enter a number pls: ")

# when is_prime function invoked, passing in user input stored in num variable as param
# if it returns True:
#   print num is prime
# else:
#    print num not prime

if is_prime(num) == True:
    print(f'{num} IS a prime number')
else:
    print(f'{num} is NOT a prime number')


# Q1. How can you optimize this program?
# Optimisations:    
# -> Program does not account for float nums passed in as input
# -> Assumes that user will not pass in a value that may not be converted to type int - eg what happens if user passes in "cheese"? 


# Q2. Implement [The Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes),
#     one of the oldest algorithms known (ca. 200 BC).

# As per Wikipedia, The sieve of Eratosthenes can be expressed in pseudocode, as follows:

# algorithm Sieve of Eratosthenes is
#     input: an integer n > 1.
#     output: all prime numbers from 2 through n.

#     let A be an array of Boolean values, indexed by integers 2 to n,
#     initially all set to true.
    
#     for i = 2, 3, 4, ..., not exceeding √n do
#         if A[i] is true
#             for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
#                 A[j] := false

#     return all i such that A[i] is true.

import math

def optimised_is_prime(n):
    # convert n to int
    n = int(n)
    # initialize list of boolean values, initially all set to true, indexed by ints 2 -> n
    lst = [True] * (n + 1)
    # for i = 2, 3, 4, ..., not exceeding √n do
    i = 2
    while i * i <= n:
        # if A[i] is true
        if lst[i] == True:
            # for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
            for j in range(i * 2, n + 1, i):
                # A[j] := false
                lst[j] = False
        i += 1      
    # return all i such that A[i] is true.
    for i in range(2, n):
        if lst[i]:
            print(lst[i])

optimised_is_prime(30)