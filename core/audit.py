from rich.console import Console
from rich.table import Table
from rich.panel import Panel


class GraduationAuditor:
    def __init__(self, min_credits: int = 120, min_gpa: float = 2.0):
        self.console = Console()
        self.min_credits = min_credits
        self.min_gpa = min_gpa

    def check_eligibility(self, total_credits: int, gpa: float) -> dict:
        meets_credit = total_credits >= self.min_credits
        meets_gpa = gpa >= self.min_gpa
        status = "✅ Eligible" if meets_credit and meets_gpa else "❌ Not Eligible"

        return {
            "status": status,
            "total_credits": total_credits,
            "required_credits": self.min_credits,
            "gpa": round(gpa, 2),
            "required_gpa": self.min_gpa
        }

    def display_eligibility(self, result: dict) -> None:
        table = Table(title="🎓 Graduation Eligibility Status", title_style="bold magenta")
        table.add_column("Criteria", justify="left", style="cyan", no_wrap=True)
        table.add_column("Value", justify="right", style="white")

        table.add_row("Total Credits", str(result["total_credits"]))
        table.add_row("Required Credits", str(result["required_credits"]))
        table.add_row("GPA", str(result["gpa"]))
        table.add_row("Required GPA", str(result["required_gpa"]))

        status_color = "green" if "Eligible" in result["status"] else "red"
        status_panel = Panel.fit(
            f"[bold {status_color}]{result['status']}[/bold {status_color}]",
            border_style=status_color,
            title="Result",
            title_align="left"
        )

        self.console.print(table)
        self.console.print(status_panel)
