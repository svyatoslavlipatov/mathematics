import maclaurin_calculations as mcl

def test_maclaurin_series_exp_first():
    x, n = 2, 0
    res = mcl.calculations_maclaurin_series_exp(x, n)
    exp = 1.0
    assert res == exp

def test_maclaurin_series_exp_second():
    x, n = 2, 5
    res = mcl.calculations_maclaurin_series_exp(x, n)
    exp = 7.266666666666667
    assert res == exp
    
def test_maclaurin_series_exp_third():
    x, n = 2, 2
    res = mcl.calculations_maclaurin_series_exp(x, n)
    exp = 5.0
    assert res == exp

def test_maclaurin_series_cos():
    x, n = 1.5, 5
    res = mcl.calculations_maclaurin_series_cos(x, n)
    exp = 0.07073693411690848
    assert res == exp

def test_maclaurin_series_sin_first():
    x, n = 1, 2
    res = mcl.calculations_maclaurin_series_sin(x, n)
    exp = 0.8416666666666667
    assert res == exp

def test_maclaurin_series_sin_second():
    x, n = 1.5, 5
    res = mcl.calculations_maclaurin_series_sin(x, n)
    exp =  0.9974949556821353
    assert res == exp

def test_maclaurin_series_arcsin_first():
    x, n = 1, 0
    res = mcl.calculations_maclaurin_series_arcsin(x, n)
    exp = 1.0
    assert res == exp

def test_maclaurin_series_arcsin_second():
    x, n = 1, 3
    res = mcl.calculations_maclaurin_series_arcsin(x, n)
    exp = 1.286309523809524
    assert res == exp

def test_maclaurin_series_arccos_first():
    x, n = 1, 0
    res = mcl.calculations_maclaurin_series_arccos(x, n)
    exp = 0.5707963267948966
    assert res == exp

def test_maclaurin_series_arccos_second():
    x, n = 1, 2
    res = mcl.calculations_maclaurin_series_arccos(x, n)
    exp = 0.32912966012822986
    assert res == exp