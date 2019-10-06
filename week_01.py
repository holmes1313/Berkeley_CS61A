
"""
the most important part:
    Lab section
    Discussion section


A course about managing complexity
    mastering abstraction
    programming paradigms
    
    

All expressions can use function called notation.
"""


"""
UNIX commands
Directories:

ls: list the files and folders inside of the current directory
mkdir: make a new directory. For example, mkdir example creates a directory called example
cd: change directories. For example, cd example changes directories to example
rm -r: recursively remove a specified directory. For example, rm -r example removes the example directory and all files and subdirectories inside it.
Files:

cat: displays the contents of a file on the screen. For example, cat unix.txt shows the contents of the file unix.txt
mv: moves a file/directory to another file/directory. For example, mv file1 file2 moves the contents of file1 into a (possibly new) file called file2. When moving one file to another, we are effectively renaming the file!
cp: copies a file to another file/directory. For example, cp file1 file2 copies the contents of file1 into a file named file2.
rm: removes a file. For example, rm file1 deletes the file called file1.
Miscellaneous:

echo: displays words on the screen
man: displays manual pages for a specified command
"""


"""
Vim has different modes, each of which allow you to do different things.

Normal mode (ESC key) allows you to use keyborad shortcusts for navigation, file manipulation, etc.
Normal mode is connected to all the other modes.

Insert mode (i) allows you to use Vim like a regular editor

Commond mode (normal mode -> : key)
To save the file, type the letter w and then press Enter.
To close vim, type the letter q and then press Enter.

If you have unsaved change and you don't want to save it, you can add an exclamation mark to the q (:q!)


VIM keyboard shortcuts
line:
    0: moves to the beginning of the line
    $: moves to the end of the line

undo and redo in the normal mood, 
    u: to undo a change
    Ctrl-r: to redo a change

Searching in the normal mood,
    search for the word def: /def
    jump to line 42: :42
"""


def greet(name):
    print('Hi', name, ', how are you doing?')
    print(' - Python')

"""
python -i greet.py

    1.python is the command that starts python
    2.the -i flag tells python to start in Interactive mode, which allows you to type in Python commands from your terminal
    3. greet.py is the name of the Python file we want to load
"""



# Assignment Statements
a = 1
b = 2
b, a = a + b, b

"""
Execution rule for assignment statements:
    1. Evaluate all expressions to the right of = from left to right.
    2. Bind all names tot he left of = to the resulting values in the current frame.
"""


# Looking up names in environments
"""
Every expression is evaluated in the context of an environment.

So far, the current environment is either:
    the global frame alone, or
    a local frame, followed by the global frame.
    
*IMPORTANT*
An environment is a sequence of frames.

A name evaluates to the value bound to that name in the earliest frame of the 
current environment in which that name is found.
e.g., to look up some name in the body of the square function:
    1.look for that name in the local frame
    2.if not found, look for it in the global frame.
"""









