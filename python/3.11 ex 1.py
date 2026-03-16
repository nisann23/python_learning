# 3.11 ex #modular programming (functions)
#ne oldugunu yaz

def add(a, b):
    return a+b
def substract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a/b
 
