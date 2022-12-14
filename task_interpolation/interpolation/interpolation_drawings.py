from interpolation.interpolation_calculations import calculation_lagrange_polynomial
import matplotlib.pyplot as plt

def show_draw(x, y):
    #Вывод на экран. Визуализация
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()

def draw_linear_interpolation(x, y, xp, yp):
    #Линейная интерполяция. Визуализация
    plt.title("Linear Interpolation")
    plt.scatter(x, y, color='blue')
    plt.scatter(xp, yp, color = "red")
    show_draw(x, y)

def draw_piecewise_linear_interpolation(x, y, xp, yp):
    #Кусочно-линейная интерполяция. Визуализация 
    plt.title("Piecewise Linear Interpolation")
    plt.scatter(x, y, color='blue')
    plt.scatter(xp, yp, color = "orange")
    show_draw(x, y)

def draw_lagrange_polynomial(x, y, xp, yp):
    #Полином Лагранжа. Визуализация 
    plt.title("Lagrange Polynomial")
    plt.scatter(xp, yp, color="orange")
    plt.axis([min(x) - abs(xp) - 5, max(x) + xp + 5, min(y) - abs(yp * 1.5) - 5, max(y) + abs(yp * 1.5)])
    x_new =  []
    min_x = ((min(x) - xp) * 10)
    max_x = ((max(x) + xp) * 10 + 1)
    for i in range(int(min_x), int(max_x)):
        x_new.append(i / 10)
    y_new = []
    for item in x_new:
        a = calculation_lagrange_polynomial(x, y, item)
        y_new.append(a)
    show_draw(x_new, y_new)