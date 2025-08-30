# utils/file_io.py

import pandas as pd
from rich.console import Console
from rich.panel import Panel

console = Console()

def load_student_data(file_path: str, student_id: int) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        student_df = df[df["student_id"] == student_id]

        if student_df.empty:
            raise ValueError(f"No data found for student ID {student_id}")

        return student_df.reset_index(drop=True)

    except FileNotFoundError:
        console.print(
            Panel(f"❌ File not found: [bold yellow]{file_path}[/bold yellow]", title="File Error", style="bold red")
        )
        return pd.DataFrame()
    except Exception as e:
        console.print(
            Panel(f"⚠️ Error loading data: [italic]{e}[/italic]", title="Unexpected Error", style="bold red")
        )
        return pd.DataFrame()

def save_transcript_to_file(transcript_text: str, student_id: int) -> None:
    try:
        path = f"data/transcripts/transcript_{student_id}.txt"
        with open(path, "w", encoding="utf-8") as file:
            file.write(transcript_text)
        console.print(f"✅ Transcript saved to [green]{path}[/green]")
    except Exception as e:
        console.print(
            Panel(f"❌ Failed to save transcript: {e}", title="Write Error", style="bold red")
        )
