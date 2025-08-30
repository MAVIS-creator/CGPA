from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel
from utils.file_io import load_student_data, save_transcript_to_file
from utils.input_validator import validate_student_id
from utils.logger import log_info, log_warning, log_error
from core.transcript_generator import TranscriptGenerator
from core.audit import GraduationAuditor
from core.recommendation import RecommendationLetterGenerator
import os

console = Console()
DATA_PATH = os.path.join("data", "students.csv")

def main_menu():
    console.print(Panel("🎓 [bold cyan]Student Grade Management CLI[/bold cyan]", style="green"))

    while True:
        console.print("\n[bold yellow]Main Menu:[/bold yellow]")
        console.print("[1] View Transcript")
        console.print("[2] Run Degree Audit")
        console.print("[3] Generate Recommendation Letter")
        console.print("[4] Exit")

        choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4"])

        if choice == "4":
            log_info("Exited the application.")
            console.print("\n👋 Goodbye!")
            break

        try:
            raw_input = IntPrompt.ask("Enter student ID")
            student_id = validate_student_id(raw_input)
            student_df = load_student_data(DATA_PATH, student_id)

            if student_df.empty:
                log_warning(f"No data found for student ID {student_id}")
                continue

            student_name = student_df.iloc[0]["name"]

            if choice == "1":
                transcript = TranscriptGenerator().generate(student_df, student_name)
                save_transcript_to_file(transcript, student_id)
                log_info(f"Transcript generated and saved for student ID {student_id}")

            elif choice == "2":
                GraduationAuditor().check(student_df, student_name)
                log_info(f"Degree audit completed for student ID {student_id}")

            elif choice == "3":
                RecommendationLetterGenerator().generate(student_df, student_name)
                log_info(f"Recommendation letter generated for student ID {student_id}")

        except ValueError as ve:
            log_error(str(ve))
            console.print(f"[red]Input Error:[/red] {ve}")

        except Exception as e:
            log_error(str(e))
            console.print(f"[red]Unexpected Error:[/red] {e}")

if __name__ == "__main__":
    main_menu()
