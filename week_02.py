# -*- coding: utf-8 -*-
"""
Created on Sun May 19 19:22:19 2019

@author: z.chen7
"""

# print and None
-2
print(-2)

'Go Bears!'
print('Go Bears!')

None
print(None)

print(1, 2, 3)
print(None, None)
#IMPORTANT#
print(print(1), print(2))

"""
The special value None represents nothing in Python

A function that does not explicitly return a value will return None.

Careful: None is not displayed by the interpreter as the value of an expression"""

def does_not_square(x):
    x * x

sixteen = does_not_square(4)
sixteen is None

"""
Non-pure functions, which have side effects.

func print() has output/return value None and displays whatever is passed into it.
"""
print(-2) is None  # True



# true dividend
2013 / 10
# integer dividend
2013 // 10
# reminder dividend
2013 % 10

from operator import truediv, floordiv, mod
truediv(2013, 10)
floordiv(2013, 10)
mod(2013, 10)


"""
Boolean contexts

False values in Python: False, 0, '', None
True values in Python: anything else
"""



"""
return and print
The return statement will give the result of some computation back to the caller
of the function and exit the function.

The print function is used to display values in the Terminal.

Unlike a return statement, when Python evaluates a print expression, the function
does not terminate immediately.

Notice that print will display text without the quotes, but return will preserve
the quotes."""

def what_prints():
    print('Hello world1')
    return 'Exiting this function.'
    print('61A is awesome!')

what_prints()



"""
Boolean operators
boolean operators, like arithmetic operators, have an order of operation:
    not has the highest priority
    and
    or has the lowest priority
"""


not None

True and 1/0



"""
Q4: Sum Digits
Write a function that takes in a nonnegative integer and sums its digits. 
(Using floor division and modulo might be helpful here!)"""
def sum_digits(n):    
    digit_list = list(str(n))    
    digit_sum = sum([int(digit) for digit in digit_list])
    return digit_sum

sum_digits(10)
sum_digits(4224)
sum_digits(1234567890)


"""
Q6: Falling Factorial
Let's write a function falling, which is a "falling" factorial that takes two arguments, 
n and k, and returns the product of k consecutive numbers, starting from n and working downwards."""
from functools import reduce
def falling(n, k):
    if k==0:
        return 1
    else:
        my_list = list(range(n, n-k, -1))
        return reduce((lambda x, y: x * y), my_list)

falling(6, 3)
falling(4, 0)
falling(4, 3)
falling(4, 1)



"""
Q7: Double Eights
Write a function that takes in a number and determines if the digits contain two adjacent 8s."""
def double_eights(n):
    return '88' in str(n)

double_eights(88)



"""
The purpose of higher-order functions

Functions are first class: functions can be manipulated as values in our
programming language.

Higer-order function: a function that takes a function as an argument or returns
a function as a return value

Higher-order functions:
    express general methods of computation
    remove repetition from programs
    separate concerns amoung functions
    
"""


square = lambda x: x * x
"""
Lambda expressions
    a function
        with formal parameter x
            that returns the value of "x*x"

Lambda expressions in python cannot contain statements at all!

Only the def statement gives the function an intrinsic name.
"""
square(4)
square    # <function __main__.<lambda>>, no intrinsic name



"""
Environment diagrams for nested def statements
    Every user-defined function has a parent frame (often global)
    The parent of a function if the frame in which it was defined
    Every local frame has a parent frame (often global)
    The parent of a frame is the parent of the function called

"""


# local variable
def f(x, y):
    return g(x)

def g(a):
    return a + y

f(1, 2)  # NameError: name 'y' is not defined
# the above is different from the nested function below
def m(x):
    def n(y):
        return x + y
    return n

m(1)(2)


# Function composition
def make_adder(n):
    def adder(k):
        return k + n
    return adder

def square(x):
    return x * x

def triple(x):
    return 3 * x

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h


compose1(square, triple)(5)
compose1(triple, square)(5)
compose1(square, make_adder(2))(3)



# Guerrilla 01: Variables & Functions, Control, Environment Diagrams
# WWPD (What would Python Display) after evaluating each of the following expressions?
0 and 1/0    # 0
1 and 1/0    # ZeroDivisionError: division by zero

6 or 1 or 'a' or 1/6
6 and 1 and 'a' and 1/0
6 and 1 and False and 1/0

print(print(4) and 2)

not True and print("a")
True and print("a")
if True and print("a"):
    print("b")








