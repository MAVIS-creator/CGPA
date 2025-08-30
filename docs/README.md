<h1 align="center">🎓 GradeCalc – Student GPA Calculator & Transcript Generator (CLI)</h1>

<p align="center">
  <b>GradeCalc</b> is a Python-based command-line application that helps manage academic records.<br>
  It calculates student GPAs, generates transcripts, audits graduation eligibility, analyzes GPA trends, 
  and creates recommendation letters — all from CSV data.
</p>

<p align="center">
  <i>Lightweight, modular, and depends only on the Python Standard Library + 
  <a href="https://github.com/Textualize/rich">rich</a> for styled CLI output.</i>
</p>

<hr>

<h2>✨ Features</h2>
<ul>
  <li>📊 <b>GPA Calculation</b> on a 5.0 scale</li>
  <li>🗂️ <b>Transcript Generation</b> (semester-wise)</li>
  <li>🎓 <b>Graduation Eligibility Audit</b> (based on GPA & credits)</li>
  <li>📝 <b>Recommendation Letter Generation</b></li>
  <li>📈 <b>GPA Trend Analysis</b> across semesters</li>
  <li>🖥️ <b>CLI-only interface</b> (no GUI dependencies)</li>
  <li>🔧 <b>Modular & Object-Oriented Architecture</b></li>
  <li>📦 <b>Lightweight</b>: only requires Python + <code>rich</code></li>
</ul>

<hr>

<h2>📁 Project Structure</h2>

<pre>
gradecalc/
├── main.py                 # CLI entry point
├── cli_menu.py             # CLI menu interactions (optional)
├── config.py               # Constants (grading scale, etc.)

├── core/                   # Core application logic
│   ├── gpa_calculator.py   # GPA computation logic
│   ├── transcript_generator.py # Transcript output logic
│   ├── analytics.py        # GPA trend analysis
│   ├── audit.py            # Graduation eligibility checker
│   ├── recommendation.py   # Recommendation letter generator
│   ├── student.py          # Student object class
│   └── course.py           # Course object class

├── utils/                  # Helper utilities
│   ├── file_io.py          # File read/write helpers
│   ├── input_validator.py  # Input validation functions
│   └── logger.py           # Log handling (optional)

├── data/                   # Input & output data
│   ├── students.csv        # Input student records
│   └── transcripts/        # Generated transcripts

├── templates/              # Text templates
│   ├── recommendation_letter.txt
│   └── transcript_template.txt

├── tests/                  # Unit tests
│   ├── test_gpa_calculator.py
│   ├── test_audit.py
│   └── test_transcript_generator.py

├── docs/                   # Documentation
│   ├── README.md           # Project overview
│   ├── USER_GUIDE.md       # CLI usage instructions
│   ├── REQUIREMENTS.md     # Functional requirements
│   └── TECHNICAL_DOC.md    # Technical documentation

└── requirements.txt        # Python dependencies (only `rich`)
</pre>

<hr>

<h2>🖥️ Requirements</h2>
<ul>
  <li>Python 3.7+</li>
  <li><a href="https://pypi.org/project/rich/">rich</a> (for styled CLI output)</li>
</ul>

<p>Install <code>rich</code>:</p>

<pre><code>pip install rich</code></pre>

<hr>

<h2>🚀 Usage</h2>

<ol>
  <li><b>Clone the repository</b></li>
</ol>

<pre><code>git clone https://github.com/your-username/gradecalc.git
cd gradecalc
</code></pre>

<ol start="2">
  <li><b>Prepare your student data</b></li>
</ol>

<p>Place your <code>students.csv</code> file inside <code>data/</code>.</p>

<ol start="3">
  <li><b>Run the CLI</b></li>
</ol>

<pre><code>python main.py --student-id 2023001111</code></pre>

<ol start="4">
  <li><b>Generate transcript + recommendation letter</b></li>
</ol>

<pre><code>python main.py --student-id 2023001111 --recommend</code></pre>

<ol start="5">
  <li><b>Optional: specify a custom CSV path</b></li>
</ol>

<pre><code>python main.py --csv data/students.csv --student-id 2023001111</code></pre>

<hr>

<h2>🧪 Running Tests</h2>

<p>Run all tests:</p>
<pre><code>python -m unittest discover</code></pre>

<p>Run a specific test:</p>
<pre><code>python -m unittest tests.test_gpa_calculator</code></pre>

<hr>

<h2>🗃️ Sample Data Format (<code>students.csv</code>)</h2>

<pre><code>student_id,name,department,level,course,credit,grade,semester
2023001111,Alice Smith,Computer Science,400,CSC202,3,A,Fall 2023
</code></pre>

<hr>

<h2>✍️ Author</h2>
<p>👤 <b>ADEG</b></p>

<hr>

<h2>📜 License</h2>
<p>This project is licensed under the <b>MIT License</b> (or your preferred license).</p>

<hr>

<h2>📎 Related Files</h2>
<ul>
  <li>templates/recommendation_letter.txt</li>
  <li>templates/transcript_template.txt</li>
  <li>data/students.csv</li>
</ul>
