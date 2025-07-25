# CuResume - AI-Powered Resume Curation Tool

A web application that helps CS students tailor their LaTeX resumes to specific job applications using AI agents built with LangGraph.

## 🎯 Project Goals

- **Input**: LaTeX resume code + job application link
- **Process**: AI agent analyzes job requirements and suggests targeted edits
- **Output**: Curated resume with approval/rejection workflow (like Cursor editor)
- **Result**: Side-by-side diff view for easy copy-paste to LaTeX editor

## 🏗️ Architecture

```
curesume/
├── frontend/          # React + TypeScript UI
├── backend/           # FastAPI Python backend
├── agents/            # LangGraph AI agents
├── shared/            # Shared types and utilities
└── docs/              # Documentation
```

## 🛠️ Tech Stack

- **Frontend**: React, TypeScript, Tailwind CSS, Vite
- **Backend**: FastAPI, Python 3.11+
- **AI Framework**: LangGraph, OpenAI/Anthropic APIs
- **PDF Processing**: LaTeX compilation tools
- **Database**: SQLite → PostgreSQL (production)
- **Development**: Docker, Poetry/pip

## 🚀 Development Phases

### Phase 1: Foundation (Current)
- [x] Project structure setup
- [ ] Basic React frontend with file upload
- [ ] FastAPI backend with basic endpoints
- [ ] LaTeX → PDF compilation pipeline

### Phase 2: Core Features
- [ ] Job posting analysis (web scraping/API)
- [ ] LangGraph agent for resume analysis
- [ ] Edit suggestion system
- [ ] Approval/rejection workflow UI

### Phase 3: Advanced Features
- [ ] Side-by-side diff viewer
- [ ] Edit history and version control
- [ ] Multiple resume templates
- [ ] Analytics and feedback loop

## 🎓 Learning Objectives

This project teaches:
- Full-stack web development
- AI agent design with LangGraph
- LaTeX processing and PDF generation
- Real-time collaborative editing patterns
- API design and integration

## 📝 Getting Started

### Prerequisites
- Node.js 18+
- Python 3.11+
- LaTeX distribution (TeX Live recommended)
- OpenAI/Anthropic API key

### Setup
```bash
# Clone and setup
git clone <repo-url>
cd curesume

# Setup backend
cd backend
pip install -r requirements.txt

# Setup frontend
cd ../frontend
npm install

# Start development servers
npm run dev        # Frontend (port 3000)
python -m uvicorn main:app --reload  # Backend (port 8000)
```

## 📚 Documentation

See `docs/` directory for:
- API documentation
- Agent workflow diagrams
- LaTeX processing guide
- Deployment instructions 