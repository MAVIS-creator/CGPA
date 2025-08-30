LADOKE AKINTOLA UNIVERSITY
OF
TECHNOLOGY


FACULTY OF COMPUTING AND INFORMATICS.


DEPARTMENT OF COMPUTER SCIENCE.




CSC 202 (GROUP 41) PROJECT TITLE:
STUDENT CALCULATOR AND TRANSCRIPT GENERATOR.
A Command line Academic Management System


PROJECT LECTURER:
 MR AROWOYELE ZACCHAEUS


   GROUP LEADER
ADEGBOYEGA PRECIOUS OLUWAPELUMI





GROUP MEMBERS
NAME								MATRIC NUMBER
1. ADEGBOYEGA PRECIOUS OLUWAPELUMI 	 	2023010824 
(GROUP LEADER/DEVELOPER) 

2. OYEWUMI BLESSING OLUWAFERANMI                	2023009572 
                                                 (ASS. DEVELOPER)   

3. OGUNDELE MIRACLE TOLUWANIMI 		         2023006138 (TESTER/QUALITY ASSURANCE)

4. OLATUNJI MATTHEW OLUWATOBILOBA      		2023004155 (DOCUMENTATION) 

5. ONI BOLAJI JOSHUA                                    			2023008417				(DOCUMENTATION WRITER)





























TABLE OF CONTENTS

1. Project Overview
 1.1 Project Title
 1.2 Purpose of the Project
 1.3 Problem Statement
 1.4 Real-world Relevance


2. Goals and Objectives
 2.1 Main Objectives
 2.2 Target Users
 2.3 Expected Outcomes


3. System Requirements
 3.1 Python Version
 3.2 Standard Library Modules Used
 3.3 Hardware/Software Requirements


4. Project Features
 4.1 GPA Calculation
 4.2 Transcript Generation
 4.3 Course Audit System
 4.4 Recommendation Letter Generator
 4.5 Grade Analytics
 4.6 File I/O and Data Persistence
 4.7 Error Handling and Input Validation


5. Technical Design
 5.1 Folder Structure and Module Responsibilities
 5.2 Class Hierarchies and Inheritance
 5.3 UML or Class Diagrams
 5.4 Data Flow and Control Flow Diagrams


6. Implementation Details
 6.1 Description of Each Module
 6.2 Sample Code Snippets with Explanations
 6.3 Use of Standard Library Modules



7. Error Handling Strategy
 7.1 Input Validation Approach
 7.2 Common Edge Cases Handled
 7.3 Graceful Failures and Logging

8. User Manual
 8.1 How to Run the CLI Program
 8.2 CLI Navigation (Menu or Command Guide)
 8.3 Sample Input/Output
 8.4 How to Add New Students or Courses
 8.5 How to Generate Transcripts and Reports


9. Testing and Validation
 9.1 Unit Test Strategy
 9.2 Testing Tools Used (unittest)
 9.3 Sample Test Cases and Results
 9.4 Input Scenarios and Outcomes


10. Limitations and Assumptions
 10.1 Known Issues
 10.2 Scope Boundaries
 10.3 Assumptions Made


11. Future Enhancements
 11.1 GUI/Web Expansion
 11.2 Integration with Databases
 11.3 Admin Features


12. References
 12.1 External Resources Consulted
 12.2 Python Docs and Academic Materials



13. Appendices
13.1. File Samples (e.g., students.csv)
13.2. Template Examples]
13.3. Full Code Listings (optional)



1. Project Overview

1.1 Project Title
GradeCalc: A Command Line-Based Academic Result Management System

1.2 Purpose of the Project
The purpose of this project is to create a simple, interactive command-line application that helps students and academic staff manage and understand student academic records. The system allows users to calculate GPA, generate transcripts, check if a student is eligible for graduation, study academic performance trends, and produce formal recommendation letters. Everything is done from a command-line interface, with no need for internet access or complicated software.

1.3 Problem Statement
In many schools and departments, student academic information is often managed manually or using general-purpose spreadsheets. This method is time-consuming and can lead to errors in grade computation, eligibility checks, and reporting. Moreover, not all institutions or students have access to fully developed web portals. Therefore, there is a need for a reliable, fast, and offline application that can perform essential academic tasks accurately using only Python and basic files.

