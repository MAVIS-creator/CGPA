GradeCalc – Student GPA Calculator & Transcript Generator (CLI)
GradeCalc is a command-line application written in Python that calculates student GPAs, generates academic transcripts, audits graduation eligibility, and creates recommendation letters — all using CSV data and the standard library (plus rich for styled output).

🚀 Features

GPA Calculation using a 5.0 scale

Semester-wise transcript generation

Graduation eligibility audit (based on GPA and credits)

Recommendation letter generation

GPA trend analysis over semesters

CLI-only interface — no GUI dependencies

Fully modular and object-oriented architecture

Uses only Python Standard Library + rich for terminal formatting

📁 Project Structure

gradecalc/
├── main.py # CLI entry point
├── cli_menu.py # (if used) for CLI menu interactions
├── config.py # Constants like grading scale

├── core/
│ ├── gpa_calculator.py # GPA computation logic
│ ├── transcript_generator.py # Transcript output logic
│ ├── analytics.py # Semester-wise GPA trend chart
│ ├── audit.py # Graduation eligibility checker
│ ├── recommendation.py # Recommendation letter writer
│ ├── student.py # Student object class
│ └── course.py # Course object class

├── utils/
│ ├── file_io.py # File read/write helpers (optional)
│ ├── input_validator.py # Input validation functions
│ └── logger.py # Log handling (optional)

├── data/
│ ├── students.csv # Input data file
│ └── transcripts/ # Output transcript files

├── templates/
│ ├── recommendation_letter.txt # Saved recommendation output
│ └── transcript_template.txt # Placeholder formatting (optional)

├── tests/
│ ├── test_gpa_calculator.py
│ ├── test_audit.py
│ └── test_transcript_generator.py

├── docs/
│ ├── README.md # Project overview (this file)
│ ├── USER_GUIDE.md # CLI usage instructions
│ ├── REQUIREMENTS.md # Functional and non-functional requirements
│ └── TECHNICAL_DOC.md # Technical details and class documentation

└── requirements.txt # Only contains rich

🖥️ Requirements

Python 3.7+

rich (for styled CLI output)

Install rich:

pip install rich

🔧 How to Use

Clone or download the repository.

Place your student data in data/students.csv.

Run the CLI from the terminal:

Basic usage:

python main.py --student-id 2023001111

Generate transcript + recommendation letter:

python main.py --student-id 2023001111 --recommend

Optional: specify CSV path:

python main.py --csv data/students.csv --student-id 2023001111

🧪 Running Tests

Run all tests:

python -m unittest discover

Run specific test module:

python -m unittest tests.test_gpa_calculator

🗃️ Sample Data Format (students.csv)

student_id,name,department,level,course,credit,grade,semester
2023001111,Alice Smith,Computer Science,400,CSC202,3,A,Fall 2023

✍️ Authors

ADEG

📜 License

MIT License (or your preferred license)

📎 Related Files

templates/recommendation_letter.txt

templates/transcript_template.txt

data/students.csv