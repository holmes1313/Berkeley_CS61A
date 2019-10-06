# -*- coding: utf-8 -*-
"""
Created on Sat May 25 19:17:32 2019

@author: z.chen7
"""


# Iteration

# Return Statement
def end(n, d):
    """Print the final digiests of n in reverse order until d is found
    
    >>> end(34567, 5)
    7
    6
    5
    """
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if d == last:
            break
            # return None
        
end(34567, 5)

34567 % 10
34567 // 10


def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1

def search2(f):
    x = 0
    while not f(x):
        x += 1
    return x

        
def is_three(x):
    return x == 3

search(is_three)
search2(is_three)

def square(x):
    return x * x

def positive(x):
    return max(0, square(x) - 100)

search(positive)
search2(positive)


def inverse(f):
    """Return g(y) such that g(f(x)) = x."""
    return lambda y: search(lambda x: f(x) == y)

inverse(square)(16)
"""
f = square
y = 16
"""



# self reference
def print_all(x):
    print(x)
    return print_all

print_all(1)(3)(5)


def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n+k)
    return next_sum

print_sums(1)   # print_sums
print_sums(1)(3)    # next_sums(3) or print_sums(4)
print_sums(1)(3)(5)   # next_sums(5) or print_sums(9)



# Lab 2: Higher Order Functions

# Lambda Expressions
# Lambda expressions can be used as an operator or operand
negate = lambda f, x: -f(x)
negate(lambda x: x * x, 3)


(lambda: 3)()


b = lambda x: lambda: x
c = b(88)
c
c()
c(1)


z = 3
e = lambda x: lambda y: lambda: x + y + z
e(0)
e(0)(1)
e(0)(1)()


def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie

chocolate = cake()
chocolate
chocolate()




# Recursive Functions
"""
Defination: a function is called recursive if the body of that function calls itself,
either directly or indirectly.
That is, the process of executing the body of a recursive function may in turn
require applying that function again.
"""
def sum_digits(n):
    """Returning the sum of the digits of positive integer n."""
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last


# The anatomy of a recursive function
"""
The body begins with a base case, a conditional statement that defines the behavior
of the function for the inputs that are simplest to process.

The base cases are then followed by one or more recursive calls. Recursive calls
always have a certain character: they simplify the original problem. Recursive
functions express computation by simplyfying problems incrementally.
"""
def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total
        
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

"""
Treating a recursive call as a functional abstraction has been called a recursive leap
of faith. We define a function in terms of itself, but simply trust that
the simpler cases will work correctly when verifying the correctness of the function."""


# Mutial recursion
"""
When a recursive procedure is divided among two functions that call each other,
the functions are said to be mutually recursive.

a number is even if it is one more than an odd number
a number is odd if it is one more than an even number
0 is even
"""
def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)

def is_odd(n):
    if n == 0:
        return False
    else: 
        return is_even(n-1)


result = is_even(4)

"""
Mutually recursive functions can be turned into a single recursive function
by breaking the abstraction boundary between the two functions."""
def is_even(n):
    if n == 0:
        return True
    else:
        if n-1 == 0:
            return False
        else:
            return is_even((n-1)-1)
        
        
# Printing in recursive functions
"""
The computational process evolved by a recursive function can be often visualized
using calls to print.
As an example, we will implement a function cascade that prints all prefixes of a
number from largest to smallest to largest.
"""
def cascade(n):
    """Print a cascade of prefix of n."""
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)
    
cascade(2013)

