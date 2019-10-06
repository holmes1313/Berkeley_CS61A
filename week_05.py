# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 20:38:25 2019

@author: z.chen7
"""

# Containers
[[1, 2]] in [3, [[1, 2]], 4]


# Sequence unpacking in for statement
pairs = [[1, 2], [2, 2], [3, 2], [4, 4]]
same_count = 0

for x, y in pairs:
    if x == y:
        same_count += 1
print(same_count)    


# ranges
"""
Ranges are another sequence type, meaning that they're sequences but they're
not lists.

A range is a sequence of consecutive integers.
It's including the starting value but excluding the ending value.

Length: ending value - starting value"""
for _ in range(3):
    print('Go Bears!')


# list comprehension
def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

divisors(18)



# Dictionaries
numerals = {'I': 1, 'V': 5, 'X': 10}

numerals.keys()
numerals.values()
numerals.items()

items = [('I', 1), ('V', 5), ('X', 10)]
dict(items)


{x: x * x for x in range(10)}

"""
Dictionaries are unordered collection of key-value pairs

Dictionary keys have two restrictions:
    1. A key of a dictionary cannot be a list or a dictionary (or any mutable type)
    2. Two keys cannot be equal; There can be at most one value for a give key
"""


"""
Data abstraction
Data abstraction is a powerful concept in computer science that allows
programmers to treate code as objects. That way, programmers don't have to
worry about how code is implemented -- they just have to know what it does.

An abstract data type consists of two types of functions:
    Constructors: functions that build the abstract data type.
    Selectors: functions that retrieve information from the data type
"""


def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    flatten_list = []
    
    if not lst:
        return flatten_list

    for i in lst:
        if type(i) != list:
            flatten_list.append(i)
        else:
            flatten_list.extend(flatten(i))
    return flatten_list 

flatten([1, [2, 3], 4])       
flatten([[1, [1, 1]], 1, [1, 1]])



def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    lst1.extend(lst2)
    lst1.sort(reverse=True)
    return lst1




# 2.2 Data abstraction
"""
The general technique of isolating the parts of a program that deal with how data 
are represented from the parts that deal with how data are manipulated is a powerful
design methodology called data abstraction.
"""

# 2.2.1 example: rational numbers
"""
<numerator> / <denominator>
, where numerator and denominator are placeholders for integer values.

Let us further assume that the constructor and selectors are available as
following three functions:
    rational(n, d) returns the rational number with numerator n and denominator d.
    numer(x) returns the numerator of the rational number x
    denom(x) returns the denominator of the rational number x.

"""
from fractions import gcd
def rational(n, d):
    g = gcd(n, d)
    return [n // g, d // g]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

def add_rationals(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rationals(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def print_rational(x):
    print(numer(x), '/', denom(x))
    
def rationals_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

half = rational(1, 2)
print_rational(half) 
third = rational(1, 3)
print_rational(mul_rationals(half, third))
print_rational(add_rationals(half, third))
print_rational(add_rationals(third, third))




# 2.3.6 Trees
"""
In general, a method for combining data values has a closure property 
if the result of combination can itself be combined using the same method.
Closure is the key to power in any means of combination because it permits
us to create hierarchical structures - structure made of parts, which themselves
are made up of parts, and so on.

The tree is a fundamental data abstraction that imposes regularity on how
hierarchical values are structured and manipulated.

A tree has a root label and a sequence of branches. 
Each branch of a tree is a tree. A tree with no branches is called a leaf. 
Any tree contained within a tree is called a sub-tree of that tree 
(such as a branch of a branch). The root of each sub-tree of a tree is 
called a node in that tree.

The data abstraction for a tree consists of the constructor tree and the 
selectors label and branches.

