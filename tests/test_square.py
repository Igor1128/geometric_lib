import unittest
import square


class TestSquare(unittest.TestCase):
    def test_area_valid(self):
        # Arrange
        side = 5
        expected_result = side * side

        # Act
        result = square.area(side)

        # Assert
        self.assertEqual(result, expected_result)

    def test_perimeter_valid(self):
        # Arrange
        side = 5
        expected_result = 4 * side

        # Act
        result = square.perimeter(side)

        # Assert
        self.assertEqual(result, expected_result)

    def test_area_zero_side(self):
        # Arrange
        side = 0
        expected_result = 0

        # Act
        result = square.area(side)

        # Assert
        self.assertEqual(result, expected_result)

    def test_perimeter_zero_side(self):
        # Arrange
        side = 0
        expected_result = 0

        # Act
        result = square.perimeter(side)

        # Assert
        self.assertEqual(result, expected_result)

    def test_area_negative_side(self):
        # Arrange
        side = -5

        # Act & Assert
        with self.assertRaises(ValueError):
            square.area(side)

    def test_perimeter_negative_side(self):
        # Arrange
        side = -5

        # Act & Assert
        with self.assertRaises(ValueError):
            square.perimeter(side)

    def test_perimeter_invalid_square(self):
        # Arrange
        side = -5

        # Act & Assert
        with self.assertRaises(ValueError):
            square.perimeter(side)

    def test_area_invalid_square(self):
        # Arrange
        side = -5

        # Act & Assert
        with self.assertRaises(ValueError):
            square.area(side)
