# Напишите функцию для транспонирования матрицы

def transpose(table):
    table0 = []

    for i in range(len(table[0])):
        table0.append(list())
        for j in range(len(table)):
            table0[i].append(table[j][i])
    return table0


matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)
matrix2 = transpose(matrix)
print(matrix2)