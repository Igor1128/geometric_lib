def area(a):
    """Вычисляет площадь квадрата."""
    if a < 0:
        raise ValueError("Invalid square side")
    return a * a


def perimeter(a):
    """Вычисляет периметр квадрата."""
    if a < 0:
        raise ValueError("Invalid square side")
    return 4 * a
