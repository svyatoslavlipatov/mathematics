def get_coord1_and_coord2(coord):
    # Получение x1, x2 и y1, y2. Вычисление
    coord1 = coord[0]
    coord2 = coord[1]
    return coord1, coord2

def get_x_and_y(matrix):
    # Получение значений из матрицы. Вычисление
    x = []
    y = []
    for i in range(len(matrix)):
        x.append(matrix[i][0])
        y.append(matrix[i][1])
    return x, y

def calculation_linear_interpolation(x, y, xp):
    #Вычисление линейной интерполяции. Вычисление
    x1, x2 = get_coord1_and_coord2(x)
    y1, y2 = get_coord1_and_coord2(y)
    y = y1 + ((xp - x1) * (y2 - y1) / (x2 - x1))
    return y

def calculation_piecewise_linear_interpolation(x, y, xp):
    #Вычисление кусочно-линейной интерполяции. Вычисление
    index = -1
    yp = []
    for z in xp:
        for i in range(1, len(x)):
            if z <= x[i]:
                index = i-1
                break
            else:
                i += 1
        piecewise = (z-x[index+1])*y[index]/((x[index]-x[index+1])) + (z-x[index])*y[index+1]/((x[index+1]-x[index]))
        yp.append(piecewise)
    return yp

def calculation_lagrange_polynomial(x, y, xp):
    #Вычисление методом полинома Лагранжа. Вычисление
    yp = 0
    for i in range(len(x)):
        p = 1
        for j in range(len(x)):
            if j != i:
                p *= (xp - x[j]) / (x[i] - x[j])
        yp += y[i] * p
    return yp