A tree is well-formed only if it has a root label and all branches are also trees.
"""
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)


t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
t
label(t)
branches(t)
label(branches(t)[1])
is_leaf(t)
is_leaf(branches(t)[0])


"""
Tree-recursive function can be used to construct trees.
For example, the nth Fibonacci tree has a root label of the nth Fibonacci number
and, for n > 1, two branches that are also Fibonacci trees. A Fibonacci tree
illustrates the recursive computation of a Fibonacci number"""
def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])

fib_tree(5)


def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)

count_leaves(fib_tree(5))


"""
Trees can also be used to represent the partitions of an integer. 
A partition tree for n using parts up to size m is a binary (two branches) tree
that represents the choices taken during computation. In a non-leaf partition
tree:
    1.the left (index 0) branch contains all ways of partitioning n using at least one m
    2.the right (index 1) branch contains partitions using parts up to m-1
    3. the root label is m

The labels at the leaves of a partition tree express whether the path from 
the root of the tree to the leaf represents a successfl partition of n."""
def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m."""
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])
    
partition_tree(2, 2)

"""
Printing the partitions from a partition tree is another tree-recursive process
that traverses the tree, constructing each partition as a list. Whether a True
leaf is reached, the partition is printed.
"""
def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)

print_parts(partition_tree(6, 4))

"""
Slicing can be used on the branches of a tree as well. For example, we may want
to place a restriction on the number of branches in a tree. A binarized tree
has at most two branches. A common tree transformation called binarization finds
a binarized tree with the same labels as original tree by grouping together branches."""
def right_binarize(t):
    """construct a right-branching binary tree."""
    return tree(label(t), binarize_branches(branches(t)))

def binarize_branches(bs):
    """Binarize a list of branches"""
    if len(bs) > 2:
        first, rest = bs[0], bs[1:]
        return [right_binarize(first), binarize_branches(rest)]
    else:
        return [right_binarize(b) for b in bs]
    
right_binarize(tree(0, [tree(x) for x in [1, 2, 3, 5, 6, 7, 8]]))



# 2.3.7  Linked lists
"""
A common representation of a sequence constructed from nested pairs is called
a linked list. 

four = [1, [2, [3, [4, 'empty']]]]

A linked list is a pair containing the first element of the sequence (in this case 1)
and the rest of the sequence (in this case a representation of 2, 3, 4). The 
second element is also a linked list. The rest of the inner-most linked list
containing only 4 is 'empty', a value that represents an empty linked list.

Linked lists have recursive structure: the rest of a linked list is a linked
list or 'empty'. We can define an abstract data representation to validate,
construct, and select the components of linked lists.
"""
four = [1, [2, [3, [4, 'empty']]]]

empty = 'empty'

def is_link(s):
    """s is a linked list if it is empty or  a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))


def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]


def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element"
    return s[0]


def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), "rest only applies to linked lists"
    assert s != empty, "empty linked list has no rest."
    return s[1]

"""
Above, link is a constuctor and first and rest and selectors for an abstract
data representation of linked lists. 
The behavior condition for a linked list is that, like a pair, its constructor
and selector are inverse functions.
    If a linked list s was constructed from first element f and linked list r,
    then first(s) returns f, and rest(s) returns r.    
"""
four = link(1, link(2, link(3, link(4, empty))))
first(four)
rest(four)


"""
The linked list can store a sequence of values in order, but we have not yet
shown that it satisfied the sequence abstraction. Using the abstraction data
representation we have defined, we can implement the two behaviors that 
characterize a sequence: length and element selection."""

def len_link(s):
    """Return the length of linked list s."""
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length


def getitem_link(s, i):
    """Return the element at index i of linked list s."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)


len_link(four)
getitem_link(four, 2)


# Recursive manipulation
# We can also implement length and element selection using recursion.
def len_link_recursive(s):
    """Return the length of a linked list s."""
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))


def getitem_link_recursive(s, i):
    """Return the element at index i of linked list s."""
    if i == 0:
        return first(s)
    else:
        return getitem_link(rest(s), i - 1)


# Recursion is also useful for transforming and combinaing linked lists
def extend_link(s, t):
    """Return a list with the elements of s followed by those of t."""
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))

