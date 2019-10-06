# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 19:59:02 2019

@author: z.chen7
"""

# Class: Exceptions

"""
Exceptions

A built-in mechnisum in programming language to declare and respond to exceptional
conditions

Python raises an exception whenever an error occurs

Exceptions can be handled by the program, preventing the interpreter from halting

Unhandled exceptions will cause Python to halt execution and print a stack trace

Mastering exceptions:
    Exceptions are objects! They have classes with constructors.
    
    They enable non-local continuations of control:
        If f calls g and g calls h, exceptions can shift control from h to f
        without waiting for g to return.
        
    Exception handling tends to be slow.
"""


"""
Assert statements

Assert statements raise an exception of type AssertionError

    assert <expression>, <string>
    
Assertions are designed to be used liberally. They can be ignored to increase
efficiency by running Python with "-0" flag. "0" stands for optimized.

    python3 -0
    
whether asssertions are enabled is governed by a bool __debug__"""

assert False, 'Error'
assert True


"""
Raise statements

Exceptions are raised with a raise statement

    raise <expression>
    
<expression> must evaluate to a subclass of BaseException or an instance of one.

Exceptions are constructed like any other object. e.g., TypeError('Bad argument!')

TypeError -- A function was passed the wrong number/type of argument
NameError -- A name wasn't found
KeyError -- A key wasn't found in a dictionary
RuntimeError -- Catch-all for troubles during interpretation
"""
raise TypeError("Bad argument")
abs("hello")
hello
{}['hello']



# try statement
"""
Try statements handle exceptions

    try:
        <try suite>
    except <exception class> as <name>:
        <except suite>
        
        
Execution rule

The <try suite> is executed first.

If, during the course of executing the <try suite>, and exception is raised that
is not handled otherwise, and 

If the class of the exception inherits from <exception class>, then
then <except suite> is executed, with <name> bound to the exception.
"""

"""
Handing exceptions

Exception handling can prevent a program from terminating
    
    try:
        x = 1/0
    except ZeroDivisionError as e:
        print('handling a', type(e))
        x = 0
        
    handling a <class 'ZeroDivisionError'>
    
    
Multiple try statements: control jumps to the except suite of the most recent
try statement that handles that type of exception.

""""
        

# Reducing a sequence to a value
def reduce(f, s, initial):
    """
    combine elements of s pairwise using f, starting with initial.
    e.g., reduce(mul, [2, 4, 8], 1) is equivalent to mul(mul(mul(1, 2), 4), 8).
    
    f is a two-argumnet function
    
    s is a sequence of values that can be the second argument
    
    initial is a vlaue that can be the first argument
    """
    
    for x in s:
        initial = f(initial, x)
    return initial


def reduce2(f, s, initial):
    if not s:
        return initial
    else:
        first, rest = s[0], s[1:]
        return reduce(f, rest, f(initial, first))


from operator import truediv
    
def divide_all(n, ds):
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')

divide_all(1024, [2, 4, 0, 8])





# Calculator
"""
Reading scheme lists

the task of parsing a language involves coercing a string representation
of an expression to the expression itself.

Parsers must validate that expressions are well-formed.

"""

"""
Parsing

A parser takes text and returns an expression

Text -Lexical analysis-> Tokens -Syntactic analysis-> Expression

Syntactic analysis identifies the hierarchical structure of an expression, which
may be nested.

"""


"""
Syntax is about the structure or the grammar of the language. 
It answers the question: how do I construct a valid sentence?

Semantics is about the meaning of the sentence. 
It answers the questions: is this sentence valid? If so, what does the sentence mean? 

Calculator syntax
The calculator language has primitive expressions and call expressions.

A primitive expression is a number: 2, -4, 5.6

A call expression is a combination that begins with an operator (+, -, *, /)
followed by 0 or more expressions: (+ 1 2 3), (/ 3 (+ 4 5))

Expressions are represented as Scheme lists (Pair instances) that encode tree
structure.


Calculator Semantics
The value of a calculator expression is defined recursively

Primitive: A numer evaluates to itself

Call: a call expression evaluates to its argument values combined by an operator.
"""









