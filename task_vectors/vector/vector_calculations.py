import math 

def summa(a, b):
    # Сумма векторов. Вычисление
    res = list(map(lambda x, y: x + y, a, b))
    return res


def sub(a, b):
    # Разность векторов. Вычисление
    res = list(map(lambda x, y: x - y, a, b))
    return res


def multiply_scalar(a, sc):
    # Произведение вектора на скаляр. Вычисление
    res = [i * sc for i in a]
    return res


def division_scalar(a, sc):
    # Частное вектора на скаляр. Вычисление
    res = [i / sc for i in a]
    return res


def multiplication_vectors(a, b):
    # Произведение векторов. Вычисление
    res = sum(list(map(lambda x, y: x * y, a, b)))
    return res


def chk_collinear(b, coll):
    # Проверка на коллинеарность. Вычисление
    if coll == b:
        print(coll)
        return True
    else:
        return False

def collin(a, b):
    # Условие для коллинеарности. Вычисление
    res = [i * (b[0] / a[0]) for i in a]
    return res

def chk_codirectional(a, b, res):
    # Проверка на сонаправленность. Вычисление
    if res == b:
        if sum(list(map(lambda x, y: x * y, a, b))) > 0:
            return True
        else:
            return False
    else:
        return False


def chk_contradirectional(a, b, res):
    # Проверка на направленность. Вычисление
    if res == b:
        if sum(list(map(lambda x, y: x * y, a, b))) < 0:
            return True
        else:
            return False
    else:
        return False


def chk_equality(a, b):
    # Проверка равенства векторов. Вычисление
    if a == b:
        return True
    else:
        return False



def chk_equality_with_precision(res):
    # Проверка равенства векторов с заданной точностью. Вычисление
    c = 0
    for i in res:
        if abs(i) < 0.000001:
            c = c + 1
    if c == len(res):
        return True
    else:
        return False


def chk_orthogonality(res):
    # Проверка на ортогональность. Вычисление
    if res == 0:
        return True
    else:
        return False


def vector_length(a):
    # Вычисление длины вектора. Вычисление
    res = sum([i * i for i in a]) ** 0.5
    return res


def vector_rationing(a, l):
    # Вычисление нормировки. Вычисление
    res = [i / l for i in a]
    return res


def change_to_the_opposite(a):
    # Изменение на противоположный вектор. Вычисление
    res = [i * -1 for i in a]
    return res


def vector_projection(a, b):
    # Вычисление проекции на вектор. Вычисление
    res = sum(list(map(lambda x, y: x * y, a, b))) / sum([i * i for i in b]) ** 0.5
    return res

def search_for_the_cosine(a, b):
    # Нахождение косинуса. Вычисление
    skalyar = multiplication_vectors(a, b)
    akv = vector_length(a)
    bkv = vector_length(b)
    res = skalyar / (akv * bkv)
    return res


def comparison_of_angles(cosinus):
    return math.degrees(math.acos(cosinus))