import sys
import os
import argparse
from rich.console import Console
from rich.panel import Panel

sys.path.append(os.path.dirname(__file__))

from utils.file_io import load_student_data
from core.gpa_calculator import GPACalculator
from core.transcript_generator import TranscriptGenerator
from core.analytics import GPAAnalytics
from core.audit import GraduationAuditor
from core.recommendation import RecommendationLetterGenerator

console = Console()

def main():
    parser = argparse.ArgumentParser(description="🎓 Student Grade Management CLI")
    parser.add_argument("--csv", type=str, default="data/students.csv", help="Path to CSV file")
    parser.add_argument("--student-id", type=int, required=True, help="Student ID to load")
    parser.add_argument("--recommend", action="store_true", help="Generate recommendation letter")

    args = parser.parse_args()

    # 🔄 Load student data
    student_df = load_student_data(args.csv, args.student_id)

    if student_df.empty:
        console.print("[bold red]❌ No student data found or error loading.[/]")
        return

    student_name = student_df.iloc[0]["name"]
    console.rule(f"[bold cyan]🧾 Transcript for {student_name}[/]")

    # 🧾 Generate Transcript
    TranscriptGenerator().generate(student_df, student_name)

    # 📊 GPA Calculation
    calculator = GPACalculator()
    gpa, total_credits = calculator.calculate(student_df)

    if gpa is not None:
        console.print(Panel.fit(
            f"[bold yellow]📚 GPA:[/] {gpa:.2f}\n[bold yellow]🎯 Total Credits:[/] {total_credits}",
            title="📊 Academic Summary",
            border_style="magenta"
        ))

        # 📈 GPA Trend Visualization
        GPAAnalytics().plot_gpa_trend(student_df, student_name)

        # 🎓 Degree Audit
        auditor = GraduationAuditor()
        result = auditor.check_eligibility(total_credits, gpa)
        auditor.display_eligibility(result)

        # ✉️ Recommendation Letter (if requested)
        if args.recommend:
            console.rule("[bold green]📬 Recommendation Letter")
            try:
                recommender = RecommendationLetterGenerator(data_path=args.csv)
                recommender.generate(student_name, gpa)
            except Exception as e:
                console.print(f"[bold red]❌ Failed to generate recommendation letter:[/] {e}")

if __name__ == "__main__":
    main()
