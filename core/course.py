from typing import Optional

class Course:
    def __init__(self, course_code: str, credit: int, grade: str, semester: str, title: Optional[str] = None):
        self.course_code = course_code.upper()
        self.title = title or course_code.upper()
        self.credit = credit
        self.grade = grade.upper()
        self.semester = semester

    def to_dict(self) -> dict:
        return {
            "course": self.course_code,
            "title": self.title,
            "credit": self.credit,
            "grade": self.grade,
            "semester": self.semester
        }

    def __str__(self):
        return f"{self.course_code} ({self.semester}): {self.grade} ({self.credit} credits)"

    def is_valid_grade(self) -> bool:
        return self.grade in ["A", "B", "C", "D", "E", "F"]

    def grade_point(self) -> float:
        grade_map = {"A": 5.0, "B": 4.0, "C": 3.0, "D": 2.0, "E": 1.0, "F": 0.0}
        return grade_map.get(self.grade, 0.0)

    def weighted_score(self) -> float:
        return self.grade_point() * self.credit
