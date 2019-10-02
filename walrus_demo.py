'''
Walrus operator is :=
official name : PEP 572 Assignment Expressions.

Problem being solved: A regular "=" assignments is a statement
                    and statements cant be used inside statement


Rules:

    1) The assignment expression must be in paranthesis
    2) The return value is wjatever was assigning.


'''


# New way for loop

x = 10
while(y := x * 5) <= 75:
    print(y)
    x += 1

#Declarative statements

sqrt = {x**2 : x for x in range(10)}

#Case whre the walrus operator is good

with open('data/stocks.txt') as f:
    while True:
        block = f.read(10) 
        if not block:
            break
        print(repr(block))

#Better way with walrus

        # Better way with the walrus
with open('data/stocks.txt') as f:
    while (block := f.read(10)):
        print(repr(block))

###### Ways of Pascals Triangle using 

def binomial_coefficients(n):
    'Coefficients of (x + 1) ** n'
    c = 1
    row = [c]
    for k in range(1, n+1):
        c = c * (n - k + 1) // k
        row.append(c)
    return row
         
def binomial_coefficients(n):
    'Coefficients of (x + 1) ** n'
    return [(c := c * (n - k + 1) // k if k else 1) for k in range(n+1)]
            
