import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        logging.error('Attempted to divide by zero')
        raise ValueError("Cannot divide by zero.")
    logging.debug(f'Dividing {a} by {b}')
    return a / b

def divide_by_0(a, b):
    if b == 0:
        b=1:
        return a / b

def hello_world():
    return 'Ciao Mondo'