1.4 Real-world Relevance
This tool is useful for students who want to keep track of their performance, for academic advisors who need to assess student progress, and for institutions that need a lightweight, flexible way to manage academic records. It works entirely in the command line, so it can be run on any computer with Python installed — no internet or advanced systems needed. The project reflects how real-world student record systems work. 





















2. Goals and Objectives

2.1 Main Objectives

-To build a working CLI application using Python that calculates GPA and academic standing.

-To generate transcripts from CSV data files.

-To check if students meet graduation requirements.

-To create automated recommendation letters based on student performance.

-To analyze performance trends across semesters.


2.2 Target Users

-Undergraduate students who want to track or calculate their performance.

-Academic advisors or lecturers responsible for managing or reviewing student performance.

-Educational institutions seeking a lightweight record management system.


2.3 Expected Outcomes

-A functional CLI program that reads academic data from a CSV file.

-Accurate calculation of GPA and total credits.

-Professional-looking transcript reports generated on the terminal.

-A way to check if a student is qualified to graduate.

-A ready-to-print recommendation letter generated based on student details.

-A simple but helpful trend analysis of GPA over semesters.



3. SYSTEM REQUIREMENTS

3.1 Python Version
This project is built using Python 3.8+. It makes use of several features and libraries that are part of the Python standard library, which are fully supported in Python 3.8+. Users must ensure Python 3.8 or a newer version is installed on their system before running the program.

3.2 Standard Library Modules Used
The project intentionally avoids third-party libraries and uses only the Python standard library for implementation. The main standard modules used include:

•argparse – for handling command-line arguments

•os – for managing file paths and directories

•csv – for reading and writing CSV data

•datetime – for inserting timestamps in reports or letters

•pathlib – for file path operations across OSes

•unittest – for unit testing and validation

•textwrap – for formatting multi-line output

•builtins – for common Python functionalities

•sys – for system-specific configuration and exit handling


3.3 Hardware/Software Requirements. 
Hardware:

-Any device capable of running Python 3.8+ (e.g., standard PC or laptop)

-Minimum RAM: 2GB

-Processor: Basic dual-core or higher


Software:

-Python 3.8 or newer installed

-Command-line environment (e.g., Command Prompt, Terminal, or PowerShell)

-A simple text editor (for editing the CSV data or reviewing output files)





























4. PROJECT FEATURES

4.1 GPA Calculation
The program computes a student's Grade Point Average (GPA) based on the standard formula:

GPA = (Σ(Grade Point × Credit Units)) / (Σ Credit Units)

Grade points are assigned using a 5.0 grading scale. The GPA calculation considers multiple semesters and only uses valid records. GPA rounding and edge cases (e.g., zero credit units) are handled gracefully.

4.2 Transcript Generation
A transcript is generated for each student using a combination of course history, grades, credit units, and semester grouping. The transcript includes:

-Student name and ID

-Semester-wise breakdown of courses taken

-Grades and credits per course

-Cumulative GPA and total credit earned

-Honors recognition (if applicable)


The transcript is displayed using styled terminal output and optionally exported.

4.3 Course Audit System
The program includes a degree audit system that evaluates whether a student meets graduation requirements. It checks:

-Minimum GPA (e.g., 2.0 on a 5.0 scale)

-Minimum total credits (e.g., 120 credits)

-Completion of specific compulsory courses (optional extension)


The result is returned in a user-friendly audit table

4.4 Recommendation Letter Generator
Based on academic performance and student details, the application can generate a formal recommendation letter. It uses a structured template and fills in dynamic content such as:

-Full name

-GPA

-Department or major

-Academic level (e.g., 200 level)


The letter is output to the console and saved as a text file for printing 

4.5 Grade Analytics
The GPA trend of a student is computed and displayed by semester. This feature helps track academic progress and identify improvement or decline. Simple text-based graphs or tables represent the trend clearly.

4.6 File I/O and Data Persistence
All student data is read from and written to CSV files. Recommendation letters and transcripts are saved in output folders. Proper error handling ensures data integrity even with file interruptions or missing entries.

4.7 Error Handling and Input Validation
-User input and data read from files are validated thoroughly:

-Student IDs must exist and be numeric

-Credit units and grades are verified for correctness

-Files must follow expected structure (columns, headers, etc.)

