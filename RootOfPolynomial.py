import numpy as np
import sys
# DONE Bisection method
# DONE Newton's method
# DONE Secant method
# DONE Hybrid method
#DONE file IO
#TODO command line arguements

fileName = sys.argv[len(sys.argv) - 1]
solutionFile = fileName[0:len(fileName) - 3] + "sol"
polynomialFile = open(fileName, "r")

contents = polynomialFile.read()
polynomialFile.close()

lines = contents.split("\n")
nums = lines[1].split()
func = [int(i) for i in nums]

def writeSolution(root, it, outcome):
    print(root)
    print(it)
    print(outcome)
    f = open(solutionFile, "w")

    f.write(str(root) + " ")
    f.write(str(it) + " ")
    f.write(outcome)
    f.close()

print(func)

iterations = 10000
#itCompleted = 0
#outcome = ""
epsilon = pow(2, -23)
delta = 0.00001
numbers = [3, 5, 0, -7]

def bisection(func, a, b, maxIter, eps):
    global outcome
    global itCompleted
    f = np.poly1d(func)
    fa = f(a)
    fb = f(b)

    if fa * fb >= 0:
        print("Inadequate values for a and b.")
        outcome = "fail"
        return -1.0
    
    error = b - a

    for it in range(1, maxIter):
        error = error / 2
        c = a + error
        fc = f(c)

        if abs(error) < eps or fc == 0:
            itCompleted = it
            print("Algorithm has converged after " + str(it) + " iterations!") 
            outcome = "success"
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        
    print("Max iterations reached without convergence...")
    outcome = "fail"
    itCompleted = maxIter
    return c

def newtonMethod(func, x, maxIter, eps, delta):
    global outcome
    global itCompleted
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
            itCompleted = it
            print("Algorithm has converged after " + str(it) + " iterations!")
            outcome = "success"
            return x
    
    print("Max iterations reached without convergence...")
    outcome = "fail"
    itCompleted = maxIter
    return x

def secantMethod(func, a, b, maxIter, eps):
    global outcome
    global itCompleted
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
            itCompleted = it
            print("Algorithm has converged after " + str(it) + " iterations!")
            outcome = "success"
            return a
        
        a = a - d
        fa = f(a)
        
    print("Max iterations reached!")
    outcome = "fail"
    itCompleted = maxIter
    return a

def hybrid(func, a, b, maxIter, eps, delta):
    global outcome
    global itCompleted
    print("5 iters of bisection, then newtons")
    x = bisection(func, a, b, 5, eps)
    if (outcome == "success"):
        return x
    r = newtonMethod(func, x, maxIter - 5, eps, delta)
    itCompleted += 5
    return r

if sys.argv[1] == "-newt":
    if sys.argv[2] == "-maxIter":
        iterations = int(sys.argv[3])
        x = float(sys.argv[4])
        root = newtonMethod(func, x, iterations, epsilon, delta)
        writeSolution(root, itCompleted, outcome)
    else:
        x = float(sys.argv[2])
        root = newtonMethod(func, x, iterations, epsilon, delta)
        writeSolution(root, itCompleted, outcome)

elif sys.argv[1] == "-sec":
    if sys.argv[2] == "-maxIter":
        iterations = int(sys.argv[3])
        a = float(sys.argv[4])
        b = float(sys.argv[5])
        root = secantMethod(func, a, b, iterations, epsilon)
        writeSolution(root, itCompleted, outcome)
    else:
        a = float(sys.argv[2])
        b = float(sys.argv[3])
        root = secantMethod(func, a, b, iterations, epsilon)
        writeSolution(root, itCompleted, outcome)

elif sys.argv[1] == "-hybrid":
    if sys.argv[2] == "-maxIter":
        iterations = int(sys.argv[3])
        a = float(sys.argv[4])
        b = float(sys.argv[5])
        root = hybrid(func, a, b, iterations, epsilon, delta)
        writeSolution(root, itCompleted, outcome)
    else:
        a = float(sys.argv[2])
        b = float(sys.argv[3])
        root = hybrid(func, a, b, iterations, epsilon, delta)
        writeSolution(root, itCompleted, outcome)
else:
    if sys.argv[1] == "-maxIter":
        iterations = int(sys.argv[2])
        a = float(sys.argv[3])
        b = float(sys.argv[4])
        root = bisection(func, a, b, iterations, epsilon)
        writeSolution(root, itCompleted, outcome)
    else:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        root = bisection(func, a, b, iterations, epsilon)
        writeSolution(root, itCompleted, outcome)
