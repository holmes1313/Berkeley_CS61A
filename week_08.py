# -*- codinzg: utf-8 -*-
"""
Created on Mon Jul 15 14:05:22 2019

@author: z.chen7
"""

# Linked list 
"""
A linked list is either empty or a first value and the rest of the linked list

Link(3, Link(4, Link(5, Link.empty)))

A lisked list is a pair

The first (zeroth) element is an attribute value.

The rest of the elements are stored in a linked list.

A class attribute represents an empty linked list
"""

class Link:
    empty = ()  # some zero-length sequence
    
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    
    @property
    def second(self):
        return self.rest.first
    
    @second.setter
    def second(self, value):
        self.rest.first = value
    
        
Link(5).rest

s = Link(3, Link(4, Link(5)))
s.first
s.rest.first
s.rest.rest.first
s.rest.rest.rest is Link.empty

s.rest.first = 7
Link(8, s.rest)


"""
Property methods

In some cases, we want the value of instance attributes to be computed on demand.

For example, if we want to access the second element of a linked list

s.second

The @property decorator on a method designates that it will be called whenever
it is looked up on an instance.

A @<attribute>.setter decorator on a method designates that it will be called
whenever attribute is assigned. <attribute> must be an existing property method.
"""

s = Link(3, Link(4, Link(5)))
s.second
s.second = 9
s.second



# Linked lists
"""
A Python list stores all of its elements in a single object, and each element can
be accessed by using its index. A linked list, on the other hand, is a recursive
object that only stores two things: its first value and a reference to the rest
of the list, which is another linked list.

A valid linked list can be one of the following:
    1. An empty linked list (Link.empty)
    2. A Link object containing the first value of the linked list and 
    a reference to the rest of the linked list

What makes a linked list recursive is that the rest attribute of a single Link
instance is another linked list! In the big picture, each Link instance stores
a single value of the list. When multiple Links are linked together through each
instances's rest attribute, an entire sequence is formed.

Noted: Thie definition means that the rest attribute of any Link instance must be 
either Link.empty or another Link instance! This is enforced in Link.__init__,
which raises an AssertionError if the value passed in for rest is neither of 
these thinkg.
"""

class Link:
    """ A linked list.
    
    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.second
    3
    >>> s.first = 5
    >>> s.second = 6
    >>> s.rest.rest = Link.empty
    >>> s     # displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link((Link(8, Link(9))))))
    >>> print(s)    # print str(s)
    <5, 7 <8, 9>>
    """
    empty = ()
    
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
        
    @property
    def second(self):
        return self.rest.first
    
    @second.setter
    def second(self, value):
        self.rest.first = value
        
    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'
    
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
    
def test_empty(link):
    if link is Link.empty:
        print("This linked list is empty!")
    else:
        print("This linked list is not empty!")


s = Link(1)
s.rest is Link.empty
repr(s.first)
s
print(s)

s = Link(2, Link(3, Link(4)))
s
print(s)


"""
Scheme is a programming language that uses linked lists for almost everything.

Suppose we want to add an item at the head of the list:
    with Python's built=in list, if you want to put an item into the container
    labeled with index 0, you must move all the items in the list into its neighbor
    containers to make room for the first item;
    
    with linked list, you tell Python that the neighbor of the new item is
    the old beginning of the list.
"""


# Trees (again)
"""
A tree is a recursive abstract data type that has a label (the value stored in
the root of the tree) and branches (a list of trees directly underneath the root)

"""

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)
        
    def is_leaf(self):
        return not self.branches
    


# Linked lists

class Link:
    empty = ()
    
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
        
    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)
    

def filter_link(f, s):
    """Return elements e of s for which f(e) is true."""
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered
        

def extend_link(s, t):
    if empty(s):
        return t
    else:
        return Link(s.first, extend_link(s.rest), t)


# sets as unsorted sequence

def empty(s):
    return s is Link.empty


def contains(s, v):
    """Return true if set s contains value v as an element"""
    if empty(s):
        return False
    elif s.first == v:
        return True
    else:
        return contains(s.rest, v)
    

def adjoin(s, v):
    if contains(s, v):
        return s
    else:
        return Link(v, s)
    
    
def intersect(set1, set2):
    in_set2 = lambda v: contains(set2, v)
    return filter_link(in_set2, set1)


