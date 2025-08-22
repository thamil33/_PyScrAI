"""
Chat command module for interactive conversations
"""
import typer
import asyncio
from typing import Optional
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text

from app.core.config import settings
from app.services.llm_service import LLMService

# Create the chat command group
app = typer.Typer()
console = Console()

@app.command()
def interactive(
    model: Optional[str] = typer.Option(None, help="Model to use for chat"),
    provider: Optional[str] = typer.Option(None, help="LLM provider to use"),
    tulpa: Optional[str] = typer.Option(None, help="Tulpa to chat with (by name or ID)")
):
    """Start an interactive chat session"""
    console.print(Panel.fit(
        f"[bold blue]ScrAI Interactive Chat[/bold blue]\n"
        f"Model: {model or settings.DEFAULT_MODEL}\n"
        f"Provider: {provider or settings.LLM_API_PROVIDER}",
        title="Welcome",
        border_style="blue"
    ))

    # TODO: Implement interactive chat loop
    console.print("[yellow]Interactive chat coming soon![/yellow]")

@app.command()
def ask(
    message: str = typer.Argument(..., help="Message to send to the AI"),
    model: Optional[str] = typer.Option(None, help="Model to use"),
    provider: Optional[str] = typer.Option(None, help="LLM provider to use"),
    tulpa: Optional[str] = typer.Option(None, help="Tulpa to chat with (by name or ID)")
):
    """Send a single message and get a response"""
    async def _ask():
        try:
            llm_service = LLMService()

            # Prepare tulpa-specific settings
            tulpa_provider = None
            tulpa_model = None

            if tulpa:
                # TODO: Look up tulpa by name or ID from database
                # For now, we'll show that tulpa-specific settings would be used
                console.print(f"[yellow]Using tulpa: {tulpa}[/yellow]")
                # Example: tulpa_provider and tulpa_model would be fetched from database
                # tulpa_provider = tulpa_record.provider
                # tulpa_model = tulpa_record.model_used

            response = await llm_service.generate_response(
                messages=[{"role": "user", "content": message}],
                model=model,
                provider=provider,
                tulpa_provider=tulpa_provider,
                tulpa_model=tulpa_model
            )

            console.print(Panel(
                response.content,
                title=f"AI Response ({response.provider}/{response.model})",
                border_style="green"
            ))

        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")

    asyncio.run(_ask())

@app.command()
def history(
    session_id: Optional[int] = typer.Option(None, help="Session ID to show history for"),
    limit: int = typer.Option(10, help="Number of messages to show")
):
    """Show chat history"""
    console.print(f"[yellow]Chat history for session {session_id or 'current'} (limit: {limit})[/yellow]")
    console.print("[yellow]History feature coming soon![/yellow]")
