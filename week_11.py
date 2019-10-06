# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:41:32 2019

@author: z.chen7
"""

# Dynamic Scope
"""
The way in which names are looked up in Scheme and Python is called lexical scope
(or static scope)

Lexical scope: the parent of a frame is the environment in which a procedure
was defined.

Dynamic scope: the parent of a frame is the environment in which a procedure
was called.
"""



#Recursion and Iteration in Python
"""
In Python, recursion calls always create new active frames.

factorial(n, k) computes k * n!

def factorial(n, k):
    if n == 0:
        return k
    else:
        return factorial(n-1, k*n)
        
def factorial(n, k):
    while n > 0:
        n, k = n-1, k*n
    return k
"""


# Declarative programming
"""
In declarative languages such as SQL & Prolog:
    A program is a description of the desired result
    The interpreter figures out how to generate the result
    
In imperative languages such as Python & Scheme:
    A program is a description of computational processes
    The interpreter carries out execution/evaluation rules
"""
