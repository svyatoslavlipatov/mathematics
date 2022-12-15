from interpolation.interpolation_output import show_title, show_res
from interpolation.interpolation_converter import int_massive
from interpolation.interpolation_calculations import get_coord1_and_coord2, get_x_and_y, calculation_linear_interpolation, calculation_linear_interpolation, calculation_piecewise_linear_interpolation, calculation_lagrange_polynomial
from interpolation.interpolation_drawings import draw_linear_interpolation, draw_piecewise_linear_interpolation, draw_lagrange_polynomial

def get_value_of_x():
    #Ввод значения x. Условно контроллер
    return int(input("Введите значение X: "))

def matrix_append(matrix_rows, matrix):
    #Ввод строк матрицы. Условно контроллер
    for i in range(matrix_rows): 
            matrix.append(list(map(float, input(f"Введите строки массива через пробел: ").split())))

def input_one_matrix():
    #Ввод одной матрицы. Условно контроллер
    matrix_rows=int(input("Введите количество строк в массиве: "))
    matrix = []
    matrix_append(matrix_rows, matrix)
    return matrix

def input_one_massive():
    #Ввод одного массива. Условно контроллер
    m1 = input("Введите значения x через пробел: ")
    a = int_massive(m1)
    return a

def linear_interpolation():
    #1.___________Линейная интерполяция______________. Контроллер
    show_title("1.Линейная интерполяция")
    matrix = input_one_matrix()
    x, y = get_x_and_y(matrix)
    xp = get_value_of_x()
    yp = calculation_linear_interpolation(x, y, xp)
    show_res(yp, "Значение y")
    draw_linear_interpolation(x, y, xp, yp)

def piecewise_linear_interpolation():
    #2.___________Кусочно-линейная интерполяция______________. Контроллер
    show_title("2.Кусочно-линейная интерполяция")
    matrix = input_one_matrix()
    x, y = get_x_and_y(matrix)
    xp =  input_one_massive()
    yp = calculation_piecewise_linear_interpolation(x, y, xp)
    show_res(yp, "Значения y")
    draw_piecewise_linear_interpolation(x, y, xp, yp)

def lagrange_polynomial():
    #3.___________Полином Лагранжа______________. Контроллер
    show_title("3.Полином Лагранжа")
    matrix = input_one_matrix()
    x, y = get_x_and_y(matrix)
    xp = get_value_of_x()
    yp = calculation_lagrange_polynomial(x, y, xp)
    show_res(yp, "Значение y")
    draw_lagrange_polynomial(x, y, xp, yp)

def get_actions():
    # Получение доступных действий
    return [linear_interpolation, piecewise_linear_interpolation, lagrange_polynomial]
