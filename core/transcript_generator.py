import pandas as pd
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from .gpa_calculator import GPACalculator

class TranscriptGenerator:
    def __init__(self):
        self.console = Console()

    def generate(self, df: pd.DataFrame, student_name: str) -> str:
        self.console.print(
            Panel.fit(
                f"[bold cyan]📄 OFFICIAL TRANSCRIPT FOR: {student_name}[/bold cyan]",
                border_style="green"
            )
        )

        grouped = df.groupby("semester")

        for semester, group in grouped:
            semester_title = Text(f"📘 Semester: {semester}", style="bold magenta")
            self.console.print(semester_title)

            table = Table(show_header=True, header_style="bold yellow", title=f"{semester} Courses")
            table.add_column("Course", style="dim")
            table.add_column("Credit")
            table.add_column("Grade")

            for _, row in group.iterrows():
                table.add_row(row["course"], str(row["credit"]), str(row["grade"]))

            self.console.print(table)
            self.console.print()

        # GPA Summary
        gpa_calculator = GPACalculator()
        gpa, total_credits = gpa_calculator.calculate(df)
        gpa_text = Text(
            f"📊 Cumulative GPA (5.0 scale): {gpa} | Total Credits: {total_credits}",
            style="bold white on blue"
        )
        self.console.print(gpa_text)
        self.console.rule()

        return f"{student_name}'s transcript rendered above using Rich 🎓"
