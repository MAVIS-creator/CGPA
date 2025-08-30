# utils/logger.py

from rich.console import Console

console = Console()

def log_info(message: str):
    console.print(f"[bold green]INFO:[/bold green] {message}")

def log_warning(message: str):
    console.print(f"[bold yellow]WARNING:[/bold yellow] {message}")

def log_error(message: str):
    console.print(f"[bold red]ERROR:[/bold red] {message}")
