from maclaurinseries.maclaurin_output import show_title, show_res
from maclaurinseries.maclaurin_calculations import calculations_maclaurin_series_exp, calculations_maclaurin_series_cos, calculations_maclaurin_series_sin, calculations_maclaurin_series_arcsin, calculations_maclaurin_series_arccos

def input_x_and_n():
    #Ввод x и n. Условно контроллер.
    x = float(input("Введите x: "))
    n = int(input("Введите n: "))
    return x, n

def maclaurin_series_exp():
    #1.______Разложение экспоненты в ряд Маклорена______. Контроллер
    show_title("Разложение экспоненты в ряд Маклорена")
    x, n = input_x_and_n()
    res = calculations_maclaurin_series_exp(x, n)
    show_res(res, "Ответ")

def maclaurin_series_cos():
    #2.______Разложение косинуса в ряд Маклорена______. Контроллер
    show_title("Разложение косинуса в ряд Маклорена")
    x, n = input_x_and_n()
    res = calculations_maclaurin_series_cos(x, n)
    show_res(res, "Ответ")

def maclaurin_series_sin():
    #3.______Разложение синуса в ряд Маклорена______. Контроллер
    show_title("Разложение синуса в ряд Маклорена")
    x, n = input_x_and_n()
    res = calculations_maclaurin_series_sin(x, n)
    show_res(res, "Ответ")

def maclaurin_series_arcsin():
    #4.______Разложение арксинуса в ряд Маклорена______. Контроллер
    show_title("Разложение арксинуса в ряд Маклорена")
    x, n = input_x_and_n()
    res = calculations_maclaurin_series_arcsin(x, n)
    show_res(res, "Ответ")

def maclaurin_series_arccos():
    #5.______Разложение арккосинуса в ряд Маклорена______. Контроллер
    show_title("Разложение арккосинуса в ряд Маклорена")
    x, n = input_x_and_n()
    res = calculations_maclaurin_series_arccos(x, n)
    show_res(res, "Ответ")

def get_actions():
    # Получение доступных действий
    return [maclaurin_series_exp, maclaurin_series_cos, maclaurin_series_sin, maclaurin_series_arcsin, maclaurin_series_arccos]