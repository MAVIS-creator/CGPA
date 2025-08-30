📘 USER_GUIDE.md

```markdown
# 👨‍🏫 User Guide – GPA & Transcript Generator CLI

This guide walks you through setting up, running, and using the GPA & Transcript Generator application.

---

## 🛠️ Prerequisites

Make sure you have Python 3.7 or newer and pip installed on your system.

To verify:


python --version
pip --version
📦 Installing Requirements
After downloading or cloning the project, navigate to the directory:


cd student_gpa_transcript
Install all Python dependencies:


pip install -r requirements.txt
▶️ Running the Program
To run the program:


python main.py
This will start the CLI interface where you can:

Enter student information (name, ID, department, level)

Add courses for different semesters

Enter course codes, titles, credits, and grades

View the formatted transcript grouped by semester

See cumulative GPA displayed at the end

📂 Sample Data Format (Optional)
If using students.csv or automating inputs, ensure CSV data resembles:


student_id,name,department,level,course,credit,grade,semester
STU-001,Jane Doe,CSC,400,COSC402,3,A,1st
STU-001,Jane Doe,CSC,400,MTH401,2,B,1st
📤 Output Format
The transcript is printed to the terminal using Rich formatting. Example:


📄 OFFICIAL TRANSCRIPT FOR: Jane Doe

📘 Semester: 1st
+-----------+--------+--------+
|  Course   | Credit | Grade  |
+-----------+--------+--------+
| COSC402   |   3    |   A    |
| MTH401    |   2    |   B    |

📊 Cumulative GPA (5.0 scale): 4.6 | Total Credits: 5
🧩 Adding More Courses or Students
You can:

Edit the main.py to accept CSV input

Use the Student and Course classes in core/ to programmatically construct your own logic

🔄 Resetting
Simply rerun python main.py to start fresh. No local database is used.