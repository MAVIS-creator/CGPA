<!-- ===========================
   🎓 GradeCalc CLI – HTML README
   Paste directly into README.md
   =========================== -->

<!-- Gradient Neon Banner (auto-generated) -->
<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=rect&color=0:00FFC6,100:6A00FF&height=120&section=header&text=GradeCalc%20CLI%20Project&fontSize=42&fontColor=ffffff&fontAlign=50&fontAlignY=60"
    alt="GradeCalc CLI Project - Neon Gradient Banner"
  />
</p>

<!-- Animated Typing Tagline -->
<p align="center">
  <img
    src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1200&center=true&vCenter=true&width=720&height=45&duration=3500&lines=GPA+Calculator+%7C+Transcript+Generator+%7C+Graduation+Audit;Python+%2B+Rich+Terminal+UI+%7C+Fast+Lightweight+Modular"
    alt="Animated Typing Tagline"
  />
</p>

<!-- Tech / Meta Badges -->
<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Python-3.7%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.7+"></a>
  <a href="#"><img src="https://img.shields.io/badge/CLI-Application-2E8B57?style=for-the-badge&logo=gnu-bash&logoColor=white" alt="CLI App"></a>
  <a href="#"><img src="https://img.shields.io/badge/Made%20with-Rich-8A2BE2?style=for-the-badge" alt="Rich"></a>
  <a href="#"><img src="https://img.shields.io/badge/License-MIT-ffcc00?style=for-the-badge&logo=open-source-initiative&logoColor=black" alt="MIT"></a>
  <a href="#"><img src="https://img.shields.io/badge/PRs-Welcome-00B894?style=for-the-badge&logo=github" alt="PRs Welcome"></a>
</p>

<!-- Section Divider -->
<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=rect&color=0:6A00FF,100:00FFC6&height=8&section=footer"
    alt=""
  />
</p>

<!-- Title + Short Pitch -->
<h1 align="center">📊 GradeCalc – Student GPA Calculator & Transcript Generator (CLI)</h1>
<p align="center">
  A sleek, no-nonsense <b>command-line</b> tool that calculates GPAs, generates <b>semester transcripts</b>,
  performs <b>graduation audits</b>, and can draft <b>recommendation letters</b> — all from CSV data,
  with a polished terminal experience using <code>rich</code>.
</p>

<!-- Features -->
<h2>✨ Features</h2>
<ul>
  <li>📈 <b>GPA Calculation</b> on a 5.0 scale (configurable)</li>
  <li>🗂️ <b>Semester-wise Transcript Generation</b> (CSV in → formatted out)</li>
  <li>🎓 <b>Graduation Eligibility Audit</b> (GPA & total credits rules)</li>
  <li>📝 <b>Recommendation Letter Builder</b> (templated)</li>
  <li>📉 <b>GPA Trend Analysis</b> across semesters</li>
  <li>🧱 <b>Modular, OOP Architecture</b> (clean, testable)</li>
  <li>🖥️ <b>CLI-only</b> (zero GUI deps; Python stdlib + <code>rich</code>)</li>
</ul>

<!-- Section Divider -->
<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=rect&color=0:00FFC6,100:6A00FF&height=8&section=footer"
    alt=""
  />
</p>

<!-- Project Structure -->
<h2>📁 Project Structure</h2>
<pre>
gradecalc/
├─ main.py                     # CLI entry point
├─ cli_menu.py                 # (optional) menu interactions
├─ config.py                   # grading scale, constants

├─ core/                       # core logic
│  ├─ gpa_calculator.py
│  ├─ transcript_generator.py
│  ├─ analytics.py
│  ├─ audit.py
│  ├─ recommendation.py
│  ├─ student.py
│  └─ course.py

├─ utils/                      # helpers
│  ├─ file_io.py
│  ├─ input_validator.py
│  └─ logger.py                # (optional)

├─ data/
│  ├─ students.csv             # input data
│  └─ transcripts/             # generated outputs

├─ templates/
│  ├─ recommendation_letter.txt
│  └─ transcript_template.txt  # (optional)

├─ tests/
│  ├─ test_gpa_calculator.py
│  ├─ test_audit.py
│  └─ test_transcript_generator.py