extend_link(four, four)


def apply_to_all_link(f, s):
    """Apply f to each element of s."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))

apply_to_all_link(lambda x: x*x, four)


def keep_if_link(f, s):
    """Return a list with elements of s for which f(e) is true."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        kept = keep_if_link(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept

keep_if_link(lambda x: x%2 == 0, four)


def join_link(s, separator):
    """Return a string of all elements in s separated by separator."""
    assert is_link(s)
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)

join_link(four, ", ")



"""
Recursive construction
Linked lists are particularly useful when constructing sequences incrementally,
a situation that arises often in recursive computation.


The count_partitions function from Chapter 1 counted the number of ways to 
partition an integer n using parts up to size m via a tree-recursive process. 
With sequences, we can also enumerate these partitions explicitly using a similar process.

We follow the same recursive analysis of the problem as we did while counting: 
    partitioning n using integers up to m involves either
        partitioning n-m using integers up to m, or 
        partitioning n using integers up to m-1.

For base cases, we find that 0 has an empty partition, while partitioning 
a negative integer or using parts smaller than 1 is impossible.
"""

def partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked list.
    """
    if n == 0:
        return link(empty, empty)  # A list containing the empty partition
    elif n < 0 or m == 0:
        return empty
    else:
        using_m = partitions(n-m, m)
        with_m = apply_to_all_link(lambda s: link(m, s), using_m)
        without_m = partitions(n, m-1)
        return extend_link(with_m, without_m)

"""
In the recursive case, we construct two sublists of partitions. 
The first uses m, and so we prepend m to each element of the result using_m to form with_m.

The result of partitions is highly nested: a linked list of linked lists, 
and each linked list is represented as nested pairs that are list values. 
Using join_link with appropriate separators, we can display the partitions in a human-readable manner.
"""

def print_partitions(n, m):
    lists = partitions(n, m)
    strings = apply_to_all_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))

partitions(6, 4)
print_partitions(6, 4)



sum([2, 3, 4])
sum(['2', '3', '4'])
sum([2, 3, 4], 5)

[2, 3, 4] + [5]

sum([[2, 3], [4]], [])
[2, 3] + 0
[] + [2, 3] + [4]


"""
Trees are an important data abstraction for representing hierarchical 
relationships"""
# trees

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


tree(1)
is_leaf(tree(1))
tree(1, [5])
t = tree(1, [tree(5, [tree(7)]), tree(6)])
t
label(t)
branches(t)
branches(t)[0]
is_tree(branches(t)[0])
label(branches(t)[0])


def fib_tree(n):
    if n <= 1:
        return tree(n)
    else: 
        left, right= fib_tree(n-2), fib_tree(n-1)
        return tree(label(left) + label(right), [left, right])

fib_tree(1)
fib_tree(0)
fib_tree(2)
fib_tree(4)
label(fib_tree(4))


def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])

fib_tree(10)
count_leaves(fib_tree(10))


# If you sum a list of lists, you get a list containing the elements of those lists.
sum([[1], [2, 3], [4]], [])
sum([[1]], [])
sum([[[1]], [2]], [])

def leaves(tree):
    """Returning a list containing the leaf labels of tree.
    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return [label(tree)]
    else: 
        return sum([leaves(b) for b in branches(tree)], [])

leaves(fib_tree(5))    


"""
A function that creates a tree from another tree is typically also recursive."""
def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented."""
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)
        
    
fib_tree(5)
increment_leaves(fib_tree(5))


def increment(t):
    """ Return a tree like t but with all labels incremented."""
    return tree(label(t) + 1, [increment(b) for b in branches(t)])
    
fib_tree(5)
increment(fib_tree(5))    
    
    
def print_tree(t, indent=0):
    print('  ' * indent, str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)
    
print_tree(fib_tree(5))
increment(fib_tree(5))    





# Objects
"""
Objects represent information
They consist of data and behavior, bundled together to create abstractions
Objects can represent things but also properties, interactions, and processes
A type of object is called a class; classes are first-class value in Python
Object-oriented programming:
    A metophor for organizing large programs
    Special syntax that can improve the composition of programs
