from matrix.matrix_output import show_title, show_res
from matrix.matrix_calculations import add, sub, transp, multiplication_matrix_by_scalar, multiply_matrices, get_columns_lines, get_index, repl_index, multi_string_by_scalar, summ_lines, sub_lines

def input_two_matrices():
    #Ввод двух матриц. Условно контроллер
    matrix_1=int(input("Введите количество строк в первом массиве: "))
    mas_1 = []
    matrix_append(matrix_1, mas_1)  
    matrix_2=int(input("Введите количество строк во втором массиве: "))
    mas_2 = [] 
    matrix_append(matrix_2, mas_2)
    return mas_1,mas_2

def input_one_matrix():
    #Ввод одной матрицы. Условно контроллер
    matrix_1=int(input("Введите количество строк в массиве: "))
    mas_1 = []
    matrix_append(matrix_1, mas_1)
    return mas_1

def matrix_append(matrix, mas):
    #Ввод строк. Условно контроллер
    for i in range(matrix): 
        mas.append(list(map(int, input(f"Введите строки массива через пробел: ").split())))
    return mas

def input_scalar():
    #Ввод скаляра. Условно контроллер
    s1 = int(input("Введите скаляр: "))
    return s1

def input_index(mas):
    #Ввод индекса. Условно контроллер
    return int(input(f"Введите индекс строки от 0 до {len(mas)-1}: "))

def sum_of_matrices():
    #1._______Сложение матриц_______. Контроллер
    show_title("1.Сложение матриц")
    mas_1, mas_2 = input_two_matrices()
    res = add(mas_1, mas_2)
    show_res(res, "Сумма матриц")

def subtracting_matrices():
    #2._______Вычитание матриц_______. Контроллер
    show_title("2.Вычитание матриц")
    mas_1, mas_2 = input_two_matrices()
    res = sub(mas_1, mas_2)
    show_res(res, "Разность матриц")

def transposition():
    #3._______Транспонирование_______. Контроллер
    show_title("3.Транспонирование матрицы")
    mas_1 = input_one_matrix()
    res = transp(mas_1)
    show_res(res, "Транспонированная матрица")

def multiply_on_scalar():
    #4._______Умножение на скаляр_______. Контроллер
    show_title("4.Умножение матрицы на скаляр")
    mas_1 = input_one_matrix()
    s1 = input_scalar()
    res = multiplication_matrix_by_scalar(mas_1, s1)
    show_res(res, "Произведение матрицы на скаляр")

def matrix_multiplication():
    #5._______Умножение матриц_______. Контроллер
    show_title("5.Умножение матриц")
    mas_1, mas_2 = input_two_matrices()
    columns, lines = get_columns_lines(mas_1, mas_2)
    res = multiply_matrices(mas_1, mas_2, columns, lines)
    show_res(res, "Произведение матриц")

def index():
    #6._______Получение строки по индексу_______. Контроллер
    show_title("6.Получение строки по индексу")
    mas_1 = input_one_matrix()
    ind = input_index(mas_1)
    res = get_index(mas_1, ind)
    show_res(res, "Строка по индексу")

def index_transp():
    #7._______Получение столбца по индексу_______. Контроллер
    show_title("7.Получение столбца по индексу")
    mas_1 = input_one_matrix()
    ind = input_index(mas_1)
    res = transp(mas_1)[ind]
    show_res(res, "Столбец по индексу")

def index_rearranging():
    #8._______Перестановка строк матрицы местами_______. Контроллер
    show_title("8.Перестановка строк матрицы местами")
    mas_1 = input_one_matrix()
    ind_1 = input_index(mas_1)
    ind_2 = input_index(mas_1)
    res = repl_index(mas_1, ind_1, ind_2)
    show_res(res, "Измененная матрица")

def multiply_index_on_scalar():
    #9._______Умножение строки матрицы на скаляр_______. Контроллер
    show_title("9.Умножение строки матрицы по заданному индексу на скаляр")
    mas_1 = input_one_matrix()
    s1 = input_scalar()
    ind = input_index(mas_1)
    res = multi_string_by_scalar(mas_1, s1, ind)
    show_res(res, "Произведение строки на скаляр")

def adding_multiplied_strings():
    #10._______Сложение строк, умноженных на число_______. Контроллер
    show_title("10.Сложение строк, умноженных на число")
    mas_1 = input_one_matrix()
    ind_1 = input_index(mas_1)
    ind_2 = input_index(mas_1)
    s1 = input_scalar()
    multi_ind_1 = multi_string_by_scalar(mas_1, s1, ind_1)
    multi_ind_2 = multi_string_by_scalar(mas_1, s1, ind_2)
    res = summ_lines(multi_ind_1, multi_ind_2)
    show_res(res, "Сумма строк, умноженных на число")

def subtraction_multiplied_strings():
    #11._______Вычитание строк, умноженных на число_______. Контроллер
    show_title("11.Вычитание строк, умноженных на число")
    mas_1 = input_one_matrix()
    ind_1 = input_index(mas_1)
    ind_2 = input_index(mas_1)
    s1 = input_scalar()
    multi_ind_1 = multi_string_by_scalar(mas_1, s1, ind_1)
    multi_ind_2 = multi_string_by_scalar(mas_1, s1, ind_2)
    res = sub_lines(multi_ind_1, multi_ind_2)
    show_res(res, "Разность строк, умноженных на число")

def get_actions():
    # Получение доступных действий
    return [sum_of_matrices, subtracting_matrices, transposition, multiply_on_scalar, matrix_multiplication, index, index_transp, index_rearranging, multiply_index_on_scalar, adding_multiplied_strings, subtraction_multiplied_strings]