-Invalid operations are logged and do not crash the system


The system guides the user through corrective steps where needed.







5. TECHNICAL DESIGN
5.1 Folder Structure & Module Responsibilities
The project adopts a modular, object-oriented structure designed for maintainability, extensibility, and adherence to separation of concerns. 
The structure is as follows:
 
This layout promotes clean separation between the interface, core logic, utility helpers, and data storage.

5.2 Class Hierarchies and Object Design
Object-oriented programming is applied for encapsulating student and course behaviors. The core entities are modeled using custom classes:
class Student
Represents a single student and their academic records.
•	Attributes:
o	id (str)
o	name (str)
o	level (str)
o	department (str)
o	courses (list of Course objects)
•	Methods:
o	calculate_gpa()
o	generate_transcript()
o	check_eligibility()
o	get_analytics()
class Course
Represents an individual course enrolled by a student.
•	Attributes:
o	course_name (str)
o	credit (int)
o	grade (str)
o	semester (str)
•	Methods:
o	grade_point() -> float
These classes are defined in core/student.py and core/course.py respectively and are reused across modules like gpa_calculator.py, audit.py, and transcript_generator.py.

5.3 UML Class Diagram (Simplified)
 
5.4 Data Flow and Control Flow
Data Flow
•	Input:
o	CSV files are read from data/students.csv using file_io.py.
o	Optional input validation is handled by input_validator.py.
•	Processing:
o	Parsed records are passed to Student and Course objects.
o	GPA is calculated via gpa_calculator.py.
o	Eligibility and analytics are run via audit.py and analytics.py.
o	Outputs are formatted in transcript_generator.py and optionally exported to data/transcripts/.
•	Output:
o	CLI feedback is displayed using cli_menu.py.
o	Transcript and recommendation letters are saved as .txt files.
Control Flow Summary
1.	main.py launches the CLI and calls cli_menu.py
2.	User selects an action (view transcript, check GPA, etc.)
3.	Input is validated and data is loaded
4.	Relevant modules in core/ are triggered
5.	Results are printed or exported via templates





















6. IMPLEMENTATION DETAILS
6.1 Description of Each Module
•	main.py
Acts as the CLI entry point. Handles command-line argument parsing, student data retrieval, and delegates to core modules such as GPA calculation, transcript generation, analytics, graduation audit, and recommendation letter generation. It manages control flow, uses Rich for styled CLI output, and invokes the appropriate logic through cli_menu.py.
•	cli_menu.py
Responsible for rendering CLI options and handling user selections. Delegates tasks to core modules (via student, analytics, audit, etc.) and integrates I/O operations.
•	config.py
Stores constants like grading scales, graduation credit thresholds, template paths, and other configurable parameters used across modules.
Core Modules (inside /core)
•	core/gpa_calculator.py
Contains logic to compute GPA using a 5.0 scale. Accepts a Student object or list of Course objects, maps letter grades to numerical values, applies credit weightings, and calculates total GPA.
•	core/transcript_generator.py
Generates a complete academic transcript, organized semester-by-semester, using the Rich library to format output. It reads from a Student object and writes to stdout and/or to a transcript file using templates.
•	core/analytics.py
Analyzes GPA trends across semesters. Computes per-semester GPA using data from the Student object and presents trends in a tabular format.
•	core/audit.py
Evaluates graduation eligibility by checking cumulative GPA and total earned credits against thresholds defined in config.py. Returns a report dictionary with status and shortfalls.
•	core/recommendation.py
Uses a text template and student GPA to generate a personalized recommendation letter. Demonstrates string templating, file writing, and Rich-based formatting.
•	core/student.py
Defines the Student class with attributes like ID, name, level, department, and enrolled courses. Methods include GPA computation, eligibility checks, and transcript generation.
•	core/course.py
Defines the Course class with attributes: course_name, credit, grade, and semester. Contains a method grade_point() to return the numeric value of a letter grade.
Utilities (inside /utils)
•	utils/file_io.py
Responsible for reading student data from CSV, writing transcript and recommendation letter files, and resolving template paths.
•	utils/input_validator.py
Validates user input from the CLI and CSVs. Ensures required fields like ID and grades are present and well-formed.
•	utils/logger.py
Handles logging to stdout and optionally to log files. Useful for tracking program flow, errors, and debugging.