def union(set1, set2):
    not_in_set2 = lambda v: not contains(set2, v)
    set1_not_set2 = filter_link(not_in_set2, set1)
    return extend_link(set1_not_set2, set2)


# Sets as sorted sequences
def empty(s):
    return s is Link.empty


def contains(s, v):
    """
    Return true if set s contains value v as an element
    >>> s = Link(1, Link(3, Link(2)))
    >>> contains(s, 2)
    True
    >>> contains(s, 5)
    False
    """
    if empty(s) or s.first > v:
        return False
    elif s.first == v:
        return True
    else:
        return contains(s.rest, v)
    
    
def adjoins(s, v):
    if empty(s) or v < s.first:
        return Link(v, s)
    elif v == s.first:
        return s
    else:
        return Link(s.first, adjoins(s.rest, v))
    
    
s = Link(1, Link(3, Link(5)))
s
contains(s, 1)
contains(s, 2)
contains(s, 6)
adjoins(s, 3)
adjoins(s, 2)
s
t = adjoins(s, 2)
t
adjoins(t, 6)
adjoins(t, 0)


# A set if represented by a linked list with unique elements that is ordered from least to greatest
def intersect(set1, set2):
    if empty(set1) or empty(set2):
        return Link.empty
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Link(e1, intersect(set1.rest, set2.rest))
        elif e1 < e2:
            return intersect(set1.rest, set2)
        elif e2 < e1:
            return intersect(set1, set2.rest) 
        

def union(set1, set2):
    if empty(set1):
        return set2
    elif empty(set2):
        return set1
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Link(e1, union(set1.rest, set2.rest))
        elif e1 < e2:
            return Link(e1, union(set1.rest, set2))
        elif e1 > e2:
            return Link(e2, union(set1, set2.rest))
        
s = Link(1, Link(3, Link(5)))
t = Link(2, Link(3, Link(4)))
union(s, t)
union(t, s)


def add(s, v):
    """Add v to a set s and return s."""
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and empty(s.rest):
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest, v)
    return s

s = Link(1, Link(3, Link(5)))
s
add(s, 0)
add(s, 4)
add(s, 6)




# Tree sets

# Binary Tree Class
"""
A binary tree is a tree that has a left branch and a right branch.

Idea: Fill the place of a missing left branch with an empty tree

Idea2: an instance of BTree always has exactly two branches.
"""

# Trees
class Tree:
    """A tree with a label and a list of braches"""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)
        
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)
    
    def __str__(self):
        return '\n'.join(self.indented())
    
    def indented(self, k=0):
        indented = []
        for b in self.branches:
            for line in b.indented(k+1):
                indented.append(' ' + line)
        return [str(self.label)] + indented
    
    def is_leaf(self):
        return not self.branches


# Binary trees

class BTree(Tree):
    """A tree with exactly two branches, which may be empty."""
    empty = Tree(None)
    
    def __init__(self, label, left=empty, right=empty):
        for b in (left, right):
            assert isinstance(b, BTree) or b is BTree.empty
        Tree.__init__(self, label, (left, right))
        
    @property
    def left(self):
        return self.branches[0]
    
    @property
    def right(self):
        return self.branches[1]
    
    def is_leaf(self):
        return [self.left, self.right] == [BTree.empty] * 2
    
    def __repr__(self):
        if self.is_leaf():
            return 'BTree({0})'.format(self.label)
        
        elif self.right is BTree.empty:
            left = repr(self.left)
            return 'BTree({0}, {1})'.format(self.label, left)
        
        else:
            left, right = repr(self.left), repr(self.right) 
            if self.left is BTree.empty:
                left = 'BTree.empty'
            template = 'BTree({0}, {1}, {2})'
            return template.format(self.label, left, right)
        
    
BTree(3)
BTree(3).is_leaf()
t = BTree(3, BTree(1), BTree(5))
t            
t.right    
t.left
t.label
t.left.label


def fib_tree(n):
    """a Fibonacci tree."""
    if n == 0 or n == 1:
        return BTree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return BTree(fib_n, left, right)

fib_tree(3)
fib_tree(3).left
fib_tree(3).right
fib_tree(3).right.label


def contents(t):
    if t is BTree.empty:
        return []
    else:
        return contents(t.left) + [t.label] + contents(t.right)

fib_tree(3)
contents(fib_tree(3))




# Binary Search Trees

"""
Binary search is a strategy for finding a value in a sorted list: check the middle
and eliminate half.

A binary search tree is a binary tree where each node's label is:
    larger than all node labels in its left branch and
    smaller than all node labels in its right branch

"""


