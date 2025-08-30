import unittest
from unittest.mock import patch
import pandas as pd
from core.transcript_generator import TranscriptGenerator

class TestTranscriptGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = TranscriptGenerator()
        self.sample_data = pd.DataFrame({
            "course": ["Mathematics", "English", "Physics", "History"],
            "credit": [3, 2, 3, 2],
            "grade": ["A", "B", "C", "A"],
            "semester": ["Fall 2023", "Fall 2023", "Spring 2024", "Spring 2024"]
        })
        self.student_name = "Alice Johnson"

    @patch("core.transcript_generator.Console.print")
    @patch("core.transcript_generator.Console.rule")
    def test_generate_transcript_success(self, mock_rule, mock_print):
        message = self.generator.generate(self.sample_data, self.student_name)

        # Check that print was called multiple times (panel, tables, gpa summary)
        self.assertTrue(mock_print.called)
        self.assertTrue(mock_rule.called)

        # Check returned message
        self.assertIn(self.student_name, message)
        self.assertIn("transcript rendered", message)

    def test_generate_with_empty_dataframe(self):
        empty_df = pd.DataFrame(columns=["course", "credit", "grade", "semester"])
        with patch("core.transcript_generator.Console.print"):
            message = self.generator.generate(empty_df, self.student_name)

        self.assertIn(self.student_name, message)

if __name__ == "__main__":
    unittest.main()
