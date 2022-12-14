from approximation.approximation_output import show_title, show_res
from approximation.approximation_converter import int_massive
from approximation.approximation_calculations import get_resolve_element, slau, transp, matrix_multiplication, interpreter_right_side, get_sides, get_right_side, get_left_side, calculation_least_squares_method, calculate_polinom_approximation, calculation_linear_approximation

def matrix_append(matrix_rows, matrix):
    #Ввод строк матрицы. Условно контроллер
    for i in range(matrix_rows): 
            matrix.append(list(map(float, input(f"Введите строки массива через пробел: ").split())))

def ride_side_of_matrix_append(matrix_rows, right_side_of_matrix):
    #Ввод строк правой части матрицы. Условно контроллер
    for i in range(matrix_rows): 
            right_side_of_matrix.append(list(map(float, input(f"Введите правую часть: ").split())))

def input_one_matrix():
    #Ввод одной матрицы. Условно контроллер
    matrix_rows=int(input("Введите количество строк в массиве (ввод через пробел): "))
    matrix = []
    matrix_append(matrix_rows, matrix)
    return matrix

def input_two_matrices():
    #Ввод двух матриц. Условно контроллер
    matrix_rows=int(input("Введите количество строк массива (ввод через пробел): "))
    matrix_1 = []
    matrix_append(matrix_rows, matrix_1)  
    matrix_2 = [] 
    ride_side_of_matrix_append(matrix_rows, matrix_2)
    return matrix_1, matrix_2

def input_one_massive():
    #Ввод одного массива. Условно контроллер
    m1 = input("Введите значения x (ввод через пробел): ")
    a = int_massive(m1)
    return a

def least_squares_method():
    #1.____________Метод наименьших квадратов (МНК) в матричном виде____________. Контроллер
    show_title("1.Метод наименьших квадратов (МНК) в матричном виде")
    left_side, right_side = input_two_matrices()
    res = calculation_least_squares_method(left_side, right_side)
    show_res(res, "Ответ")

def linear_approximation():
    #2.____________Линейная аппроксимация____________. Контроллер
    show_title("2. Линейная аппроксимация")
    matrix = input_one_matrix()
    some_x = input_one_massive()
    res = calculation_linear_approximation(matrix, some_x)
    show_res(res, "Ответ")

def polinom_approximation():
    #3.____________Аппроксимация полиномом____________. Контроллер
    show_title("3. Аппроксимация полиномом")
    right_side = input_one_matrix()
    x_value = input_one_massive()
    res = calculate_polinom_approximation(right_side, x_value)
    show_res(res, "Ответ")

def get_actions():
    # Получение доступных действий
    return [least_squares_method, linear_approximation, polinom_approximation]