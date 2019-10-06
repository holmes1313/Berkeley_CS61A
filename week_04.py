# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:39:49 2019

@author: z.chen7
"""

# The Cascade function
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)
        
cascade(123)    

"""
1. each cascade is from a different call to cascade.
2. until the return value apprears, that call has not completed.
3. any statement can appear before or after the recursive call.
"""

# two definitions of cascade
def cascade_2(n):
    print(n)
    if n >= 10:
        cascade_2(n // 10)
        print(n)

cascade_2(123)

"""    
If two implements are equally clear, then shorter is usually better.
In this case, the longer implementation is more clear.
When learning to write recursive functions, put the base cases first.
Both are recursive functions, even though only the first has typical structure.
"""
    

# Inverse cascade
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)
    
def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)
    
inverse_cascade(1234) 
    


# Tree Recursion
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib(35)



# Counting partitions
def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 1
    else:
        with_m = count_partitions(n - m, m)
        without_m = count_partitions(n, m - 1)
        return with_m + without_m



# Rational numbers
from fractions import gcd   # Gretest common divisor
gcd(25, 50)











    
    
    