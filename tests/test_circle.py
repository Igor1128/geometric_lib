import unittest
import circle
import math


class TestCircle(unittest.TestCase):
    def test_area_valid(self):
        # Arrange
        radius = 5
        expected_result = math.pi * radius * radius

        # Act
        result = circle.area(radius)

        # Assert
        self.assertEqual(result, expected_result)

    def test_perimeter_valid(self):
        # Arrange
        radius = 5
        expected_result = 2 * math.pi * radius

        # Act
        result = circle.perimeter(radius)

        # Assert
        self.assertEqual(result, expected_result)

    def test_area_zero_radius(self):
        # Arrange
        radius = 0
        expected_result = 0

        # Act
        result = circle.area(radius)

        # Assert
        self.assertEqual(result, expected_result)

    def test_perimeter_zero_radius(self):
        # Arrange
        radius = 0
        expected_result = 0

        # Act
        result = circle.perimeter(radius)

        # Assert
        self.assertEqual(result, expected_result)

    def test_area_negative_radius(self):
        # Arrange
        radius = -5

        # Act & Assert
        with self.assertRaises(ValueError):
            circle.area(radius)

    def test_perimeter_negative_radius(self):
        # Arrange
        radius = -5

        # Act & Assert
        with self.assertRaises(ValueError):
            circle.perimeter(radius)

    def test_perimeter_invalid_circle(self):
        # Arrange
        radius = -5

        # Act & Assert
        with self.assertRaises(ValueError):
            circle.perimeter(radius)

    def test_area_invalid_circle(self):
        # Arrange
        radius = -5

        # Act & Assert
        with self.assertRaises(ValueError):
            circle.area(radius)
