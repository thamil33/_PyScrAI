# ScrAI - AI SoulSculpting Platform

A FastAPI-based AI companion platform with CLI-first design, featuring tulpa (AI companion) management, conversation tracking, and extensible memory systems.

## 🚀 Quick Start

### 1. Setup Environment
```bash
# Clone and navigate to project
cd d:/dev/_pyscrai/_PyScrAI

# Activate virtual environment
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment
Create `.env` file:
```env
# Database
POSTGRES_SERVER=localhost
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_DB=scriptorium

# LLM Configuration
LLM_API_PROVIDER=openrouter
OPENROUTER_API_KEY=your_api_key
DEFAULT_MODEL=openai/gpt-4o-mini
```

### 3. Initialize Database
```bash
python main.py serve  # This will create tables automatically
```

## 🎯 CLI Commands

### Main Commands
```bash
python main.py --help           # Show all commands
python main.py version          # Show version
python main.py info             # Show system info
```

### Chat Commands
```bash
python main.py chat interactive                    # Start interactive chat
python main.py chat ask "Hello, how are you?"     # Single message
python main.py chat history                       # Show chat history
python main.py chat history --session-id 1        # Session-specific history
```

### Tulpa Management
```bash
python main.py tulpa create "Echo"                            # Create new tulpa
python main.py tulpa create "Sage" --model claude-3-haiku     # With specific model
python main.py tulpa list                                     # List all tulpas
python main.py tulpa info 1                                   # Tulpa details
python main.py tulpa delete 1                                 # Delete tulpa
python main.py tulpa memory 1 add --content "New memory"      # Add memory
python main.py tulpa memory 1 list                            # List memories
```

### Session Management
```bash
python main.py session list                       # List all sessions
python main.py session create "My Chat Session"   # Create new session
python main.py session switch 1                   # Switch to session
python main.py session current                    # Show current session
python main.py session delete 1                   # Delete session
python main.py session export 1 --format json     # Export session
```

### Server Commands
```bash
python main.py serve                    # Start FastAPI server
python main.py serve --host 0.0.0.0 --port 8000
python main.py dev                      # Development server with reload
```

## 🔧 Development

### Project Structure
```
app/
├── cli/                    # Command Line Interface
│   ├── commands/          # CLI command modules
│   └── app.py             # Main CLI application
├── core/                  # Core functionality
│   ├── config.py          # Settings and configuration
│   └── database.py        # Database connection
├── models/                # SQLAlchemy models
│   ├── user.py
│   ├── conversation.py
│   ├── message.py
│   ├── tulpa.py
│   └── tulpa_memory.py
├── services/              # Business logic
│   └── llm_service.py     # LLM integration
└── api/                   # FastAPI routes (coming soon)
```

### Database Models
- **Users**: User accounts and preferences
- **Tulpas**: AI companions with personality traits
- **Conversations**: Chat sessions
- **Messages**: Individual chat messages
- **TulpaMemory**: Extensible memory system

## 🌐 API Endpoints (FastAPI)

### Chat Endpoints
```
POST   /api/v1/chat/completions          # Generate chat completion
GET    /api/v1/conversations            # List conversations
POST   /api/v1/conversations            # Create conversation
GET    /api/v1/conversations/{id}       # Get conversation
```

### Tulpa Endpoints
```
GET    /api/v1/tulpas                   # List tulpas
POST   /api/v1/tulpas                   # Create tulpa
GET    /api/v1/tulpas/{id}              # Get tulpa
PUT    /api/v1/tulpas/{id}              # Update tulpa
DELETE /api/v1/tulpas/{id}              # Delete tulpa
```

### Memory Endpoints
```
GET    /api/v1/tulpas/{id}/memories     # Get tulpa memories
POST   /api/v1/tulpas/{id}/memories     # Add memory
DELETE /api/v1/memories/{id}            # Delete memory
```

## 🛠️ Configuration

### Environment Variables
```env
# Project
PROJECT_NAME=ScrAI
VERSION=0.1.0

# Database
POSTGRES_SERVER=localhost
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=scriptorium

# LLM Providers
LLM_API_PROVIDER=openrouter
OPENROUTER_API_KEY=your_key
LM_STUDIO_URL=http://127.0.0.1:1234/v1

# Server
HOST=0.0.0.0
PORT=8000
DEBUG=true
```

## 📋 Requirements

- Python 3.8+
- PostgreSQL (recommended) or SQLite
- OpenRouter API key (or LM Studio)
- Virtual environment

## 🔄 Migration from Flask

This project has been migrated from Flask to FastAPI for:
- Better async support
- Automatic API documentation
- Type safety with Pydantic
- Improved performance
- Native CLI integration

## 🎯 Roadmap

- [x] FastAPI application structure
- [x] Database models with SQLAlchemy
- [x] CLI framework with Typer
- [x] LLM service integration
- [ ] Interactive chat mode
- [ ] API endpoints
- [ ] Web UI (future)
- [ ] Advanced memory systems
- [ ] Multi-user support

## 📝 Notes

- CLI is the primary interface (API is secondary)
- "Tulpa" replaces "Spark" terminology
- Memory system designed for extensibility
- Database uses "scriptorium" instead of default names