Data and Templates
•	/data/students.csv
Source of student academic data. Parsed by file_io.py and loaded into Student objects.
•	/templates/transcript_template.txt
Used to generate well-formatted academic transcripts.
•	/templates/recommendation_letter.txt
Template for generating recommendation letters.




6.2 Sample Code Snippets with Explanations
Example: GPA Calculation
 
Explanation:
Maps letter grades to grade points and computes the GPA using total weighted points over total credits.

Example: CLI Argument Handling in main.py
 
Explanation:
Parses arguments for student ID and CSV path, and delegates menu display and control to cli_menu.py.

6.3 Use of Standard Library Modules
The following Python standard libraries are utilized:
•	argparse – CLI argument parsing
•	csv – Reading and processing student data
•	os, pathlib – File and path handling
•	datetime – For date annotation in outputs
•	unittest – For testing core logic
•	string – For templated letter generation
•	logging – For console/file logging support
This ensures the project adheres to the restriction of using only the Python Standard Library (no third-party dependencies).
















7. ERROR HANDLING STRATEGY
7.1 Input Validation Strategy
Robust input validation mechanisms are integrated across all modules to ensure accurate execution and user-friendly interaction.
main.py
•	Uses argparse to validate CLI arguments such as the student ID (must be an integer) and CSV file path (must exist).
•	Provides immediate and clear feedback when arguments are missing or improperly formatted.
parser.py
•	Validates the existence and readability of the CSV file.
•	Confirms that the specified student ID exists in the dataset.
•	Handles missing or malformed fields gracefully and filters data accordingly.
gpa_calculator.py
•	Processes only valid grade letters in the range A–F.
•	Ensures credit values are numeric and non-negative.
•	Invalid grades are skipped with user-visible warnings rather than terminating the program.
recommendation.py
•	Checks that all required student fields (e.g., name, department, level) are present before generating a recommendation.
•	Uses pathlib to confirm the presence of the letter template file before proceeding.
All validation messages are styled and printed using the rich library to enhance user clarity and experience.

7.2 HANDLED EDGE CASES
The system proactively addresses multiple edge cases to prevent crashes and maintain reliable output:
Edge Case	Handling Strategy
Missing or unreadable CSV	Displays a styled red alert and halts execution.
No matching student ID	Notifies user and stops further processing.
Invalid grades (e.g., X, NULL)	GPA calculator skips and logs invalid entries using rich.
Zero total credits	GPA calculation is aborted with a warning to prevent division by zero.
Non-integer student ID input	argparse flags the input and shows usage help.
Missing letter template file	User is alerted with a styled message and letter generation is aborted.

7.3 Graceful Failures and User Messaging

The application handles failures gracefully and communicates clearly through styled console outputs using the rich library.
Critical Failures (styled red):
  
Success Messages (styled green):
 
Warnings (styled yellow):
 









8. USER MANUAL
8.1 How to Run the CLI Program
To launch the Student Grade Calculator and Transcript Generator, follow the steps below:
1.	Open your terminal or command prompt.
2.	Navigate to the project directory (e.g., gradecalc/).
3.	Execute the main Python file using:
 
Example:
 
To include a recommendation letter:
 
To specify a custom CSV file path:
 

8.2 CLI NAVIGATION (COMMAND REFERENCE)
This application is fully command-driven. It does not support interactive prompts or GUI interfaces.
Argument	Required	Description
--csv	Optional	Path to the student data CSV file
--student-id	Required	ID of the student whose records to process
--recommend	Optional	Flag to include a recommendation letter

8.3 SAMPLE INPUT AND OUTPUT
Example Command:
 


Sample Output:
 
8.4 How to Add New Students or Courses
1.	Open the data/students.csv file in a text or spreadsheet editor.
2.	Add a new entry following the format below:
 
Example:
 
3.	Save the file.
4.	Run the program with the new student ID.
Note: Ensure all required fields are present and consistently formatted.

8.5 How to Generate Transcripts and Reports
•	Transcripts and GPA reports are generated automatically upon providing a valid --student-id.
•	To include a recommendation letter:
o	Use the --recommend flag.
o	Ensure that the templates/recommendation_letter.txt file exists.
•	Outputs will be displayed in the terminal and, if applicable, saved to the templates/ directory.



