"""
It is not a rigid requirement that base cases be expressed before recursive calls.
In fact, this function can be expressed more compactly by obeserving that print(n)
if repeated in both clauses of conditional statement, and therefore can precede it.
"""
def cascade(n):
    """Print a cascade of prefixes of n."""
    print(n)
    if n >= 10:
        cascade(n // 10)
        print(n)
    
    
"""
As another example of mutual recursion, consider a two-player game in which 
there are n initial pebbles on a table. The players take turns, removing 
either one or two pebbles from the table, and the player who removes the final 
pebble wins. Suppose that Alice and Bob play this game, each using a simple strategy:

Alice always removes a single pebble
Bob removes two pebbles if an even number of pebbles is on the table, and one otherwise
Given n initial pebbles and Alice starting, who wins the game?

A natural decomposition of this problem is to encapsulate each strategy in its own
function. This allows us to modify one strategy without affecting the other,
maintaining the abstraction barrier between the two. In order to incorporate
the turn-by-turn nature of the game, these two functions call each other at the
end of each turn.
"""
def play_alice(n):
    if n == 0:
        print("Bob wins!")
    else:
        play_bob(n-1)

def play_bob(n):
    if n == 0:
        print('Alice wins!')
    elif is_even(n):
        play_alice(n-2)
    else:
        play_alice(n-1)
        
        
play_alice(6)
play_bob(6)



# Tree recursion
"""
Another common pattern of computation is called tree recursion, in which a function
calls itself more than once.

A function with multiple recursive calls is said to be tree recursive because 
each call branches into multiple smaller calles, each of which branches into 
yet smaller calls, just as the branches of a tree become smaller but more numerous
as they extend form the trunk.
"""
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

result = fib(6)
result


# Example: partition
"""
The number of partitions of a positive integer n, using parts up to size m, is 
the number of ways in which n can be expressed as the sum of positive integer
parts up to m in increasing order.

We will define a function count_partitions(n, m) that returns the number of 
different partitions of n using parts up to m. This function has a simple 
solution as a tree-recursive function, based on the following observation:

The number of ways to partition n using integers up to m equals
    1. the number of ways to partition n-m using integers up to m, and
    2. the number of ways to partition n using integers up to m-1
    
To complete the implementation, we need to speficy the following base cases:
    1. there's one way to partition 0: include no parts.
    2. there are 0 ways to partition a negative n.
    3. there are 0 ways to partition any n greater than 0 using parts of size or less
"""
def count_partitions(n, m):
    """Count the ways to partition n using parts up to m."""
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else: 
        return count_partitions(n-m, m) + count_partitions(n, m-1) 
    
    
    
"""
There are three common steps in a recursive definition:
1. Figure out your base case: The base case is usually the simplest
input possible to the function. For example, factorial(0) is 1 by
definition. You can also think of a base case as a stopping condition
for the recursion. If you can’t figure this out right away, move on to
the recursive case and try to figure out the point at which we can’t
reduce the problem any further.

2. Make a recursive call with a simpler argument: Simplify your
problem, and assume that a recursive call for this new problem will
simply work. This is called the “leap of faith”. For factorial, we
reduce the problem by calling factorial(n-1).

3. Use your recursive call to solve the full problem: Remember
that we are assuming the recursive call works. With the result of the
recursive call, how can you solve the original problem you were asked?
For factorial, we just multiply (n − 1)! by n.

"""


"""
2.1 Write a function that takes two numbers m and n and returns their product.
Assume m and n are positive integers. Use recursion, not mul or *!
Hint: 5*3 = 5 + 5*2 = 5 + 5 + 5*1.
For the base case, what is the simplest possible input for multiply?
For the recursive case, what does calling multiply(m - 1, n) do? What
does calling multiply(m, n - 1) do? Do we prefer one over the other?"""

def multiply(m, n):
    """
    >>>multiply(5, 3)
    15
    """
    if n == 1:
        return m
    else:
        return m + multiply(m, n-1)

multiply(5, 3)


"""
2.2 Write a recursive function that takes in an integer n and prints out a countdown from n to 1.
First, think about a base case for the countdown function. What is the
simplest input the problem could be given?
After you’ve thought of a base case, think about a recursive call with a
smaller argument that approches the base case. What happens if you call
countdown(n - 1)?
Then, put the base case and the recursive call together, and think about
where a print statement would be needed.
"""
def countdown(n):
    """
    >>> countdown(3)
    3
    2
    1
    """
    if n == 1:
        print(n)
    else:
        print(n)
        return countdown(n-1)
        
countdown(3)


"""
2.4 Write a recursive function that takes a number n and returns the sum of every
other digit, starting from the rightmost digit. Assume n is non-negative.
You might find the operators // and % useful."""
def sum_every_other_digit(n):
    """
    >>>sum_every_other_digit(7)
    7
    >>>sum_every_other_digit(30)
    0
    >>>sum_every_other_digit(228)
    10
    >>>sum_every_other_digit(123456)
    12
    >>>sum_every_other_digit(1234567)
    16
    """
    if n < 10:
        return n
    else:
        return (n % 10) + sum_every_other_digit(n // 100)

sum_every_other_digit(1234567)




# Choosing Names
"""
Names should convey the meaning or purpose of the values to which they are bound.
The type of value bound to the name is best documented in a function's docstring.
Function names typically convey their effect (print), their behavior (triple), or
the value returned (abs).
"""


# Function curring
"""
Curring: Transforming a multi-argument function into a single-argument, 
higher-order function."""
from operator import add
add(2, 3)

def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g
curry2(add)(2)(3)

curry2_2 = lambda f: lambda x: lambda y: f(x, y)
curry2_2(add)(2)(3)



"""
Function Decorator

@trace1
def triple(x):
    return 3 * x
    
is identical to

def triple(x):
    return 3 * x
triple = trace1(triple)
"""
def traced1(fn):
    """Returns a version of fn that first prints before it is called.
    
    fn - a function of 1 argument"""
    def traced(x):    # traced is just like fn except for it also prints
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced


@traced1
def square(x):
    return x * x

square(12)


@traced1
def sum_square_up_to(n):
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k), k + 1
    return total

sum_square_up_to(5)



# What would python print
"""
The print function returns None. It also displays its arguments (separated by spaces)
when it is called.
"""

# expression
print(5)
# evaluate to
None
# Interactive output
5

# expression
print(print(5))
# evaluate to
None
# interactive output
5
None  # print(None)


def delay(arg):
    """ A function that takes any argument and returns a function that
    returns the arguments"""
    print('delayed')
    def g():
        return arg
    return g

# expression
delay(delay)()(6)()
# evaluate to 
6
# interactive output
'delayed'
'delayed'
6

# expression
print(delay(print)()(4))
# evalute to
None
# interactive output
'deplayed'
4
None


def pirate(arggg):
    """ A function that always returns the identity function."""
    print('matey')
    def plunder(arggg):
        return arggg
    return plunder

"""
A name evaluates to the value bound to that name in the earliest frame of the
current environment in which that name is found"""

# expression
pirate(3)(square)(4)
# evaluate to
16
# interactive output 
'matey'

# expression
pirate(pirate(pirate))(5)
# evaluate to
5
# interactive output
'matey'
'matey'


# horse function
def horse(mask):
    horse = mask
    def mask(horse):
        return horse
    return horse(mask)

mask = lambda horse: horse(2)

horse(mask)




