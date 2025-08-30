📦 requirements.md

markdown
Copy
Edit
# 📦 Requirements Documentation

This document outlines the external Python libraries required for the GPA & Transcript Generator CLI application. These packages are listed in `requirements.txt` and must be installed before running the program.

---

## 🧪 Installation

To install all required packages, use:


pip install -r requirements.txt
📚 Dependencies Overview
1. rich
📌 Version: latest stable

📦 PyPI name: rich

📝 Description: A Python library for rich text and beautiful formatting in the terminal. It is used for styling tables, headers, and GPA transcripts to make the command-line output visually appealing.

🔗 Website: https://pypi.org/project/rich/


pip install rich
🔍 Verifying Installation
To check that all required packages are installed, run:


pip freeze
Ensure rich appears in the output.

⚠️ Notes
This project is lightweight and only depends on rich as an external package.

No database or web server dependencies are required.

Python standard libraries like csv, datetime, and os are used and do not require installation.

📂 requirements.txt Contents

pandas>=1.5.0
matplotlib>=3.6.0
tabulate>=0.9.0      # For pretty table outputs in CLI
Jinja2>=3.1.0        # Optional: For generating letters/reports with templates
rich>=13.0.0         # Optional: For colorful/fancy CLI output

Keep your requirements.txt file updated when adding new packages in the future.