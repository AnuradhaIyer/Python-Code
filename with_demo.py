''' Goal:  Become a black belt with the with-statement
 
What does it do?            On the day you are born, make all of your own funeral arrangement.
                            Contexts should know how to set themselves up and tear themselves down.
 
What does it work?          There are two dunder methods:  __enter__ and __exit__
 
What do it you call it?     Context managers: files, locks, database connections
 
Advice on writing on context managers:
 
    Any data known in advance
    and reused through out the "with"
    should be in __init__
    >>> 
    Anything done before the "try"
    goes in __enter__
    >>> 
    Anything done in the "except/finally"
    goes in __exit__
 
'''
 
# Old-way to open and close a file: 200% overhead
f = open('data/hamlet.txt')
try:
    play = f.read()
    print(len(play))
finally:
    f.close()
 
# New-way to open and close a file: 50% overhead
with open('data/hamlet.txt') as f:
    play = f.read()
    print(len(play))    
 
# How to create locks ##########################################################
 
import threading
 
printer_lock = threading.Lock()
 
# How to use locks -- The old-fashioned way: 200% overhead
 
printer_lock.acquire()         # Blocks until the resource becomes available
try:
    print('Critical section 1')
    print('Critical section 2')
finally:
    printer_lock.release()
 
# How to use locks -- The old-fashioned way: 50% overhead
 
with printer_lock:
    print('Critical section 1')
    print('Critical section 2')
 
 
# How to make a context manager ############################
 
class CM:
 
    def __init__(self, x):
        print('Initializing with', x)
        self.x = x
         
    def __enter__(self):
        print('Entering')
        print('and x is still', self.x)
        return 42
 
    def __exit__(self, exctype, excinst, exctb):
        print('Exiting with', exctype, excinst, exctb)
        if isinstance(excinst, KeyError):
            print('Handling the KeyError')
            return True
        return False       # Same as the default "return None"
 
print('Case 1: Normal flow with no exceptions')
print('Starting up')
with CM(10) as y:
    print('In the beginning with')
    print('In the middle')
    print('At the end')
print('Finishing up with')    
 
print('Case 2: Normal flow with a handled exceptioo')
print('=' * 20)
print('Starting up')
with CM(10) as y:
    print('In the beginning with')
    print('In the middle')
    raise KeyError('tom')
    print('Never gets here')
print('Finishing up with')
 
print('Case 3: Unhandled exceptioo')
print('=' * 20)
print('Starting up')
try:
    with CM(10) as y:
        print('In the beginning with')
        print('In the middle')
        raise IndexError(5)
        print('Never gets here')
    print("Won't get here either")
except IndexError:
    print('Doh! Bad index')
print('Finishing up with')
 
###########################################################
## Output redirection
 
import sys, os
 
def square(x):
    'Return a value times itself'
    return x**2
 
def newhelp(obj):
    'Replacement for the built-in help'
    print('=' * 30)
    print('This object is a', type(obj))
    print('It came from:', obj.__module__)
    print('Its name is:', obj.__name__)
    print('What is does:')
    print(obj.__doc__)
    print()
 
from dis import dis
 
class RedirectStdout:
    'Temporarily change stdout to some other target'
 
    def __init__(self, target):
        self.target = target
 
    def __enter__(self):
        self.oldstdout = sys.stdout
        sys.stdout = self.target
        return self.target
 
    def __exit__(self, exctype, excinst, exctb):
        sys.stdout = self.oldstdout
 
class Ignore:
    'Temporarily ignore some category of exception'
 
    def __init__(self, ignored_exception):
        self.ignored_exception = ignored_exception
 
    def __enter__(self):
        return self.ignored_exception
 
    def __exit__(self, exctype, excinst, exctb):
        if isinstance(excinst, self.ignored_exception):
            return True
         
         
with RedirectStdout(sys.stderr):
    help(square)
 
with open('square_help.txt', 'w') as f:
    with RedirectStdout(f):
        newhelp(square)
 
# Goal:  dis() output must be in lowercase
with open('tmp.txt', 'w') as f:
    with RedirectStdout(f):
        dis(square)
with open('tmp.txt') as g:
    dis_output = g.read()
try:
    os.unlink('tmp.txt')
except FileNotFoundError:
    pass
 
print(square(11))
 
 