def balanced_bst(s):
    """construct a binary search tree from a sorted list."""
    if not s:
        return BTree.empty
    else:
        mid = len(s) // 2
        left = balanced_bst(s[:mid])
        right = balanced_bst(s[mid+1:])
        return BTree(s[mid], left, right)

balanced_bst([3])
balanced_bst([3, 4, 5])
balanced_bst(range(10))



def largest(t):
    """What is the largest element in a binary search tree?"""
    if t.right is BTree.empty:
        return t.label
    else:
        return largest(t.right)
    


def second(t):
    """What's the second largest element in a binary search tree?"""
    if t.is_leaf():
        return None
    elif t.right is BTree.empty:
        return largest(t.left)
    elif t.right.is_leaf():
        return t.label
    else:
        return second(t.right)
    
    
    
# Membership in Binary Search Trees
"""
contains traverses the tree
If the element is not the label, it can only be either the left or right branch
By focusing on one branch, we reduce the set by the size of the other branch
"""
def contains(s, v):
    if s is BTree.empty:
        return False
    elif s.label == v:
        return True
    elif s.label < v:
        return contains(s.right, v)
    elif s.label > v:
        return contains(s.left, v)



# Adjoining to a Tree Set
def adjoin(s, v):
    if s is BTree.empty:
        return BTree(v)
    elif s.label == v:
        return s
    elif s.label < v:
        return BTree(s.label, s.left, adjoin(s.right, v))
    elif s.label > v:
        return BTree(s.label, adjoin(s.left, v), s.right)

odds = [2*n+1 for n in range(6)] 
odds
t = balanced_bst(odds)
t
adjoin(t, 8)
adjoin(t, 3)
adjoin(t, 4)





# Lists
s = [2, 3]
t = [5, 6]
s + [t]


t = [1, 2, 3]
t[1: 3] = [t]
t
 


# object class
"""
Instance attributes are found before class attributes;
class attributes are inheritated."""

class Worker:
    greeting = 'Sir'
    def __init__(self):
        self.elf = Worker

    def work(self):
        return self.greeting + ', I work.'
    
    def __repr__(self):
        return Bourgeoisie.greeting
    

class Bourgeoisie(Worker):
    greeting = 'Peon'
    def work(self):
        print(Worker.work(self))
        return 'I gather wealth.'
    

jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'
    

Worker().work()

jack    

jack.work()    

john.work()    

john.elf.work(john)    
    


# mutable linked lists

# Link, Tree, and BinaryTree classes
class Link:
    """A linked list."""
    empty = ()
    
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest
    
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]
        
    def __len__(self):
        return 1 + len(self.rest)
    
    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)


s = Link(3, Link(5, Link(7)))
t = Link(7, Link(9))
s.first
s.first = 2
s
s.rest.rest
s.rest.rest = t
s

"""
Attribute assignment statements can change first and rest attributes of a link

The rest of a linked list can contain the linked list as a sub-list"""

s = Link(1, Link(2, Link(3)))
s.first    
s.first = 5    
s    
t = s.rest
t
t.rest
t.rest = s
s.first
s.rest.rest.rest.first





abcd = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.'}

def morse(code):
    root = Tree(None)
    for letter, signals in sorted(code.items()):
        tree = root
        for signal in signals:
            match = [b for b in tree.branches if b.label == signal]
            if match:
                assert len(match) == 1
                tree = match[0]
            else:
                branch = Tree(signal)
                tree.branches.append(branch)
                tree = branch
        tree.branches.append(Tree(letter))
    return root


def decode(signals, tree):
    """Decode signals into a letter
    
    >>> t = morse(abcd)
    >>> [decode(s, t) for s in ['-..', '.', '-.-', '.-', '-..', '.']]
    ['d', 'e', 'c', 'a', 'd', 'e']
    """
    for signal in signals:
        tree = [b for b in tree.branches if b.label == signal][0]
    leaves = [b for b in tree.branches if not b.branches]
    assert len(leaves) == 1
    return leaves[0].label



# Tree class
class Tree:
    """A tree with entry as its root value"""
    def __init__(self, label, branches=()):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.label, branches_str)
    
    def pretty_print(self, indent=0):
        print(' ' * indent + str(self.label))
        for branch in self.branches:
            branch.pretty_print(indent + 1)


