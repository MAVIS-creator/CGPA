# utils/input_validator.py

def validate_student_id(input_str: str) -> int:
    try:
        sid = int(input_str)
        if sid <= 0:
            raise ValueError("Student ID must be a positive integer.")
        return sid
    except ValueError:
        raise ValueError("Invalid Student ID. Please enter a valid number.")
