import numpy as np
import sys
# DONE Bisection method
# DONE Newton's method
# DONE Secant method
# DONE Hybrid method
#TODO file IO
#TODO command line arguements

fileName = sys.argv[len(sys.argv) - 1]
sysEqnFile = open(fileName, "r")

contents = sysEqnFile.read()
sysEqnFile.close()

lines = contents.split("\n")
nums = lines[1].split()
func = [int(i) for i in nums]

print(func)

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

def secantMethod(func, a, b, maxIter, eps):
    f = np.poly1d(func)
    fa = f(a)
    fb = f(b)

    if abs(fa) > abs(fb):
        a, b = b, a
        fa, fb = fb, fa
    
    for it in range(1, maxIter):
        if abs(fa) > abs(fb):
            a, b = b, a
            fa, fb = fb, fa
        
        d = (b - a) / (fb - fa)
        b = a
        fb = fa
        d = d * fa

        if abs(d) < eps:
            print("Algorithm has converged after " + str(it) + " iterations!")
            return a
        
        a = a - d
        fa = f(a)
        
    print("Max iterations reached!")
    return a

def hybrid(func, a, b, maxIter, eps, delta):
    print("5 iters of bisection, then newtons")
    x = bisection(func, a, b, 5, eps)
    r = newtonMethod(func, x, maxIter - 5, eps, delta)
    return r

print("bisection")
print(bisection(numbers, 0, 1, iterations, epsilon))
print("newtons")
print(newtonMethod(numbers, 1, iterations, epsilon, delta))
print("secant")
print(secantMethod(numbers, 0, 1, iterations, epsilon))
print("hybrid")
print(hybrid(numbers, 0, 1, iterations, epsilon, delta))