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
        res = ("Векторы коллинеарные")
        return res
    else:
        res = ("Векторы не коллинеарные")
        return res

def collin(a, b):
    # Проверка ненулевых векторов. Вычисление
    res = [i * a[0] / b[0] for i in a]
    return res

def chk_codirectional(a, b, res):
    # Проверка на сонаправленность. Вычисление
    if res == b:
        if sum(list(map(lambda x, y: x * y, a, b))) > 0:
            res = ("Векторы сонаправленные")
            return res
        else:
            res = ("Векторы не сонаправленные")
            return res
    else:
        res = ("Векторы не сонаправленные")
        return res


def chk_contradirectional(a, b, res):
    # Проверка на направленность. Вычисление
    if res == b:
        if sum(list(map(lambda x, y: x * y, a, b))) < 0:
            res = "Векторы противоположно направленные"
            return res
        else:
            res = "Векторы не противоположно направленные"
            return res
    else:
        res = "Векторы не противоположно направленные"
        return res


def chk_equality(a, b):
    # Проверка равенства векторов. Вычисление
    if a == b:
        res = "Векторы равны"
        return res

    else:
        res = "Векторы не равны"
        return res



def chk_equality_with_precision(res):
    # Проверка равенства векторов с заданной точностью. Вычисление
    c = 0
    for i in res:
        if abs(i) < 0.000001:
            c = c + 1
    if c == len(res):
        res = "Векторы равны"
        return res
    else:
        res = "Векторы не равны"
        return res


def chk_orthogonality(res):
    # Проверка на ортогональность. Вычисление
    if res == 0:
        res = "Векторы ортогональны"
        return res
    else:
        res = "Векторы не ортогональны"
        return res


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
    skalyar = sum(list(map(lambda x, y: x * y, a, b)))
    akv = sum([i * i for i in a]) ** 0.5
    bkv = sum([i * i for i in b]) ** 0.5
    res = (skalyar) / (akv * bkv)
    return res


def comparison_of_angles(cosinus):
    # Сравнение углов. Вычисление
    if cosinus == 0:
        res = "Угол между векторами прямой"
        return res
    elif cosinus > 0:
        res = "Угол между векторами острый"
        return res
    elif cosinus < 0:
        res = "Угол между векторами тупой"
        return res