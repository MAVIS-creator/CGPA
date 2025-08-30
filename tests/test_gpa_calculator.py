import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pandas as pd
from core.gpa_calculator import GPACalculator

class TestGPACalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = GPACalculator()

    def test_valid_gpa_calculation(self):
        data = {
            "grade": ["A", "B", "C"],
            "credit": [3, 3, 2]
        }
        df = pd.DataFrame(data)
        gpa, total_credits = self.calculator.calculate(df)

        expected_gpa = round((5*3 + 4*3 + 3*2) / 8, 2)
        self.assertEqual(gpa, expected_gpa)
        self.assertEqual(total_credits, 8)

    def test_invalid_grade(self):
        data = {
            "grade": ["A", "Z", "B"],  # 'Z' is invalid
            "credit": [3, 2, 3]
        }
        df = pd.DataFrame(data)
        gpa, total_credits = self.calculator.calculate(df)

        self.assertIsNone(gpa)
        self.assertEqual(total_credits, 0)

    def test_zero_total_credits(self):
        data = {
            "grade": ["A", "B"],
            "credit": [0, 0]
        }
        df = pd.DataFrame(data)
        gpa, total_credits = self.calculator.calculate(df)

        self.assertIsNone(gpa)
        self.assertEqual(total_credits, 0)

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=["grade", "credit"])
        gpa, total_credits = self.calculator.calculate(df)

        self.assertIsNone(gpa)
        self.assertEqual(total_credits, 0)

if __name__ == "__main__":
    unittest.main()
