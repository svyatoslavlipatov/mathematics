import inverse_calculations as inver

def test_search_inverse_matrix():
    matrix = [[1,2],[3,4]]
    unit_matrix = inver.get_unit_matrix(matrix)
    res = inver.inverse(matrix, unit_matrix)
    exp = [[-2.0, 1.0], [1.5, -0.5]]
    assert res == exp

def test_slau_by_inverse_matrix():
    matrix = [[1,2],[3,4]]
    right_side_of_matrix = [[6],[8]]
    unit_matrix = inver.get_unit_matrix(matrix)
    inverse_matrix = inver.inverse(matrix, unit_matrix)
    res = inver.matrix_multiplication(right_side_of_matrix, inverse_matrix)
    exp = [[-4.0], [5.0]]
    assert res == exp