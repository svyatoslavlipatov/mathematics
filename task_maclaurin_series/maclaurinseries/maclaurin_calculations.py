import math

def calculations_maclaurin_series_exp(x, n):
    #Разложение экспоненты. Вычисление
    res = 0
    for h in range(0, n + 1):
        res += (x**h) / math.factorial(h)
    return res

def calculations_maclaurin_series_cos(x, n):
    #Разложение косинуса. Вычисление
    res = 0
    for h in range(0, n + 1): 
        res += (((-1)**h) / math.factorial(2*h)) * (x ** (2 * h))
    return res

def calculations_maclaurin_series_sin(x, n):
    #Разложение синуса. Вычисление
    res = 0 
    for h in range(0, n + 1):
        res += (((-1) ** h) / math.factorial(2*h + 1)) * (x ** (2*h + 1))
    return res

def calculations_maclaurin_series_arcsin(x, n):
    #Разложение арксинуса. Вычисление
    res = 0
    for h in range(0, n + 1):
        res += ((math.factorial(2*h)) / (4**h * (math.factorial(h)**2) * (2*h + 1))) * (x**(2*h + 1))
    return res

def calculations_maclaurin_series_arccos(x, n):
    #Разложение арккосинуса. Вычисление
    res = (math.pi / 2) - (calculations_maclaurin_series_arcsin(x,n))
    return res