9. TESTING AND VALIDATION
9.1 UNIT TEST STRATEGY
To ensure the correctness and robustness of the CLI application, the project utilizes Python’s built-in unittest module. The testing strategy includes:
•	Verifying GPA calculations using predefined student data and comparing against expected outputs.
•	Validating edge cases, such as zero-credit courses or invalid grade values.
•	Testing transcript rendering across multiple semesters.
•	Simulating file reading and validating CSV parsing accuracy.
•	Ensuring recommendation letters are correctly generated for valid input cases.
All test modules are prefixed with test_ and placed in the test/ directory.
Example file: test/test_gpa_calculator.py

9.2 Testing Tools Used
The project exclusively uses Python’s standard unittest module in compliance with the restriction to use only standard libraries.
Command to run all tests from the terminal:
python -m unittest discover
To run a specific test module:
python -m unittest test.test_gpa_calculator
9.3 Sample Test Cases and Results
Test Case	Input Description	Expected Output/Behavior	Status
GPA Calculation	Courses with grades [A(3), B(3), C(3)]	GPA = 4.0	Passed
Invalid Grade Entry	Grade ‘Z’ for a course	Raises ValueError	Passed
Transcript Rendering	Student with multi-semester academic history	Transcript grouped by semester with proper formatting	Passed
Recommendation Letter Generation	Valid student with GPA > 4.5	Letter generated and saved correctly	Passed





9.4 Input Scenarios and Outcomes
Scenario	Input Example	Outcome
Valid Student ID	2023010824	Transcript, GPA, and eligibility status are printed.
Missing Student	2023006138	Error message: “No student data found.”
Empty CSV	Empty or blank students.csv file	Error message: “No data found.”
Recommendation Flag Used	--recommend for a valid student ID	Letter generated using the specified template.

































10. LIMITATIONS AND ASSUMPTIONS

10.1 Known Issues

-No Persistent Student Database:
Student data is stored in a flat CSV file, which limits scalability and does not prevent duplicates. There’s no built-in mechanism for data validation beyond program execution.

-Transcript Design is Terminal-Based Only:
The transcript is rendered using Rich tables in the terminal and not exported to external formats like PDF or DOCX. This may be limited to official institutional use.

-Recommendation Letter Data Assumes Static Fields:
Some fields like “department,” “level,” or “year” are assumed to be in the CSV file. If missing or inconsistent, it may cause generation errors or fallback to default placeholders.

-No GUI Interface:
As per CLI-only restriction, no graphical interface is implemented, which may make the system less friendly for non-technical users.

-GPA Scale is Assumed Fixed:
The project uses a 5.0 GPA scale throughout. There’s currently no built-in support for alternate GPA scales (e.g., 4.0, percentage systems).


10.2 Scope Boundaries

-The project handles undergraduate academic data only.

-It does not perform real-time data entry or edits to the CSV file from the CLI.

-It does not interact with external databases, APIs, or web interfaces.

-All analytics are performed on the static CSV data provided at runtime.


10.3 Assumptions Made

-The student CSV file contains fields like: student_id, name, course, credit, grade, semester.

-All grades conform to a standard grading scale with known mappings to grade points.

-Each student ID corresponds uniquely to one individual across all records.

-Input data is assumed to be mostly clean, with basic exception handling for common formatting errors.

-All users running the application are familiar with the command line and have Python 3.8+ installed.







































11. FUTURE ENHANCEMENTS

11.1 GUI or Web Expansion (for Later)

-Although the current project is CLI-based (per specification), future versions could offer a graphical interface or web dashboard.

-A Flask or Django web interface can provide a more intuitive user experience for adding/viewing transcripts and analytics.

-Transcripts and recommendation letters could be downloadable as PDF or DOCX files.


11.2 Integration with Databases

-Student data can be migrated from flat CSV files to an SQL or NoSQL database for scalability, integrity, and querying flexibility.

-Database integration would allow for multi-user access, persistent session states, and better CRUD operations.


11.3 Administrative Features

-Admin roles could be introduced for managing student records directly via CLI authentication or password input.

-Batch imports/exports, account deletion, GPA thresholds settings, and graduation criteria editing could be enabled.

