import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Set up basic logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def add(a, b):
    logger.debug(f'Adding {a} + {b}')
    return a + b

def subtract(a, b):
    logger.debug(f'Subtracting {a} - {b}')
    return a - b

def multiply(a, b):
    logger.debug(f'Multiplying {a} * {b}')
    return a * b

def divide(a, b):
    logger.debug(f'Dividing {a} by {b}')
    if b == 0:
        logger.error('Attempted to divide by zero')
        raise ValueError("Cannot divide by zero.")
    return a / b

def divide_by_0(a, b):
    logger.debug(f'Divide by 0 function called with {a} and {b}')
    if b == 0:
        logger.warning('Received 0 for b, adjusting to 1 to avoid division by zero')
        b = 1
    return a / b

def hello_world():
    logger.info('Hello world function called')
    return 'Ciao Mondo'
