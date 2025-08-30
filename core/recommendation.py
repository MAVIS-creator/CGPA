import pandas as pd
from rich.console import Console
from rich.panel import Panel
from datetime import datetime
import os


class RecommendationLetterGenerator:
    def __init__(self, data_path="data/students.csv", output_path="templates/recommendation_letter.txt"):
        self.console = Console()
        self.data_path = data_path
        self.output_path = output_path

    def generate(self, student_name: str, gpa: float) -> None:
        try:
            df = pd.read_csv(self.data_path)

            if "name" not in df.columns:
                raise KeyError("Column 'name' not found in students.csv")

            match = df[df["name"].str.lower() == student_name.lower()]
            if match.empty:
                self.console.print(f"[red]❌ Error:[/] Student '{student_name}' not found in the database.")
                return

            student = match.iloc[0]
            department = student.get("department", "Department")
            level = student.get("level", "Unknown")
            full_name = student.get("name", student_name)

            # Construct letter
            letter = f"""
To Whom It May Concern,

I am pleased to write this letter of recommendation for {full_name}, a student of the {department} department. 
Throughout their academic journey, {full_name} has consistently demonstrated a high level of dedication, 
critical thinking, and excellence in their coursework.

Currently at level {level}, {full_name} has achieved a commendable GPA of {gpa:.2f}. 
This speaks volumes about their intellectual capabilities and strong work ethic.

It is without hesitation that I recommend {full_name} for any academic or professional opportunity they may seek. 
I am confident that they will continue to excel and bring value to any institution or organization.

Sincerely,
Dr. A.I. Recommender
Faculty Advisor  
Date: {datetime.now().strftime('%Y-%m-%d')}
""".strip()

            self.console.print(Panel(letter, title="📬 Recommendation Letter", expand=False, border_style="cyan"))

            # Ensure template directory exists
            os.makedirs(os.path.dirname(self.output_path), exist_ok=True)

            # Save to file
            with open(self.output_path, "w", encoding="utf-8") as f:
                f.write(letter)

            self.console.print(
                f"\n[green]✅ Recommendation letter saved to:[/] [bold]{self.output_path}[/bold]"
            )

        except Exception as e:
            self.console.print(f"[bold red]❌ Error generating recommendation letter:[/bold red] {e}")