In Python, every value is an object:
    All objects have attributes
    A lot of data manipulation happens through object methods
    Functions do one thing; objects do many related things.
    
"""



# String
"""
Strings are an abstraction that allows us to represent texts.

The ASCII standard is English specific but the Unicode standard is designed
in order to have one character set that would be used for all different languages.

The process of encoding converts information from a source into symbols for 
communication or storage. 

Decoding is the reverse process, converting code symbols back into a form 
that the recipient understands, such as English or Spanish.


"""

a = 'A'
ord(a)
hex(ord(a))

print('\a')

from unicodedata import name, lookup
name('A')
name('a')    
lookup('LATIN SMALL LETTER A')    
lookup('WHITE SMILING FACE')    
lookup('SNOWMAN')     
lookup('SOCCER BALL')     
lookup('BABY')     

lookup('BABY').encode()     



# mutation operation
"""
The same object can change in value throughout the course of computation.

All names that refer to the same object are affected by a mutation.

Only objects of mutable types can change so far: lists & dictionary
"""
suits = ['coin', 'string', 'myriad']
original_suits = suits
suits.pop()
suits.remove('string')
suits
suits.append('cup')
suits.extend(['sword', 'club'])
suits
suits[2] = 'spade'
suits[0: 2] = ['heart', 'diamond']
suits
original_suits


numerals = {'I': 1, 'V': 5, 'X': 10}
numerals
numerals['X']
numerals['X'] = 11
numerals['X']
numerals
numerals['L'] = 50
numerals
numerals['L']
numerals.pop('X')
numerals.get('X')
numerals


'''
Mutation can happen within a function call

A function can change the value of any object in its scope.'''

def mystery(s):
    s.pop()
    s.pop()
    
# or

def mystery_2(s):
    s[-2:] = []

four = [1, 2, 3, 4]
len(four)

mystery(four)
len(four)
mystery_2(four)
len(four)

def another_mystery():
    three.pop()
    three.pop()
    
three = [1, 2, 3]

another_mystery()
len(three)



# Tuples
"""
Tuples are immutable sequences

Immutable values are protected from mutation
"""
(3, 4, 5, 6)
3, 4, 5, 6
()
tuple()
tuple([1, 2, 3, 4])
2, 
(2,)
(2)
(3, 4) + (5, 6)
5 in (3, 4, 5)

{(1, 2): 3}
{[2, 3]: 3}
{([1], 2): 3}

"""
The value of an expression can change because of changes in names or objects:    
"""
# Name change
x = 2
x + x
x = 3
x + 3

# object mutation
x = [1, 2]
x + x 
x.append(3)
x + x

"""
An immutable sequence may still change if it contains"""
s = ([1, 2], 3)
s[0] = 4

s[0][0] = 4
s


# Sameness and change
"""
As long as we never modify objects, a compound object is just the totality of its pieces

A rational number is just its numerator and denominator

This view is no longer valid in the presence of change

A compound data object has an 'identity' in addition to the pieces of which it is composed.

A list is still 'the same' list even if we change its contents.

Conversely, we could have two lists that happend to have the same contents, but are different.
"""
a = [10]
b = a
a == b
a is b
a.append(20)
a
b
a == b
a is b

a = [10]
b = [10]
a == b
a is b
a.append(10)
a
b

"""
Identity Operators

<exp0> is <exp1>
evaluates to True if both <exp0> and <exp1> evaluate to the same object

<exp0> == <exp1>
evaluates to True if <exp0> and <exp1> evaluate to equal values.

Identical objects are always equal values.
"""

"""
Mutable default arguments are dangerous.

A default argument value is part of a function value, not generated by a call."""

def f(s=[]):
    s.append(5)
    return len(s)

f()
f()
f()






