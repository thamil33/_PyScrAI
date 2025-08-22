"""
Main CLI application for ScrAI
"""
import typer
import asyncio
from typing import Optional

from app.core.config import settings
from app.cli.commands import chat, tulpa, session

# Create the main CLI app
app = typer.Typer(
    name="scrai",
    help="ScrAI - AI SoulSculpting Platform with CLI Interface",
    add_completion=False,
)

# Add command groups
app.add_typer(chat.app, name="chat", help="Interactive chat commands")
app.add_typer(tulpa.app, name="tulpa", help="Tulpa management commands")
app.add_typer(session.app, name="session", help="Session management commands")

@app.command()
def version():
    """Show version information"""
    typer.echo(f"ScrAI v{settings.VERSION}")

@app.command()
def info():
    """Show system information"""
    typer.echo(f"ScrAI - {settings.DESCRIPTION}")
    typer.echo(f"Version: {settings.VERSION}")
    typer.echo(f"LLM Provider: {settings.LLM_API_PROVIDER}")
    typer.echo(f"Default Model: {settings.DEFAULT_MODEL}")
    typer.echo(f"Database: {settings.POSTGRES_DB}")

@app.callback()
def main_callback():
    """Main CLI callback"""
    pass

if __name__ == "__main__":
    app()
