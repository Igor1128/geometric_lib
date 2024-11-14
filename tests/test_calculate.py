import unittest
import calculate


class TestCalculate(unittest.TestCase):
    def test_calc_circle_area_valid(self):
        # Arrange
        fig = "circle"
        func = "area"
        size = [5]
        expected_result = 78.53981633974483

        # Act
        result = calculate.calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_calc_square_perimeter_valid(self):
        # Arrange
        fig = "square"
        func = "perimeter"
        size = [4]
        expected_result = 16

        # Act
        result = calculate.calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_calc_triangle_perimeter_valid(self):
        # Arrange
        fig = "triangle"
        func = "perimeter"
        size = [3, 4, 5]
        expected_result = 12

        # Act
        result = calculate.calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_calc_circle_perimeter_valid(self):
        # Arrange
        fig = "circle"
        func = "perimeter"
        size = [5]
        expected_result = 31.41592653589793

        # Act
        result = calculate.calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_calc_square_area_valid(self):
        # Arrange
        fig = "square"
        func = "area"
        size = [4]
        expected_result = 16

        # Act
        result = calculate.calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_calc_triangle_area_valid(self):
        # Arrange
        fig = "triangle"
        func = "area"
        size = [3, 4, 5]
        expected_result = 6

        # Act
        result = calculate.calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_calc_invalid_figure(self):
        # Arrange
        fig = "rectangle"
        func = "area"
        size = [5, 10]
        expected_result = "Invalid figure: rectangle. Available figures: ['circle', 'square', 'triangle']"

        # Act
        result = calculate.calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_calc_invalid_function(self):
        # Arrange
        fig = "circle"
        func = "volume"
        size = [5]
        expected_result = (
            "Invalid function: volume. Available functions: ['perimeter', 'area']"
        )

        # Act
        result = calculate.calc(fig, func, size)

        # Assert
        self.assertEqual(result, expected_result)

    def test_calc_invalid_triangle_sides(self):
        # Arrange
        fig = "triangle"
        func = "area"
        size = [1, 2, 4]
        expected_result = "Error calculating area of triangle: math domain error"

        # Act
        result = calculate.calc(fig, func, size)

        # Assert
        self.assertIn(expected_result, result)

    def test_calc_invalid_square_sides(self):
        # Arrange
        fig = "square"
        func = "area"
        size = [-4]
        expected_result = "Error calculating area of square: negative side"

        # Act
        result = calculate.calc(fig, func, size)

        # Assert
        self.assertIn(expected_result, result)

    def test_calc_invalid_circle_radius(self):
        # Arrange
        fig = "circle"
        func = "perimeter"
        size = [-5]
        expected_result = "Error calculating perimeter of circle: negative radius"

        # Act
        result = calculate.calc(fig, func, size)

        # Assert
        self.assertIn(expected_result, result)
