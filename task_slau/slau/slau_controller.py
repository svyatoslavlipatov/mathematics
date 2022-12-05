from slau.slau_output import show_title, show_res
from slau.slau_converter import int_massive
from slau.slau_calculations import get_resolve_element, gauss_jordan_method

def input_one_massive():
    #Ввод правой части. Условно контроллер
    m = input("Введите правую часть через пробел: ")
    a = int_massive(m)
    return a

def matrix_append(matrix_rows, matrix):
    #Ввод строк матрицы. Условно контроллер
    for i in range(matrix_rows): 
            matrix.append(list(map(int, input(f"Введите строки массива через пробел: ").split())))

def input_one_matrix():
    #Ввод одной матрицы. Условно контроллер
    matrix_rows=int(input("Введите количество строк в массиве: "))
    matrix = []
    matrix_append(matrix_rows, matrix)
    return matrix

def slau():
    #1._____Решение СЛАУ методом Гаусса-Жордана_____. Контроллер
    show_title("1.Решение СЛАУ методом Гаусса-Жордана")
    matrix = input_one_matrix()
    right_side = input_one_massive()
    res = gauss_jordan_method(matrix,right_side)
    show_res(res, "Ответ")

def get_actions():
    # Получение доступных действий
    return [slau]