├─ docs/
│  ├─ README.md
│  ├─ USER_GUIDE.md
│  ├─ REQUIREMENTS.md
│  └─ TECHNICAL_DOC.md

└─ requirements.txt            # only `rich`
</pre>

<!-- Quickstart -->
<h2>⚙️ Setup & Installation</h2>
<pre>
# 1) Clone
git clone https://github.com/your-username/gradecalc-cli.git
cd gradecalc-cli

# 2) (Optional) create venv
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 3) Install deps
pip install -r requirements.txt
# or just
pip install rich
</pre>

<!-- Usage -->
<h2>🚀 Usage</h2>
<pre>
# Basic: compute by student ID
python main.py --student-id 2023001111

# Also generate recommendation letter
python main.py --student-id 2023001111 --recommend

# Use a custom CSV path
python main.py --csv data/students.csv --student-id 2023001111
</pre>

<!-- Tests -->
<h2>🧪 Running Tests</h2>
<pre>
# Run all tests
python -m unittest discover

# Run specific test module
python -m unittest tests.test_gpa_calculator
</pre>

<!-- Sample Data -->
<h2>🗃️ Sample CSV (students.csv)</h2>
<pre>
student_id,name,department,level,course,credit,grade,semester
2023001111,Alice Smith,Computer Science,400,CSC202,3,A,Fall 2023
</pre>

<!-- Section Divider -->
<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=rect&color=0:6A00FF,100:00FFC6&height=8&section=footer"
    alt=""
  />
</p>

<!-- Authors with Badges -->
<h2>✍️ Authors</h2>

<table>
  <tr>
    <td align="center" width="50%">
      <a href="https://github.com/Precious07-Ade">
        <img src="https://github.com/Precious07-Ade.png?size=120" width="120" height="120" style="border-radius:50%;" alt="Precious07-Ade Avatar"/><br/>
        <sub><b>Precious07-Ade</b></sub>
      </a>
      <br/>
      <i>👑 Main Author</i>
      <br/><br/>
      <!-- Main Author badges -->
      <a href="https://github.com/Precious07-Ade">
        <img src="https://img.shields.io/badge/Follow-Precious07--Ade-0A66C2?style=for-the-badge&logo=github" alt="Follow Precious"/>
      </a>
      <a href="https://github.com/Precious07-Ade?tab=repositories">
        <img src="https://img.shields.io/badge/Repos-Explore-6A00FF?style=for-the-badge&logo=github" alt="Repos"/>
      </a>
    </td>
    <td align="center" width="50%">
      <a href="https://github.com/MAVIS-Creator">
        <img src="https://github.com/Precious07-Ade.png?size=120" width="120" height="120" style="border-radius:50%;" alt="MAVIS_Creator avatar"/><br/>
        <sub><b>MAVIS-Creator</b></sub>
      </a>
      <br/>
      <i>🤝 Co-Author</i>
      <br/><br/>
      <a href="https://github.com/MAVIS-Creator">
        <img src="https://img.shields.io/badge/Follow-MAVIS--Creator-9B59B6?style=for-the-badge&logo=github" alt="Follow Mavis"/>
      </a>
      <a href="https://github.com/MAVIS-Creator?tab=repositories">
        <img src="https://img.shields.io/badge/Repos-Explore-00B894?style=for-the-badge&logo=github" alt="Repos"/>
      </a>
    </td>
  </tr>
</table>

<!-- Extra CTA badge row (optional) -->
<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Contributions-Welcome-27AE60?style=for-the-badge&logo=git" alt="Contributions Welcome"></a>
  <a href="#"><img src="https://img.shields.io/badge/Good%20First%20Issues-Available-F39C12?style=for-the-badge" alt="Good First Issues"></a>
</p>

<!-- License -->
<h2>📜 License</h2>
<p>
  Licensed under the <b>MIT License</b>. You’re free to use, modify, and distribute with attribution.
</p>

<!-- Footer Divider -->
<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=rect&color=0:00FFC6,100:6A00FF&height=8&section=footer"
    alt=""
  />
</p>

<!-- Footer Note -->
<p align="center">
  Made with ❤️ by
  <a href="https://github.com/Precious07-Ade">Precious07-Ade</a>
  &amp;
  <a href="https://github.com/MAVIS-Creator">MAVIS-Creator</a>.
</p>
