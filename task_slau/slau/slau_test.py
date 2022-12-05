import slau_calculations as sl

def test_2d_slau():
    matrix = [[2, 3],[4, 3]]
    right_side = [2, 7]
    res = sl.gauss_jordan_method(matrix, right_side)
    exp = [2.5, -1.0]
    assert res == exp

def test_3d_slau():
    matrix = [[-1, 2, 6], [3, -6, 0], [1, 0, 6]]
    right_side = [15, -9, 5]
    res = sl.gauss_jordan_method(matrix, right_side)
    exp = [-7.0, -2.0, 2.0]    
    assert res == exp

def test_4d_slau():
    matrix = [[3, 1, 2, 5], [3, 1, 0, 2], [6, 4, 11, 11], [-3, -2, -2, -10]]
    right_side = [-6, -10, -27, 1]
    res = sl.gauss_jordan_method(matrix, right_side)
    exp = [-3.0, -5.0, -1.0, 2.0]    
    assert res == exp