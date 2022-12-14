import approximation_calculations as apr

def test_least_squares_method():
    left_side = [[2, 3], [3, 3], [4, 7]]
    right_side = [[7],[7],[3]]
    res = apr.calculation_least_squares_method(left_side, right_side)
    exp = [4.680851063829789, -2.063829787234044]
    assert res == exp

def test_linear_approximation_first():
    matrix = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    some_x = [4]
    res = apr.calculation_linear_approximation(matrix, some_x)
    exp = [[4, 4.615763546798029]]
    assert res == exp

def test_linear_approximation_second():
    matrix = [[1, 2], [3, 4], [3.5, 3], [6, 7]]
    some_x = [1, 3, 5]
    res = apr.calculation_linear_approximation(matrix, some_x)
    exp =  [[1, 1.660098522167488], [3, 3.6305418719211824], [5, 5.600985221674877]]
    assert res == exp

def test_polinom_approximation_2nd_degree():
    right_side = [[0.13], [0.07], [1.89]]
    x_value =  [1, 3, 5]
    res = apr.calculate_polinom_approximation(right_side, x_value)
    exp = [[1, 2.09], [3, 3.2699999999999996], [5, 5.49]]
    assert res == exp

def test_polinom_approximation_3rd_degree():
    right_side = [[0.48], [-4.8], [13.96], [-7.64]]
    x_value =  [1, 3, 5]
    res = apr.calculate_polinom_approximation(right_side, x_value)
    exp = [[1, 2.000000000000001], [3, 4.000000000000008], [5, 2.1600000000000117]]
    assert res == exp