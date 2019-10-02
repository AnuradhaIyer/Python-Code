'''
 
Use the command-line for short snippets:
 
    $ python3.8 -m timeit -s 'data = list(range(10_000))' 'sum(data)'
    5000 loops, best of 5: 71.1 usec per loop
 
'''
 
from timeit import repeat
 
setup = '''
data = list(range(10000))
 
def mysum(seq):
    total = 0
    for x in seq:
        total += x
    return total
''' 
print(min(repeat('sum(data)', setup, number=500)))
print(min(repeat('mysum(data)', setup, number=5000)))
