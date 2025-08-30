# gradecalc/core/analytics.py

from rich.console import Console
from rich.table import Table
import pandas as pd


class GPAAnalytics:
    def __init__(self):
        self.console = Console()

    def plot_gpa_trend(self, df: pd.DataFrame, student_name: str) -> None:
        if df.empty or not {'semester', 'grade_points', 'credits'}.issubset(df.columns):
            self.console.print("[bold red]No GPA data available to display.[/bold red]")
            return

        table = Table(title=f"📈 GPA Trend for {student_name}", title_style="bold cyan")
        table.add_column("Semester", justify="left", style="magenta")
        table.add_column("GPA", justify="right", style="green")

        # Sort semester labels properly (e.g., "Spring 2023", "Fall 2023")
        try:
            semesters = sorted(df['semester'].unique(), key=lambda x: (x.split()[-1], x.split()[0]))
        except Exception:
            semesters = df['semester'].unique()

        for semester in semesters:
            sem_df = df[df['semester'] == semester]
            total_credits = sem_df['credits'].sum()
            gpa = sem_df['grade_points'].sum() / total_credits if total_credits else 0.0
            table.add_row(str(semester), f"{gpa:.2f}")

        self.console.print(table)
