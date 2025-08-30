# config.py

# Grading scale
GRADE_SCALE = {
    "A": 5.0,
    "B": 4.0,
    "C": 3.0,
    "D": 2.0,
    "E": 1.0,
    "F": 0.0,
}

# Minimum CGPA to graduate
GRADUATION_THRESHOLD = 2.0

# Transcript generation settings
TRANSCRIPT_TEMPLATE_PATH = "templates/transcript_template.txt"
TRANSCRIPT_OUTPUT_DIR = "data/transcripts"

# Recommendation letter template
RECOMMENDATION_TEMPLATE_PATH = "templates/recommendation_letter.txt"

# Audit rules
REQUIRED_COURSES = {
    "CSC101", "CSC102", "MTH101", "MTH102", "GST101"
}

# Allowed file formats
CSV_ENCODING = "utf-8"
DEFAULT_DATA_PATH = "data/students.csv"

# Logging settings (optional extension)
LOG_FILE_PATH = "logs/app.log"
ENABLE_FILE_LOGGING = False  # Set to True if using file-based logs

# Academic honors thresholds (optional extension)
HONORS = {
    "First Class": 4.50,
    "Second Class Upper": 3.50,
    "Second Class Lower": 2.40,
    "Third Class": 1.50,
}
