"""
Session management command module
"""
import typer
from typing import Optional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Create the session command group
app = typer.Typer()
console = Console()

@app.command()
def list():
    """List all chat sessions"""
    table = Table(title="Chat Sessions")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Messages", style="yellow", justify="right")
    table.add_column("Created", style="blue")
    table.add_column("Last Updated", style="green")

    # TODO: Fetch from database
    table.add_row("1", "Getting to know Echo", "15", "2024-01-15 10:30", "2024-01-15 11:45")
    table.add_row("2", "Philosophy discussion", "8", "2024-01-16 14:20", "2024-01-16 15:30")

    console.print(table)

@app.command()
def create(
    title: str = typer.Argument(..., help="Title for the new session"),
    tulpa_id: Optional[int] = typer.Option(None, help="Tulpa to associate with this session")
):
    """Create a new chat session"""
    console.print(Panel.fit(
        f"[bold green]Creating Session[/bold green]\n"
        f"Title: {title}\n"
        f"Tulpa ID: {tulpa_id or 'None'}",
        title="New Session",
        border_style="green"
    ))
    console.print("[yellow]Session creation feature coming soon![/yellow]")

@app.command()
def switch(session_id: int = typer.Argument(..., help="Session ID to switch to")):
    """Switch to a different session"""
    console.print(f"[blue]Switching to session {session_id}...[/blue]")
    console.print("[yellow]Session switching feature coming soon![/yellow]")

@app.command()
def delete(
    session_id: int = typer.Argument(..., help="Session ID to delete"),
    force: bool = typer.Option(False, help="Force deletion without confirmation")
):
    """Delete a session and all its messages"""
    if not force:
        typer.confirm(f"Are you sure you want to delete session {session_id} and all its messages?", abort=True)

    console.print(f"[red]Deleting session {session_id}...[/red]")
    console.print("[yellow]Session deletion feature coming soon![/yellow]")

@app.command()
def export(
    session_id: int = typer.Argument(..., help="Session ID to export"),
    format: str = typer.Option("json", help="Export format: json, markdown, txt"),
    output: Optional[str] = typer.Option(None, help="Output file path")
):
    """Export a session to a file"""
    output_file = output or f"session_{session_id}.{format}"
    console.print(Panel.fit(
        f"[bold blue]Exporting Session[/bold blue]\n"
        f"Session ID: {session_id}\n"
        f"Format: {format}\n"
        f"Output: {output_file}",
        title="Export Session",
        border_style="blue"
    ))
    console.print("[yellow]Session export feature coming soon![/yellow]")

@app.command()
def current():
    """Show information about the current session"""
    console.print(Panel.fit(
        "[bold cyan]Current Session Info[/bold cyan]\n"
        "Session ID: 1\n"
        "Title: Getting to know Echo\n"
        "Messages: 15\n"
        "Tulpa: Echo (ID: 1)\n"
        "Status: Active",
        title="Current Session",
        border_style="cyan"
    ))
