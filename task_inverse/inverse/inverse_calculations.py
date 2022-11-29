def get_unit_matrix(matrix):
    #Получение единичной матрицы. Вычисление
    unit_matrix = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
    c = len(matrix)
    for i in range(c):
        for j in range(c):
            unit_matrix[j][j] = 1
    return unit_matrix

def matrix_multiplication(a, b):
    #Умножение матриц. Вычисление
    res = [[0 for __ in range(len(a[0]))] for __ in range(len(b))]  
    for i in range(len(b)):
        for j in range(len(a[0])):      
            res[i][j] = sum(b[i][x] * a[x][j] for x in range(len(a)))
    return res

def add_a_unit_matrix(a, b):
    #Добавление единичной матрицы к матрице. Вычисление
    for i in range(len(a)):
        a[i].extend(b[i])
    return a

def inverse(a, b):
    #Поиск обратной матрицы. Вычисление
    inverse_matrix = []
    a_with_unit = add_a_unit_matrix(a, b)
    n = len(a_with_unit) 
    for k in range(n):
        if abs(a_with_unit[k][k]) < 1.0e-12:
            for i in range(k+1, n):
                if abs(a_with_unit[i][k]) > abs(a_with_unit[k][k]):
                    for j in range(k, 2*n):
                        a_with_unit[k][j], a_with_unit[i][j] = a_with_unit[i][j], a_with_unit[k][j] 
                    break
        resolve_element = a_with_unit[k][k]
        if resolve_element == 0: 
            return False
        else:
            for j in range(k, 2*n): 
                a_with_unit[k][j] /= resolve_element
            for i in range(n):
                if i == k or a_with_unit[i][k] == 0: 
                    continue
                factor = a_with_unit[i][k]
                for j in range(k, 2*n): 
                    a_with_unit[i][j] -= factor * a_with_unit[k][j]
    inverse_matrix_res = get_inverse_matrix(a_with_unit, inverse_matrix, n)
    return inverse_matrix_res

def get_inverse_matrix(a, inverse_matrix, n):
    #Получение обратной матрицы. Вычисление
    for i in range(len(a) ): 
        for j in range(len(a) , len(a[0])):
            inverse_matrix.append(a[i][j])
    inverse_matrix_res = [inverse_matrix[i:i + n] for i in range(0, len(inverse_matrix), n)]
    return inverse_matrix_res