def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def divide_by_0(a, b):
    if b == 0:
        b=1
        return a / b

def hello_world():
    return 'Hello World'
