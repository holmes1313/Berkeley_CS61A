# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 15:47:23 2019

@author: z.chen7
"""

class Account:
    interest = 0.02  # A class attribute
    
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0
        
    def deposite(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance
    
    
class CheckingAccount(Account):
    interest = 0.01
    withdraw_fee = 1
    def withdraw(self, amount):
        return super().withdraw(amount + self.withdraw_fee)
    
    
b = CheckingAccount('Jack')
b.balance
b.holder
b.withdraw_fee
b.deposite(100)
b.withdraw(10)

 
class Bank:
    def __init__(self):
        self.accounts = []
        
    def open_account(self, holder, amount, kind=Account):
        account = kind(holder)
        account.deposite(amount)
        self.accounts.append(account)
        return account
    
    def pay_interest(self):
        for a in self.accounts:
            a.deposite(a.balance * a.interest)
            
    def too_big_to_fail(self):
        return len(self.accounts) > 1


bank = Bank()
john = bank.open_account('John', 10)
type(john)
isinstance(john, Account)
john.interest
bank.accounts

jack = bank.open_account('Jack', 5, CheckingAccount)
isinstance(jack, CheckingAccount)
bank.accounts

bank.pay_interest()
jack.balance
john.balance



class A:
    z = -1
    def f(self, x):
        return B(x-1)
    
class B(A):
    n = 4
    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y+1)
            
class C(B):
    def f(self, x):
        return x
    

a = A()
b = B(1)
b.n = 5

C(2).n  # 4

a.z == C.z 

type(b.z.z.z)
 

"""
The constructor of a class if a function that creates an instance, or a single occurrence, of the object outlined by the class.
In Python, the constructor method is named __init__.
"""




# String representations
"""
In python, all objects produce two string representations:
    the str is legible to humans
    the repr is legible to the Python interpreter

The repr function returns a Python expression (a string)
that evaluates to an equal object.

The result of calling repr on a value is what Python
prints in an interactive seesion
"""
12e12
repr(12e12)
print(repr(12e12))

"""
Some objects do not have a simple Python-readable string"""
repr(min)


from fractions import Fraction
half = Fraction(1, 2)
half
repr(half)
str(half)

"""
The result of calling str on the value of an expression
is what Python prints using the print function:"""
print(half)




# Growth

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)


def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

fib = count(fib)

fib(5)
fib.call_count
fib(30) 
fib.call_count


# Memorization
"""
Idea: remember the results that have been computed before"""
def memo(f):
    cache = {}     # keys are arguments that map to the return values
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized


fib(30)
fib = count(fib)
counted_fib = fib
counted_fib.call_count
fib = memo(fib)
fib = count(fib)
fib(30)
fib.call_count
counted_fib.call_count


# Space
"""
Which environment frames do we need to keep during evaluation?

At any moment there's a set of active environments

Values and frames in active environments consume memory

Memory that is used for other values and frames can be recycled


Active environment:
    Environments for any function callc currently being evaluated
    
    Parent environments of functions named in active environments
"""

def count_frames(f):
    def counted(n):
        counted.open_count += 1
        if counted.open_count >= counted.max_count:
            counted.max_count = counted.open_count
        result = f(n)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted
        
fib = count_frames(fib)
fib(20)        
fib.open_count        
fib.max_count        

fib(5)        
fib.max_count        
        

# Time
"""
Implementations of the same functional abstraction can require different amounts of time

Problem: how many factors does a postive integer n have?
(A factor k of n is a postive integer that evenly divides n)

def factors(n):
    
    Slow: test each k from 1 through n
    
    Fast: test each k from 1 to square root n
          for every k, n/k is also a factor"""

def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

@count
def divides(k, n):
    return n % k == 0

def factors(n):
    total = 0
    for k in range(1, n+1):
        if divides(k, n):
            total += 1
    return total

factors(576)
divides.call_count

from math import sqrt

def factors_fast(n):
    total = 0
    sqrt_n = sqrt(n)
    k = 1
    while k < sqrt_n:
        if divides(k, n):
            total += 2
        k += 1
    if k*k == n:
        total += 1
    return total
    
factors_fast(576)
divides.call_count


# Orders of growth

# Exponentiation

# comparing orders of growth
