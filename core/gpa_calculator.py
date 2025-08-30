import pandas as pd
from rich.console import Console


class GPACalculator:
    GRADE_MAP = {
        "A": 5.0,
        "B": 4.0,
        "C": 3.0,
        "D": 2.0,
        "E": 1.0,
        "F": 0.0
    }

    def __init__(self):
        self.console = Console()

    def calculate(self, df: pd.DataFrame) -> tuple[float, int] | tuple[None, int]:
        """
        Calculate GPA and total credits from a DataFrame.

        Args:
            df (pd.DataFrame): Must contain 'grade' and 'credit' columns.

        Returns:
            Tuple containing (gpa: float, total_credits: int) or (None, 0) on error.
        """
        try:
            df["grade_point"] = df["grade"].map(self.GRADE_MAP)

            if df["grade_point"].isnull().any():
                missing_grades = df[df["grade_point"].isnull()]["grade"].unique()
                raise ValueError(f"Invalid grade(s) found: {', '.join(missing_grades)}")

            df["weighted_point"] = df["grade_point"] * df["credit"]
            total_credits = df["credit"].sum()
            total_weighted = df["weighted_point"].sum()

            if total_credits == 0:
                raise ValueError("Total credits cannot be zero.")

            gpa = total_weighted / total_credits
            return round(gpa, 2), total_credits

        except Exception as e:
            self.console.print(f"[bold red]❌ Error calculating GPA:[/bold red] {e}")
            return None, 0
