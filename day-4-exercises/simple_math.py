"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    Summing up two variables a and b
    """
    return a+b

def simple_sub(a,b):
    """
    Subtraction of variable b from a
    """
    return a-b

def simple_mult(a,b):
    """
    Multiplication of two variables a and b
    """
    return a*b

def simple_div(a,b):
    """
    Division of variable a by b
    """
    return a/b

def poly_first(x, a0, a1):
    """
    Polynomial operation
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    Quadratic polynomial operation
    """
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
