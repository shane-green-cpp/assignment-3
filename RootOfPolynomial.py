import numpy as np
# DONE Bisection method
# TODO Newton's method
# TODO Secant method
# TODO Hybrid method

iterations = 10000
epsilon = pow(2, -23)
delta = 0.00001
numbers = [3, 5, 0, -7]

def bisection(func, a, b, maxIter, eps):
    f = np.poly1d(func)
    fa = f(a)
    fb = f(b)

    if fa * fb >= 0:
        print("Inadequate values for a and b.")
        return -1.0
    
    error = b - a

    for it in range(1, maxIter):
        error = error / 2
        c = a + error
        fc = f(c)

        if abs(error) < eps or fc == 0:
            print("Algorithm has converged after " + str(it) + " iterations!") 
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        
    print("Max iterations reached without convergence...")
    return c

def newtonMethod(func, x, maxIter, eps, delta):
    f = np.poly1d(func)
    derF = np.polyder(f)
    fx = f(x)

    for it in range(1, maxIter):
        fd = derF(x)

        if abs(fd) < delta:
            print("Small slope!")
            return x
        
        d = fx / fd
        x = x-d
        fx = f(x)

        if abs(d) < eps:
            print("Algorithm has converged after " + str(it) + " iterations!")
            return x
    
    print("Max iterations reached without convergence...")
    return x


print("bisection")
print(bisection(numbers, 0, 1, iterations, epsilon))
print("newtons")
print(newtonMethod(numbers, 1, iterations, epsilon, delta))