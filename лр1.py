import math
import sys


def get_coef(x):
    while True:
        s = input(x)
        try:
            return float(s)
        except ValueError:
            print("Некорректное значение, повторите ввод:")


def get_roots(a, b, c):
    roots = []

    if a == 0:
        if b == 0:
            return []
        t = -c / b
        if t > 0:
            roots.append(math.sqrt(t))
            roots.append(-math.sqrt(t))
        elif t == 0:
            roots.append(0)
        return roots

    D = b*b - 4*a*c
    if D > 0:
        t1 = (-b + math.sqrt(D)) / (2*a)
        t2 = (-b - math.sqrt(D)) / (2*a)
        for t in (t1, t2):
            if t > 0:
                roots.append(math.sqrt(t))
                roots.append(-math.sqrt(t))
            elif t == 0:
                roots.append(0)
    elif D == 0:
        t = -b / (2*a)
        if t > 0:
            roots.append(math.sqrt(t))
            roots.append(-math.sqrt(t))
        elif t == 0:
            roots.append(0)
    return roots


def get_coefs_from_term():
    args = sys.argv[1:]
    coefs = [None, None, None]

    for i in range(min(3, len(args))):
        try:
            coefs[i] = float(args[i])
        except ValueError:
            if i == 0:
                name = "A"
            elif i == 1:
                name = "B"
            else:
                name = "C"
            print(f"Некорректный аргумент {name}: {args[i]}. "
                  f"Значение будет введено с клавиатуры.")
            coefs[i] = None
    return coefs


def main():
    coefs = get_coefs_from_term()

    if coefs[0] is None:
        coefs[0] = get_coef("Введите A:")
    if coefs[1] is None:
        coefs[1] = get_coef("Введите B:")
    if coefs[2] is None:
        coefs[2] = get_coef("Введите C:")

    a, b, c = coefs
    roots = get_roots(a, b, c)

    roots.sort()

    n = len(roots)
    if n == 0:
        print("Действительных корней нет")
    else:
        print(f"Найдено действительных корней: {n}")
        if n >= 1:
            print(f"  x1 = {roots[0]}")
        if n >= 2:
            print(f"  x2 = {roots[1]}")
        if n >= 3:
            print(f"  x3 = {roots[2]}")
        if n >= 4:
            print(f"  x4 = {roots[3]}")


main()