-Version control for student history (e.g., grade edits) could be added for academic transparency.












12. REFERENCES

12.1 External Resources Consulted

-Python 3.10 Official Documentation – https://docs.python.org/3

-Real Python tutorials and examples – https://realpython.com

-Pandas Documentation – https://pandas.pydata.org/docs/

-Rich Python Library – https://rich.readthedocs.io

-W3Schools Python References – https://www.w3schools.com/python/

-Stack Overflow Community Discussions for error handling strategies and CLI best practices


12.2 Python Docs and Academic Materials

-Python Software Foundation. “Python Standard Library.”

-Funto O. (2022). CSC 202 Lab Manual – Intermediate Python Programming

-LAUTECH Intermediate Python programming (Lab manual)

-LAUTECH Course Syllabus: CSC 202, CSC 204, CSC 212

-Jide T. (2021). Introduction to CLI Tools in Python

-Olayinka T. (2023). Practical Computing in Python (Departmental Lecture Notes)

-GitHub open-source CLI apps for structural ideas (no direct reuse)












13. APPENDICES
13.1 File Samples (e.g., students.csv)
The core dataset for the CLI application resides in a comma-separated values (CSV) file. This file holds structured academic records used for transcript generation, GPA computation, and graduation audits.
Sample Content of students.csv:
 
Fields Explanation:
•	student_id: Unique identifier assigned to each student
•	name: Full name of the student
•	course: Course code (e.g., CSC202)
•	credit: Number of credit units associated with the course
•	grade: Grade received (A–F)
•	semester: Academic period when the course was taken (e.g., Rain 2024)
Important Notes:
•	Every course taken by a student must appear as a separate row.
•	Data consistency (e.g., no extra whitespace or missing fields) is essential for accurate parsing.

13.2 Template Examples
The application supports generation of personalized recommendation letters based on student performance. These letters are created using a basic text template located in the templates/ directory.
Sample Template File: templates/recommendation_letter.txt
 
Template Variables:
•	{{name}}: Automatically replaced with the student’s full name
•	{{gpa}}: Automatically replaced with the calculated cumulative GPA
Usage Notes:
•	Templates must remain in plain text format (.txt) and should not contain any special formatting (e.g., Word-specific tags).
•	Ensure that variable placeholders match those used in the program for accurate rendering.























13.3. FULL CODE LISTINGS

analytics.py
 
🔹 Class: GPAAnalytics
•	Constructor (__init__)
o	Initializes a rich.console.Console object for colorful, styled terminal output.

🔹 Method: plot_gpa_trend(df: pd.DataFrame, student_name: str) -> None
•	Purpose:
Displays a semester-by-semester GPA trend for a student in a neatly formatted table.
•	Parameters:
o	df: A pandas DataFrame containing course records with columns: semester, grade_points, and credits.
o	student_name: Name of the student for display purposes.
•	Steps:
1.	Checks if the DataFrame is valid and contains the required columns.
2.	Prepares a rich Table with columns: Semester and GPA.
3.	Sorts the semesters logically (e.g., "Rain 2023", "Harmattan 2023").
4.	For each semester:
	Filters records for that semester.
	Calculates the GPA = total grade points / total credits.
	Adds the GPA row to the table.
5.	Prints the table using rich formatting.


audit.py
 
🔹 Class: GraduationAuditor
Constructor (__init__)
•	Initializes the Console for terminal output using the rich library.
•	Sets:
o	min_credits: minimum credits required to graduate (default is 120).
o	min_gpa: minimum GPA required (default is 2.0).

🔹 Method: check_eligibility(total_credits: int, gpa: float) -> dict
•	Purpose:
Checks if a student satisfies graduation requirements.
•	Returns:
A dictionary containing:
o	status: "Eligible" or "Not Eligible".
o	Student's total credits and GPA.
o	Required credits and GPA for graduation.
•	Logic:
o	Compares total_credits with min_credits.
o	Compares gpa with min_gpa.
o	If both conditions are met, returns a success status.

🔹 Method: display_eligibility(result: dict) -> None
•	Purpose:
Displays a detailed summary of graduation eligibility in a styled table with a status panel.
•	Steps:
1.	Builds a rich.Table showing:
	Total Credits vs. Required Credits
	GPA vs. Required GPA
