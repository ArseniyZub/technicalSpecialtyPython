import json
import math

def save_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                "arguments": args,
                "result": result
            }
            with open(filename, 'w') as jsonfile:
                json.dump(data, jsonfile)
            return result
        return wrapper
    return decorator

@save_json('file1.json')
def quadratic_roots(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        root1 = (-b + math.sqrt(D)) / (2*a)
        root2 = (-b - math.sqrt(D)) / (2*a)
        return {"root1": root1, "root2": root2}
    elif D == 0:
        root1 = -b / (2*a)
        return {"root": root1}
    else:
        return {"error": "Нет корней"}

quadratic_roots(1, -3, 2)  