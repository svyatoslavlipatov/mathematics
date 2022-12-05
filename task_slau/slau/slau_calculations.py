def get_resolve_element(a, k):
    #Получение разрешающего элемента. Вычисление
    resolve_element = a[k][k]
    return resolve_element

def gauss_jordan_method(a,b):
    #Метод Гаусса-Жордана. Вычисление
    n = len(b)
    for k in range(n):
        if abs(a[k][k]) < 1.0e-12:
            for i in range(k+1, n):
                if abs(a[i][k]) > abs(a[k][k]):
                    for j in range(k,n):
                        a[k][j], a[i][j] = a[i][j], a[k][j]
                    b[k], b[i] = b[i], b[k]
                    break
        resolve_element = get_resolve_element(a, k)
        if resolve_element == 0: 
            return False
        else:    
            for j in range(k,n):
                a[k][j] /= resolve_element
            b[k] /= resolve_element
            for i in range(n):
                if i == k or a[i][k] == 0: 
                    continue
                factor = a[i][k]
                for j in range(k,n):
                    a[i][j] -= factor * a[k][j]
                b[i] -= factor * b[k]        
    return b