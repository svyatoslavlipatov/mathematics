def get_resolve_element(a, k):
    #Получение разрешающего элемента. Вычисление
    resolve_element = a[k][k]
    return resolve_element

def slau(a,b):
    #Метод Гаусса-Жордана. Вычисление
    n = len(b)
    for k in range(n):
        if abs(a[k][k]) < 1.0e-12:
            for i in range(k+1, n):
                if abs(a[i][k]) > abs(a[k][k]):
                    for j in range(k,n):
                        a[k][j], a[i][j] = a[i][j], a[k][j]
                    b[k], b[i] = b[i], b[k]
                    break
        resolve_element = get_resolve_element(a, k)
        if resolve_element == 0: 
            return False
        else:    
            for j in range(k,n):
                a[k][j] /= resolve_element
            b[k] /= resolve_element
            for i in range(n):
                if i == k or a[i][k] == 0: 
                    continue
                factor = a[i][k]
                for j in range(k,n):
                    a[i][j] -= factor * a[k][j]
                b[i] -= factor * b[k]        
    return b

def transp(mas):
    #Транспонирование матрицы. Вычисление
    return [list(i) for i in zip(*mas)]

def matrix_multiplication(b, a):
    #Умножение матриц. Вычисление
    res = [[0 for __ in range(len(a[0]))] for __ in range(len(b))]  
    for i in range(len(b)):
        for j in range(len(a[0])):      
            res[i][j] = sum(b[i][x] * a[x][j] for x in range(len(a)))
    return res

def interpreter_right_side(multiright):
    #Преобразование правой части.
    return [x for x, in multiright]

def get_sides(matrix):
    #Получение сторон.
    left_side = get_left_side(matrix)
    right_side = get_right_side(matrix)
    return left_side, right_side

def get_right_side(matrix):
    #Получение правой стороны матрицы. Вычисление
    right_side = []
    for i in range(len(matrix)):
        right_side.append([matrix[i][1]])
    return right_side

def get_left_side(matrix):
    #Получение левой стороны матрицы. Вычисление
    left_side = []
    for i in range(len(matrix)):
        left_side.append([matrix[i][0], 1])
    return left_side

def calculation_least_squares_method(left_side, right_side):
    #МНК. Вычисление
    transp_left_side = transp(left_side)
    multi_left = matrix_multiplication(transp_left_side, left_side)
    multi_right = matrix_multiplication(transp_left_side, right_side)
    get_right = interpreter_right_side(multi_right)   
    return slau(multi_left, get_right)

def calculate_polinom_approximation(right_side, x_value):
    #Вычисление полиномом. Вычисление
    Ax = []
    for i in range(len(x_value)):
        A = []
        for j in range(len(right_side)):
            A = [x_value[i]**j] + A
        Ax += [A]
    y = matrix_multiplication(Ax, right_side)
    res = []
    for n in range(len(y)):
        res.append([x_value[n], y[n][0]])
    return res

def calculation_linear_approximation(matrix, some_x):
    #Получение линейной аппроксимации. Вычисление
    left_side, right_side = get_sides(matrix)
    slau_values  = calculation_least_squares_method(left_side, right_side)
    res = []
    for x_value in some_x:
        res.append([x_value, slau_values[0] * x_value + slau_values[1]])
    return res