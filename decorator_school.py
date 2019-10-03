def run(tasks, characteristic, x):
    print(f'====== {characteristic} ======')
    for task in tasks:
        if getattr(task, characteristic, False):
            y = task(x)
            print(f'{x:,d} --({task.__name__})--> {y:,d}')
            x = y
    print()
 
########################################################
 
def square(x):
    return x ** 2
 
square.happy = True
 
def cube(x):
    return x ** 3
 
cube.playful = True
 
def increment(x):
    return x + 1
 
increment.happy = True
increment.playful = True
 
def decrement(x):
    return x - 1
 
def double(x):
    return x * 2
 
double.happy = True
 
def halve(x):
    return x // 2
 
def collatz(x):
    return 3*x + 1 if x%2 else x // 2
 
collatz.happy = True
collatz.playful = True
 
tasks = [halve, square, increment, collatz,
         decrement, halve, cube, decrement,
         halve, square, decrement]
 
run(tasks, 'happy', 10)
run(tasks, 'playful', 10)
run(tasks, 'happy', 20)