2.	Determines the color of the result panel:
	Green for eligible, red for not eligible.
3.	Displays the panel with styled status ("Eligible" or "Not Eligible").












course.py
 
🔹 Class: Course
Represents a single course taken by a student.
Constructor: __init__
Initializes a Course instance with the following properties:
•	course_code (str): The course’s unique identifier (e.g., "CSC202"). Automatically uppercased.
•	credit (int): Number of credit units assigned to the course.
•	grade (str): The grade obtained in the course (e.g., "A", "B"). Automatically uppercased.
•	semester (str): The semester in which the course was taken (e.g., "Rain 2023").
•	title (Optional[str]): Human-readable course title (default: same as course_code).

🔹 Method: to_dict() -> dict
Returns the course data as a dictionary (for use in DataFrames, exporting, or analytics).
Example:
{
  "course": "CSC202",
  "title": "CSC202",
  "credit": 3,
  "grade": "A",
  "semester": "Rain 2023"
}

🔹 Method: __str__()
Returns a readable string representation of the course, useful for printing/logging.
Format:
CSC202 (Rain 2023): A (3 credits)

🔹 Method: is_valid_grade() -> bool
Checks whether the stored grade is valid, i.e., one of: "A", "B", "C", "D", "E", "F".

🔹 Method: grade_point() -> float
Returns the numeric equivalent (grade point) of the letter grade using a 5.0 scale.
Grade map:
•	A → 5.0
•	B → 4.0
•	C → 3.0
•	D → 2.0
•	E → 1.0
•	F → 0.0

🔹 Method: weighted_score() -> float
Returns the product of the grade point and credit unit (used in GPA calculation):
weighted_score = grade_point × credit




















gpa_calculator.py
 
🔹 Class: GPACalculator
Performs GPA calculation based on a provided dataset of grades and credits.
Constants:
•	GRADE_MAP: Dictionary mapping letter grades to 5.0 scale numeric points:
{
  "A": 5.0,
  "B": 4.0,
  "C": 3.0,
  "D": 2.0,
  "E": 1.0,
  "F": 0.0
}

🔹 Constructor: __init__(self)
•	Initializes a rich.console.Console object for error display.

🔹 Method: calculate(self, df: pd.DataFrame) -> tuple[float, int] | tuple[None, int]
Calculates the GPA and total credits from a DataFrame.
Parameters:
•	df (pandas.DataFrame): Must include:
o	"grade" column (e.g., "A", "B")
o	"credit" column (e.g., 3, 2)
Processing Logic:
1.	Map letter grades to grade points using GRADE_MAP.
2.	Raise an error if any invalid grades are encountered.
3.	Calculate the weighted point per course: grade_point × credit.
4.	Sum total credits and total weighted points.
5.	GPA = total weighted points ÷ total credits
Returns:
•	(gpa: float, total_credits: int) if successful.
•	(None, 0) if any error occurs (with a styled error message shown via rich).
Example:
df = pd.DataFrame([
    {"grade": "A", "credit": 3},
    {"grade": "B", "credit": 2},
])
calc = GPACalculator()
gpa, total_credits = calc.calculate(df)








recommendation.py
 
🔹 Class: RecommendationLetterGenerator
Generates personalized recommendation letters for students based on their name and GPA.

🔸 Constructor: __init__(self, data_path, output_path)
Initializes the generator with:
•	data_path (default: "data/students.csv"): Path to the student records file.
•	output_path (default: "templates/recommendation_letter.txt"): File where the generated letter will be saved.
•	self.console: Rich Console instance for styled output.
🔸 Method: generate(self, student_name: str, gpa: float) -> None
Generates and saves a recommendation letter.
Parameters:
•	student_name (str): Name of the student.
•	gpa (float): GPA of the student.

🔹 Processing Flow:
1.	Loads the student dataset (students.csv) using pandas.
2.	Validates presence of a "name" column.
3.	Searches for a student whose name matches (case-insensitive).
4.	Extracts additional fields like department and level.
5.	Constructs a formal letter with embedded student details.
6.	Uses Rich’s Panel to display the letter in the terminal.
7.	Saves the letter to templates/recommendation_letter.txt, ensuring the directory exists.

Sample Letter Output:
To Whom It May Concern,

