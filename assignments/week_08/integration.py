# Students should edit this Python file (just as you would a Python cell in a Jupyter Notebook)
# this module will contain functions for numerical integration


def trapezoidal_rule(f, a, b, N):
    h = (b - a) / N
    
    total = f(a) + f(b)
    
    for i in range(1, N):
        x = a + i * h
        total += 2 * f(x)
    
    return (h / 2) * total



def simpsons_rule(f, a, b, N):
    if N % 2 != 0:
        raise ValueError("N must be even for Simpson's rule")
    
    h = (b - a) / N
    
    total = f(a) + f(b)
    
    for i in range(1, N):
        x = a + i * h
        
        if i % 2 == 0:
            total += 2 * f(x)
        else:
            total += 4 * f(x)
    
    return (h / 3) * total