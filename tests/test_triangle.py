import unittest
import triangle


class TestTriangle(unittest.TestCase):
    def test_area_valid(self):
        # Arrange
        a = 3
        b = 4
        c = 5
        expected_result = 6

        # Act
        result = triangle.area(a, b, c)

        # Assert
        self.assertEqual(result, expected_result)

    def test_perimeter_valid(self):
        # Arrange
        a = 3
        b = 4
        c = 5
        expected_result = 12

        # Act
        result = triangle.perimeter(a, b, c)

        # Assert
        self.assertEqual(result, expected_result)

    def test_area_zero_sides(self):
        # Arrange
        a = 0
        b = 0
        c = 0

        # Act & Assert
        with self.assertRaises(ValueError):
            triangle.area(a, b, c)

    def test_perimeter_zero_sides(self):
        # Arrange
        a = 0
        b = 0
        c = 0

        # Act & Assert
        with self.assertRaises(ValueError):
            triangle.perimeter(a, b, c)

    def test_area_invalid_triangle(self):
        # Arrange
        a = 1
        b = 2
        c = 4

        # Act & Assert
        with self.assertRaises(ValueError):
            triangle.area(a, b, c)

    def test_perimeter_negative_side(self):
        # Arrange
        a = 3
        b = -4
        c = 5

        # Act & Assert
        with self.assertRaises(ValueError):
            triangle.perimeter(a, b, c)

    def test_area_negative_side(self):
        # Arrange
        a = 3
        b = -4
        c = 5

        # Act & Assert
        with self.assertRaises(ValueError):
            triangle.area(a, b, c)

    def test_perimeter_invalid_triangle(self):
        # Arrange
        a = 1
        b = 2
        c = 4

        # Act & Assert
        with self.assertRaises(ValueError):
            triangle.perimeter(a, b, c)
