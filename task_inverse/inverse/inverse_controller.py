from inverse.inverse_output import show_title, show_res
from inverse.inverse_calculations import get_unit_matrix, matrix_multiplication, add_a_unit_matrix, inverse, get_inverse_matrix  

def matrix_append(matrix_rows, matrix):
    #Ввод строк матрицы. Условно контроллер
    for i in range(matrix_rows): 
            matrix.append(list(map(int, input(f"Введите строки массива через пробел: ").split())))

def ride_side_of_matrix_append(matrix_rows, right_side_of_matrix):
    #Ввод строк правой части матрицы. Условно контроллер
    for i in range(matrix_rows): 
            right_side_of_matrix.append(list(map(int, input(f"Введите правую часть: ").split())))

def input_one_matrix():
    #Ввод одной матрицы. Условно контроллер
    matrix_rows=int(input("Введите количество строк в массиве: "))
    matrix = []
    matrix_append(matrix_rows, matrix)
    return matrix

def input_two_matrices():
    #Ввод двух матриц. Условно контроллер
    matrix_rows=int(input("Введите количество строк массива: "))
    matrix_1 = []
    matrix_append(matrix_rows, matrix_1)  
    matrix_2 = [] 
    ride_side_of_matrix_append(matrix_rows, matrix_2)
    return matrix_1, matrix_2

def search_inverse_matrix():
    #1._____Поиск обратной матрицы методом Гаусса-Жордана_____. Контроллер
    show_title("1. Поиск обратной матрицы методом Гаусса-Жордана")
    matrix = input_one_matrix()
    unit_matrix = get_unit_matrix(matrix)
    inverse_matrix = inverse(matrix, unit_matrix)
    show_res(inverse_matrix, "Обратная матрица")

def slau_by_inverse_matrix():
    #2._____Решение СЛАУ с помощью обратной матрицы_____. Контроллер
    show_title("2. Решение СЛАУ с помощью обратной матрицы")
    matrix, right_side_of_matrix = input_two_matrices()
    unit_matrix = get_unit_matrix(matrix)
    inverse_matrix = inverse(matrix, unit_matrix)
    res = matrix_multiplication(right_side_of_matrix, inverse_matrix)
    show_res(res, "Ответ")


def get_actions():
    # Получение доступных действий
    return [search_inverse_matrix, slau_by_inverse_matrix]