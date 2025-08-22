"""
ScrAI API Backend - FastAPI Edition
Main application entry point with CLI support
"""

import asyncio
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import typer

from app.core.config import settings
from app.core.database import init_db
from app.api.routes import router as api_router
from app.cli.app import app as cli_app

# FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    await init_db()

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to ScrAI API", "version": settings.VERSION}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

# CLI app
cli = typer.Typer()
cli.add_typer(cli_app, name="cli")

@cli.command()
def serve(
    host: str = "0.0.0.0",
    port: int = 8000,
    reload: bool = True
):
    """Start the FastAPI server"""
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )

@cli.command()
def dev():
    """Start development server with hot reload"""
    serve(host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    cli()
