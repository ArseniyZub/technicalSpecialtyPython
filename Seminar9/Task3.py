import csv
import math

def quadratic_roots(func):
    def wrapper(csv_filename):
        with open(csv_filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if len(row) == 3:
                    a, b, c = map(int, row)
                    result = func(a, b, c)
                    print(result)
    return wrapper

@quadratic_roots
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
    
quadratic_roots('file.csv')  