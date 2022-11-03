def add(mas_1, mas_2):
    #Сумма матриц. Вычисление
    res = []
    for i in range(len(mas_1)):
        l = (list(map(lambda x, y: x + y, mas_1[i], mas_2[i])))
        res.append(l)
    return res

def sub(mas_1, mas_2):
    #Разность матриц. Вычисление
    res = []
    for i in range(len(mas_1)):
        l = (list(map(lambda x, y: x - y, mas_1[i], mas_2[i])))
        res.append(l)
    return res

def transp(mas):
    #Транспонирование матрицы. Вычисление
    return [list(i) for i in zip(*mas)]


def multiplication_matrix_by_scalar(mas_1, s1):
    #Умножение матрицы на скаляр. Вычисление
    res = []
    for i in range(len(mas_1)):
        l = [s * s1 for s in mas_1[i]]
        res.append(l)
    return res


def multiply_matrices(mas_1, mas_2, columns, lines):
    #Умножение матриц. Вычисление
    if lines == columns:
        length = len(mas_1) 
        res = [[0 for i in range(length)] for i in range(length)]
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    res[i][j] += mas_1[i][k] * mas_2[k][j]
        return res
    else:
        res = "Невозможно умножить матрицы."
        return res

def get_columns_lines(mas_1, mas_2):
    #Получение строки и столбца матрицы для проверки. Вычисление
    columns = 0
    lines = len(mas_1[0])
    for i in mas_2:
        columns += 1
    return columns,lines

def get_index(mas, ind):
    #Получение индекса из матрицы. Вычисление
    return mas[ind]

def repl_index(mas_1, ind_1, ind_2):
    #Перестаовка строк матрицы. Вычисление
    mas_1[ind_1], mas_1[ind_2] = mas_1[ind_2], mas_1[ind_1]
    return mas_1

def multi_string_by_scalar(mas_1, s1, ind):
    #Умножение строки на скаляр. Вычисление
    return [s * s1 for s in mas_1[ind]]

def summ_lines(a, b):
    #Сложение строк. Вычисление
    return list(map(lambda x, y: x + y, a, b))

def sub_lines(multi_ind_1, multi_ind_2):
    #Разность строк. Вычисление
    return list(map(lambda x, y: x - y, multi_ind_1, multi_ind_2))