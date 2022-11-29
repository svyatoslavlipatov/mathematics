from vector.vector_output import show_title, show_res
from vector.vector_calculations import summa, sub, multiply_scalar, division_scalar, multiplication_vectors, chk_collinear, collin, chk_codirectional, chk_contradirectional, chk_equality, chk_equality_with_precision, chk_orthogonality, vector_length, vector_rationing, change_to_the_opposite, vector_projection, search_for_the_cosine, angles
from vector.vector_converter import int_massive

def input_two_arrays():
    #Ввод двух массивов. Условно контроллер
    m1 = input("Введите первый массив через запятую: ")
    a = int_massive(m1)
    m2 = input("Введите второй массив через запятую: ")
    b = int_massive(m2)
    return a,b

def input_one_massive():
    #Ввод одного массива. Условно контроллер
    m1 = input("Введите массив через запятую: ")
    a = int_massive(m1)
    return a

def input_scalar():
    #Ввод скаляра. Условно контроллер
    s = int(input("Введите скаляр: "))
    return s

def sum_of_vectors():
    #_____1.Сложение векторов_____. Контроллер
    show_title('1.Сложение векторов')
    a, b = input_two_arrays()
    res = summa(a, b)
    show_res(res, 'Сумма векторов')


def subtracting_vectors():
    #_____2.Вычитание векторов_____. Контроллер
    show_title('2.Вычитание векторов')
    a, b = input_two_arrays()
    res = sub(a, b)
    show_res(res, 'Разность векторов')


def multiply_on_scalar():
    #_____3.1.Умножение вектора на скаляр_____. Контроллер
    show_title('3.1.Умножение вектора на скаляр')
    a = input_one_massive()
    sc = input_scalar()
    res = multiply_scalar(a, sc)
    show_res(res, 'Произведение вектора на скаляр')


def division_on_scalar():
    #_____3.2.Деление вектора на скаляр_____. Контроллер
    show_title('3.2.Деление вектора на скаляр')
    a = input_one_massive()
    sc = input_scalar()
    res = division_scalar(a, sc)
    show_res(res, 'Деление вектора на скаляр')


def scalar_multiplication_of_vectors():
    # _____4.Скалярное произведение векторов_____. Контроллер
    show_title('4.Скалярное произведение векторов')
    a, b = input_two_arrays()
    res = multiplication_vectors(a, b)
    show_res(res, 'Скалярное произведение векторов')


def collinear_vectors():
    #_____5.Коллинеарные векторы_____. Контроллер
    show_title('5.Коллинеарные векторы')
    a, b = input_two_arrays()
    coll = collin(a, b)
    res = chk_collinear(b, coll)
    show_res(res, 'Ответ')


def codirectional_vectors():
    #_____6.Сонаправленные векторы_____. Контроллер
    show_title('6.Сонаправленные векторы')
    a, b = input_two_arrays()
    coll = collin(a, b)
    res = chk_codirectional(a, b, coll)
    show_res(res, 'Ответ')


def contradirectional_vectors():
    #_____7.Противоположнонаправленные вектора_____. Контроллер
    show_title('7.Противоположно направленные векторы')
    a, b = input_two_arrays()
    coll = collin(a, b)
    res = chk_contradirectional(a, b, coll)
    show_res(res, 'Ответ')

def equality():
    #_____8.Равенство векторов_____. Контроллер
    show_title('8.Равенство векторов')
    a, b = input_two_arrays()
    res = chk_equality(a, b)
    show_res(res, 'Ответ')


def equality_with_a_given_precision():
    #_____9.Равенство векторов с заданной точностью_____. Контроллер
    show_title('9.Равенство векторов с заданной точностью')
    a, b = input_two_arrays()
    subt = sub(a, b)
    res = chk_equality_with_precision(subt)
    show_res(res, 'Ответ')


def orthogonality():
    #_____10.Ортогональность векторов_____. Контроллер
    show_title('10.Равенство векторов')
    a, b = input_two_arrays()
    mlt = multiplication_vectors(a, b)
    res = chk_orthogonality(mlt)
    show_res(res, 'Ответ')
    
def length():
    #_____11.Длина вектора_____. Контроллер
    show_title('11.Длина вектора')
    a = input_one_massive()
    res = vector_length(a)
    show_res(res, 'Длина вектора')

def rationing():
    #_____12.Нормировка вектора_____. Контроллер
    show_title('12.Нормировка вектора')
    a = input_one_massive()
    l = vector_length(a)
    res = vector_rationing(a, l)
    show_res(res, 'Нормировка вектора')

def opposite():
    #_____13.Изменение направления вектора на противоположный_____. Контроллер
    show_title('13.Изменение направления вектора на противоположный')
    a = input_one_massive()
    res = change_to_the_opposite(a)
    show_res(res, 'Измененное направление вектора')


def angle():
    #_____14.Угол между векторами_____. Контроллер
    show_title('14.Угол между векторами')
    a, b = input_two_arrays()
    cos = search_for_the_cosine(a, b)
    res = angles(cos)
    show_res(res, 'Ответ')

def projection():
    #_____15.Проекция вектора на вектор_____. Контроллер
    show_title('15.Проекция вектора на вектор')
    a, b = input_two_arrays()
    res = vector_projection(a, b)
    show_res(res, 'Проекция вектора на вектор равна')

def cosine():
     #_____16.Косинус между векторами_____. Контроллер
    show_title('16.Косинус между векторами')
    a, b = input_two_arrays()
    res = search_for_the_cosine(a, b)
    show_res(res, 'Косинус между векторами (cos α)')


def get_actions():
    # Получение доступных действий
    return [sum_of_vectors, subtracting_vectors, multiply_on_scalar, division_on_scalar, scalar_multiplication_of_vectors, collinear_vectors, codirectional_vectors, contradirectional_vectors, equality, equality_with_a_given_precision, orthogonality, length, rationing, opposite, angle, projection, cosine]
