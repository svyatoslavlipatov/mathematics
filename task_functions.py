#_____1.Сложение векторов_____
def sum_of_vectors():
    print("1.Сложение векторов")
    m1 = input("Введите первый массив через запятую: ")
    m2 = input("Введите второй массив через запятую: ")
    massiv1 = m1.split(',')
    massiv2 = m2.split(',')
    a = [int(x) for x in massiv1]
    b = [int(x) for x in massiv2]
    res = list(map(lambda x, y: x + y, a, b))
    print(f"Сумма векторов: {res}")

#_____2.Вычитание векторов_____
def subtracting_vectors():
    print("2.Вычитание векторов")
    m1 = input("Введите первый массив через запятую: ")
    m2 = input("Введите второй массив через запятую: ")
    massiv1 = m1.split(',')
    massiv2 = m2.split(',')
    a = [int(x) for x in massiv1]
    b = [int(x) for x in massiv2]
    res = list(map(lambda x, y: x - y, a, b))
    print(f"Разность векторов: {res}")

#_____3.Умножение, деление вектора на скаляр_____
def multiply_or_division_on_scalar():
    print("3.Умножение, деление вектора на скаляр")
    m1 = input("Введите массив через запятую: ")
    s1 = int(input("Введите скаляр: "))
    op = input("Введите оператор (* или /): ")
    massiv1 = m1.split(',')
    a = [int(x) for x in massiv1]
    if op == "*":
        res = [i * s1 for i in a]
        print(f"Произведение вектора на скаляр: {res}")
    elif op == "/": 
        res = [i / s1 for i in a]
        print(f"Деление вектора на скаляр: {res}")

#_____4.Скалярное произведение векторов_____
def scalar_multiplication_of_vectors():
    print("4.Скалярное произведение векторов")
    m1 = input("Введите первый массив через запятую: ")
    m2 = input("Введите второй массив через запятую: ")
    massiv1 = m1.split(',')
    massiv2 = m2.split(',')
    a = [int(x) for x in massiv1]
    b = [int(x) for x in massiv2]
    res = list(map(lambda x, y: x * y, a, b))
    res_sum = sum(res)
    print(f"Скалярное произведение векторов: {res_sum}")

#_____5.Коллинеарные векторы_____
def collinear_vectors():
    print("5.Коллинеарные векторы")
    m1 = input("Введите первый массив через запятую: ")
    m2 = input("Введите второй массив через запятую: ")
    massiv1 = m1.split(',')
    massiv2 = m2.split(',')
    a = [int(x) for x in massiv1]
    b = [int(x) for x in massiv2]
    a1 = a[0]
    b1 = b[0]
    n = b1/a1
    res = [i * n for i in a]
    if res == b:
        print("Векторы коллинеарные")
    else:
        print("Векторы не коллинеарные")

#_____6.Сонаправленные векторы_____
def codirectional_vectors():
    print("6.Сонаправленные векторы")
    m1 = input("Введите первый массив через запятую: ")
    m2 = input("Введите второй массив через запятую: ")
    massiv1 = m1.split(',')
    massiv2 = m2.split(',')
    a = [int(x) for x in massiv1]
    b = [int(x) for x in massiv2]
    a1 = a[0]
    b1 = b[0]
    n = b1/a1
    res = [i * n for i in a]
    if res == b:
        if sum(list(map(lambda x, y: x * y, a, b))) > 0:
            print("Векторы сонаправленные")
        else:
            print("Векторы не сонаправленные")
    else:
        print("Векторы не сонаправленные")

#_____7.Противоположнонаправленные вектора_____
def contradirectional_vectors():
    print("7.Противоположно направленные векторы")
    m1 = input("Введите первый массив через запятую: ")
    m2 = input("Введите второй массив через запятую: ")
    massiv1 = m1.split(',')
    massiv2 = m2.split(',')
    a = [int(x) for x in massiv1]
    b = [int(x) for x in massiv2]
    a1 = a[0]
    b1 = b[0]
    n = b1/a1
    res = [i * n for i in a]
    if res == b:
        if sum(list(map(lambda x, y: x * y, a, b))) < 0:
            print("Векторы противоположно направленные")
        else:
            print("Векторы не противоположно направленные")
    else:
        print("Векторы не противоположно направленные")

#_____8.Равенство векторов_____
def equality():
    print("8.Равенство векторов")
    m1 = input("Введите первый массив через запятую: ")
    m2 = input("Введите второй массив через запятую: ")
    massiv1 = m1.split(',')
    massiv2 = m2.split(',')
    a = [int(x) for x in massiv1]
    b = [int(x) for x in massiv2]
    if a == b:
        print(f"Векторы {a} и {b} равны")
    else:
        print("Векторы не равны")

