import math

def quadratic_roots(a, b, c):
    D = b**2 - 4*a*c
    
    if D > 0:
        root1 = (-b + math.sqrt(D)) / (2*a)
        root2 = (-b - math.sqrt(D)) / (2*a)
        return root1, root2
    elif D == 0:
        root1 = -b / (2*a)
        return root1
    else:
        return "Нет корней"

print(quadratic_roots(1, -3, 3))