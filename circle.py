import math


def area(radius):
    """Вычисляет площадь круга."""
    if radius < 0:
        raise ValueError("Invalid circle radius")
    return math.pi * radius * radius


def perimeter(radius):
    """Вычисляет периметр круга."""
    if radius < 0:
        raise ValueError("Invalid circle radius")
    return 2 * math.pi * radius