#_____9.Равенство векторов с заданной точностью_____
def equality_with_a_given_precision():
    print("9.Равенство векторов с заданной точностью")
    m1 = input("Введите первый массив через запятую: ")
    m2 = input("Введите второй массив через запятую: ")
    massiv1 = m1.split(',')
    massiv2 = m2.split(',')
    a = [int(x) for x in massiv1]
    b = [int(x) for x in massiv2]
    eps = 0.000001
    res = list(map(lambda x, y: x - y, a, b))
    c = 0
    for i in res:
        if abs(i) < eps:
            c = c+1
    if c == len(res):
        print("Векторы равны")
    else:
        print("Векторы не равны")

#_____10.Ортогональность векторов_____
def orthogonality():
    print("10.Равенство векторов")
    m1 = input("Введите первый массив через запятую: ")
    m2 = input("Введите второй массив через запятую: ")
    massiv1 = m1.split(',')
    massiv2 = m2.split(',')
    a = [int(x) for x in massiv1]
    b = [int(x) for x in massiv2]
    res = list(map(lambda x, y: x * y, a, b))
    res_sum = sum(res)
    if res_sum == 0:
        print(f"Скалярное произведение векторов равно нулю. Векторы ортогональны")
    else:
        print(f"Скалярное произведение векторов: {res_sum} ≠ 0. Векторы не ортогональны")

#_____11.Длина вектора_____
def length():
    print("11.Длина вектора")
    m1 = input("Введите первый массив через запятую: ")
    massiv1 = m1.split(',')
    a = [int(x) for x in massiv1]
    l = sum([i * i for i in a]) ** 0.5
    print(l)

#_____12.Нормировка вектора_____
def normirovka():
    print("12.Нормировка вектора")
    m1 = input("Введите первый массив через запятую: ")
    massiv1 = m1.split(',')
    a = [int(x) for x in massiv1]
    l = sum([i * i for i in a]) ** 0.5
    norm = [i / l for i in a]
    print(f"Нормировка вектора: {norm}")

#_____13.Изменение направления вектора на противоположный_____
def protivop():
    print("13.Изменение направления вектора на противоположный")
    m1 = input("Введите первый массив через запятую: ")
    massiv1 = m1.split(',')
    a = [int(x) for x in massiv1]
    pr = [i * -1 for i in a]
    print(f"Измененное направление вектора {pr}")

#_____14.Угол между векторами_____
def angle():
    print("14.Угол между векторами")
    m1 = input("Введите первый массив через запятую: ")
    m2 = input("Введите второй массив через запятую: ")
    massiv1 = m1.split(',')
    massiv2 = m2.split(',')
    a = [int(x) for x in massiv1]
    b = [int(x) for x in massiv2]
    skalyar = sum(list(map(lambda x, y: x * y, a, b)))
    akv = sum([i * i for i in a]) ** 0.5
    bkv = sum([i * i for i in b]) ** 0.5
    cosinus = (skalyar) / (akv * bkv)
    print(f"Угол между векторами: cos α = {cosinus}")

#_____15.Проекция вектора на вектор_____
def projection():
    print("15.Проекция вектора на вектор")
    m1 = input("Введите первый массив через запятую: ")
    m2 = input("Введите второй массив через запятую: ")
    massiv1 = m1.split(',')
    massiv2 = m2.split(',')
    a = [int(x) for x in massiv1]
    b = [int(x) for x in massiv2]
    skalyar = sum(list(map(lambda x, y: x * y, a, b)))
    bkv = sum([i * i for i in b]) ** 0.5
    pr_a_on_b = skalyar / bkv
    print(f"Проекция вектора на вектор равна {pr_a_on_b}")

#_____16.Косинус между векторами_____
def cosine():
    print("16.Косинус между векторами")
    m1 = input("Введите первый массив через запятую: ")
    m2 = input("Введите второй массив через запятую: ")
    massiv1 = m1.split(',')
    massiv2 = m2.split(',')
    a = [int(x) for x in massiv1]
    b = [int(x) for x in massiv2]
    skalyar = sum(list(map(lambda x, y: x * y, a, b)))
    akv = sum([i * i for i in a]) ** 0.5
    bkv = sum([i * i for i in b]) ** 0.5
    cosinus = (skalyar) / (akv * bkv)
    if cosinus == 0:
        print(f"Угол между векторами прямой")
    elif cosinus > 0:
        print(f"Угол между векторами острый")
    elif cosinus < 0:
        print(f"Угол между векторами тупой")