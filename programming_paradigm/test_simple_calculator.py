import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(3, 2), 1.5)
        self.assertEqual(self.calc.divide(-6, -3), 2)
        self.assertEqual(self.calc.divide(0, 1), 0)

        # Test division by zero
        self.assertIsNone(self.calc.divide(10, 0))

    def test_division_by_zero(self):
        """Test edge case of division by zero."""
        self.assertIsNone(self.calc.divide(10, 0), "Division by zero should return None.")
        self.assertIsNone(self.calc.divide(-10, 0), "Division by zero should return None.")
    
    def test_edge_cases(self):
        """Test other edge cases for divide."""
        self.assertEqual(self.calc.divide(0, 5), 0)  # 0 divided by a number should return 0
        self.assertIsNone(self.calc.divide(5, 0))  # Number divided by 0 should return None

if __name__ == '__main__':
    unittest.main()
