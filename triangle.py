import math


def area(a, b, c):
    """Вычисляет площадь треугольника по трем сторонам."""
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle sides")

    # Вычисляем полупериметр
    s = (a + b + c) / 2
    # Вычисляем площадь по формуле Герона
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def perimeter(a, b, c):
    """Вычисляет периметр треугольника по трем сторонам."""
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle sides")
    return a + b + c
