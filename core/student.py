from typing import List, Optional
from core.course import Course

class Student:
    def __init__(self, student_id: str, name: str, level: str, courses: Optional[List[Course]] = None):
        self.student_id = student_id
        self.name = name
        self.level = level
        self.courses = courses or []

    def _generate_student_id(self) -> str:
        # Simple auto-generated ID format: DEPT-LEVEL-00123
        import random
        suffix = str(random.randint(1000, 9999))
        dept_code = self.department[:3].upper()
        return f"{dept_code}-{self.level}-{suffix}"

    def add_course(self, course: Course):
        self.courses.append(course)

    def get_courses_by_semester(self, semester: str) -> List[Course]:
        return [c for c in self.courses if c.semester == semester]

    def calculate_total_credits(self) -> int:
        return sum(course.credit for course in self.courses)

    def __str__(self):
        return f"{self.name} ({self.student_id}) - {self.department} Level {self.level}"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "student_id": self.student_id,
            "department": self.department,
            "level": self.level,
            "courses": [c.to_dict() for c in self.courses]
        }