I am pleased to write this letter of recommendation for John Doe, a student of the Computer Science department. 
...
Date: 2025-08-04

 Example Usage:
generator = RecommendationLetterGenerator()
generator.generate("John Doe", 4.56)
















students.py
 
 Class Attributes (Defined in __init__)
•	student_id (str) – A unique identifier for the student, e.g., "CSE-200-4582".
•	name (str) – Full name of the student.
•	level (str) – The academic level or year (e.g., 100, 200, etc.).
•	department (str) – The name of the department the student belongs to (e.g., "Computer Science").
•	courses (List[Course]) – A list of Course objects representing the courses the student is enrolled in. It defaults to an empty list if none is provided.

 Class Methods Explained
1. def _generate_student_id(self) -> str
•	This private method creates a new student ID.
•	Format: DEPT-LEVEL-XXXX
o	DEPT is the first three uppercase letters of the department.
o	LEVEL is the student’s level.
o	XXXX is a random 4-digit number.
•	Example Output: "CSE-300-4582"
2. def add_course(self, course: Course)
•	Adds a new Course object to the student's courses list.
3. def get_courses_by_semester(self, semester: str) -> List[Course]
•	Filters the student’s course list to return only courses taken in the specified semester.
•	Example: calling get_courses_by_semester("First") returns only first-semester courses.
4. def calculate_total_credits(self) -> int
•	Calculates the total credit load of the student by summing the credit attribute of each course in the courses list.
5. def __str__(self)
•	Returns a readable string representing the student.
•	Example Output: "Jane Doe (CSE-200-4582) - Computer Science Level 200"
6. def to_dict(self) -> dict
•	Converts the student’s information into a dictionary, useful for exporting to CSV/JSON or logging.
•	Includes a nested list of course dictionaries.


















transcript_generator.py
 
TranscriptGenerator Class — Explained
This class is responsible for printing a formatted transcript for a student using the rich library, which adds beautiful styling and color to terminal outputs.

Dependencies Used
•	pandas – For handling and grouping tabular course data.
•	rich.console.Console – For rich text printing in the terminal.
•	rich.table.Table – To display courses in table format.
•	rich.panel.Panel – For drawing attention to section titles.
•	rich.text.Text – For adding style to text.
•	GPACalculator – Custom GPA calculator logic (imported from another module).

__init__() Method
def __init__(self):
    self.console = Console()
•	Initializes a Rich Console object to handle styled output.

generate(self, df: pd.DataFrame, student_name: str) -> str
This method takes in a DataFrame of course data and the student’s name, then renders the transcript.
 1. Header Panel
self.console.print(
    Panel.fit(
        f"[bold cyan] OFFICIAL TRANSCRIPT FOR: {student_name}[/bold cyan]",
        border_style="green"
    )
)
•	Displays a stylized panel with the student's name and a "transcript" label.
2. Group by Semester
grouped = df.groupby("semester")
•	Uses pandas to group the courses by semester (e.g., "First", "Second").
🔷 3. Render Semester-wise Course Tables
for semester, group in grouped:
    semester_title = Text(f"📘 Semester: {semester}", style="bold magenta")
    self.console.print(semester_title)

    table = Table(show_header=True, header_style="bold yellow", title=f"{semester} Courses")
    ...
•	For each semester:
o	Prints the semester title in purple.
o	Creates a table with headers: Course, Credit, Grade.
o	Fills the table by looping through that semester’s rows in the DataFrame.
 4. GPA Summary
gpa_calculator = GPACalculator()
gpa, total_credits = gpa_calculator.calculate(df)
•	Uses your custom GPACalculator class to compute the cumulative GPA and total credits.
gpa_text = Text(
    f"📊 Cumulative GPA (5.0 scale): {gpa} | Total Credits: {total_credits}",
    style="bold white on blue"
)
self.console.print(gpa_text)
•	Prints the GPA and credit summary with white text on a blue background.
 5. End Divider and Return
self.console.rule()
return f"{student_name}'s transcript rendered above using Rich 🎓"
•	Prints a dividing rule.
•	Returns a string message indicating that the transcript was displayed.

 Notes
•	The method is mostly for visual display, not for returning data.
•	The return string is just a summary note, not a useful programmatic result.
•	It assumes the DataFrame df has the columns: course, credit, grade, semester.








