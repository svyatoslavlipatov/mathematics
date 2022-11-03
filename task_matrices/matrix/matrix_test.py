import matrix_calculations as matr

def test_sum_of_matrices():
    mas_1 = [[2,2,5],[1,4,7],[8,5,7]]
    mas_2 = [[1,2,5],[5,4,7],[7,8,7]]
    res = matr.add(mas_1, mas_2)
    exp = [[3, 4, 10], [6, 8, 14], [15, 13, 14]]
    assert res == exp

def test_subtracting_matrices():
    mas_1 = [[2,2,5],[1,4,7],[8,5,7]]
    mas_2 = [[1,2,5],[5,4,7],[7,8,7]]
    res = matr.sub(mas_1, mas_2)
    exp = [[1, 0, 0], [-4, 0, 0], [1, -3, 0]]
    assert res == exp

def test_transposition():
    mas_1 = [[2,2,5],[1,4,7],[8,5,7]]
    res = matr.transp(mas_1)
    exp = [[2, 1, 8], [2, 4, 5], [5, 7, 7]]
    assert res == exp

def test_multiply_on_scalar():
    mas_1 = [[2,4,7],[1,2,5],[8,5,7]]
    s1 = 3
    res = matr.multiplication_matrix_by_scalar(mas_1, s1)
    exp = [[6, 12, 21], [3, 6, 15], [24, 15, 21]]
    assert res == exp

def test_matrix_multiplication():
    mas_1 = [[2,2,5],[1,4,7],[8,5,7]]
    mas_2 = [[1,2,5],[5,4,7],[7,8,7]]
    columns, lines = matr.get_columns_lines(mas_1, mas_2)
    res = matr.multiply_matrices(mas_1, mas_2, columns, lines)
    exp = [[47, 52, 59], [70, 74, 82], [82, 92, 124]]
    assert res == exp

def test_index():
    mas_1 = [[2,4,7],[1,2,5],[8,5,7]]
    ind = 1
    res = matr.get_index(mas_1, ind)
    exp = [1,2,5]
    assert res == exp

def test_index_transp():
    mas_1 = [[2,4,7],[1,2,5],[8,5,7]]
    ind = 1
    res = matr.transp(mas_1)[ind]
    exp = [4,2,5]
    assert res == exp

def test_index_rearranging():
    mas_1 = [[2,4,7],[1,2,5],[8,5,7]]
    ind_1 = 0
    ind_2 = 1
    res = matr.repl_index(mas_1, ind_1, ind_2)
    exp = [[1, 2, 5], [2, 4, 7], [8, 5, 7]]
    assert res == exp

def test_multiply_index_on_scalar():
    mas_1 = [[2,4,7],[1,2,5],[8,5,7]]
    s1 = 3
    ind = 1
    res = matr.multi_string_by_scalar(mas_1, s1, ind)
    exp = [3, 6, 15]
    assert res == exp

def test_adding_multiplied_strings():
    mas_1 = [[2,4,7],[1,2,5],[8,5,7]]
    s1 = 3
    ind_1 = 0
    ind_2 = 1
    multi_ind_1 = matr.multi_string_by_scalar(mas_1, s1, ind_1)
    multi_ind_2 = matr.multi_string_by_scalar(mas_1, s1, ind_2)
    res = matr.summ_lines(multi_ind_1, multi_ind_2)
    exp = [9, 18, 36]
    assert res == exp

def test_subtraction_multiplied_strings():
    mas_1 = [[2,4,7],[1,2,5],[8,5,7]]
    ind_1 = 0
    ind_2 = 1
    s1 = 5
    multi_ind_1 = matr.multi_string_by_scalar(mas_1, s1, ind_1)
    multi_ind_2 = matr.multi_string_by_scalar(mas_1, s1, ind_2)
    res = matr.sub_lines(multi_ind_1, multi_ind_2)
    exp = [5, 10, 10]
    assert res == exp