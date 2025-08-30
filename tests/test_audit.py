import unittest
from core.audit import GraduationAuditor
from core.student import Student
from core.course import Course


class TestGraduationAuditor(unittest.TestCase):

   def setUp(self):
    self.auditor = GraduationAuditor(min_credits=120, min_gpa=2.0)

    # Student who fails (less than required credits)
    self.student_fail = Student(
        name="Failing Student",
        student_id="FS123",
        courses=[
            Course("ENG101", 3, "C", "Fall", "English"),
            Course("MTH101", 3, "D", "Fall", "Math")
        ]
    )

    # Student who passes
    self.student_pass = Student(
        name="Passing Student",
        student_id="PS456",
        courses=[
            Course("ENG101", 3, "A", "Fall"),
            Course("MTH101", 3, "B", "Fall"),
            Course("PHY101", 3, "A", "Fall"),
            Course("BIO101", 3, "B", "Fall"),
            Course("CSC101", 3, "A", "Fall"),
            Course("CHM101", 3, "A", "Fall"),
            Course("PSY101", 3, "B", "Fall"),
            Course("HIS101", 3, "C", "Fall"),
            Course("GEO101", 3, "A", "Fall"),
            Course("ART101", 3, "B", "Fall"),
            Course("MTH201", 3, "B", "Fall"),
            Course("ENG201", 3, "A", "Fall")
        ]
    )

    def test_check_eligibility_failure(self):
        total_credits = self.student_fail.total_credits()
        gpa = self.student_fail.calculate_gpa()
        result = self.auditor.check_eligibility(total_credits, gpa=gpa)
        self.assertFalse(result["eligible"])
        self.assertIn("credit", result["reasons"])

    def test_check_eligibility_success(self):
        total_credits = self.student_pass.total_credits()
        gpa = self.student_pass.calculate_gpa()
        result = self.auditor.check_eligibility(total_credits, gpa=gpa)
        self.assertTrue(result["eligible"])
        self.assertEqual(result["reasons"], [])
