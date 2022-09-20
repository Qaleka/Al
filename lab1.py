import sys
import math


def get_coef(index, prompt):

    try:
        coef_str = sys.argv[index]
        n = int(coef_str)
    except:
        print("Неправильный ввод параметров, либо их отсутствие.")
        while True:
            print(prompt)
            coef_str = input()
            try:
                n=int(coef_str)
                break
            except:
                print("Неправильный ввод данных")
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        if root < 0:
            return result
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1 < 0:
            if root2 < 0:
                return result
            else:
                root2 = math.sqrt(root2)
                result.append(root2)
                result.append(-root2)
        else:
            if root2 < 0:
                root1 = math.sqrt(root1)
                result.append(root1)
                result.append(-root1)
            else:
                root1 = math.sqrt(root1)
                result.append(root1)
                result.append(-root1)
                root2 = math.sqrt(root2)
                result.append(root2)
                result.append(-root2)
    return result


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    roots = get_roots(a, b, c)

    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {} и {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {} и {} и {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
