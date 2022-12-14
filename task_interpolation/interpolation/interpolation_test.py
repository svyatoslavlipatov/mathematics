import interpolation_calculations as inter

def test_linear_interpolation():
    matrix =  [[2, 5], [6, 9]]
    x, y = inter.get_x_and_y(matrix)
    xp = 4
    res = inter.calculation_linear_interpolation(x, y, xp)
    exp = 7.0
    assert res == exp


def test_piecewise_linear_interpolation():
    matrix = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    x, y = inter.get_x_and_y(matrix)
    xp = [-1.5, 3, 2, 5, 9]
    res = inter.calculation_piecewise_linear_interpolation(x, y, xp)
    exp = [-0.5, 4.0, 3.0, 5.4, 11.8]
    assert res == exp


def test_lagrange_polynomial():
    matrix = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    x, y = inter.get_x_and_y(matrix)
    xp = 4
    res = inter.calculation_lagrange_polynomial(x, y, xp)
    exp = 2.12
    assert res == exp