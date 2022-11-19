import vector_calculations as vec


def test_summa():
    a = [1, 2, 5]
    b = [4, 8, 1]
    exp = [5, 10, 6]
    res = vec.summa(a, b)
    assert res == exp


def test_sub():
    a = [1, 2, 5]
    b = [4, 8, 1]
    exp = [-3, -6, 4]
    res = vec.sub(a, b)
    assert res == exp

def test_multiply_scalar():
    a = [1, 2, 5]
    sc = 2
    exp = [2, 4, 10]
    res = vec.multiply_scalar(a, sc)
    assert res == exp

def test_division_scalar():
    a = [1, 2, 5]
    sc = 2
    exp = [0.5, 1, 2.5]
    res = vec.division_scalar(a, sc)
    assert res == exp

def test_multiplication_vectors():
    a = [1, 2, 5]
    b = [5, 4, 7]
    exp = 48
    res = vec.multiplication_vectors(a, b)
    assert res == 48

def test_chk_collinear():
    a = [1, 2, 5]
    b = [1, 2, 5]
    coll = vec.collin(a, b)
    res = vec.chk_collinear(b, coll)
    assert res == True

def test_chk_codirectional():
    a = [1, 2, 5]
    b = [1, 2, 5]
    coll = vec.collin(a, b)
    res = vec.chk_codirectional(a, b, coll)
    assert res == True

def test_chk_contradirectional():
    a = [1, 4, 7]
    b = [-1, -4, -7]
    coll = vec.collin(a, b)
    res = vec.chk_contradirectional(a, b, coll)
    assert res == True

def test_chk_equality():
    a = [1, 4, 7]
    b = [1, 4, 7]
    res = vec.chk_equality(a, b)
    assert res == True

def test_chk_equality_with_precision():
    a = [1, 4, 7]
    b = [1, 4, 7]
    subt = vec.sub(a, b)
    res = vec.chk_equality_with_precision(subt)
    assert res == True

def test_chk_orthogonality():
    a = [2, 4]
    b = [-2, 1]
    mlt = vec.multiplication_vectors(a, b)
    res = vec.chk_orthogonality(mlt)
    assert res == True

def test_vector_length():
    a = [2,5,7]
    res = vec.vector_length(a)
    exp = 8.831760866327848
    assert res == exp

def test_vector_rationing():
    a = [5, 4, 7]
    l = vec.vector_length(a)
    res = vec.vector_rationing(a, l)
    exp = [0.5270462766947299, 0.4216370213557839, 0.7378647873726218]
    assert res == exp

def test_change_to_the_opposite():
    a = [5, 4, 7]
    res = vec.change_to_the_opposite(a)
    exp = [-5, -4, -7]
    assert res == exp

def test_comparison_of_angles():
    a = [2, 2, 5]
    b = [5, 4, 7]
    cos = vec.search_for_the_cosine(a, b)
    res = vec.comparison_of_angles(cos)
    exp = 13.463609704775655
    assert res == exp

def test_vector_projection():
    a = [2, 2, 5]
    b = [5, 4, 7]
    res = vec.vector_projection(a, b)
    exp = 5.586690532964137
    assert res == exp

def test_search_for_the_cosine():
    a = [2, 2, 5]
    b = [5, 4, 7]
    res = vec.search_for_the_cosine(a, b)
    exp = 0.9725179925282852
    assert res == exp
