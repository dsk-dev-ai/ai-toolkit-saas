# AI Toolkit SaaS

AI-powered content generation platform using Google Gemini and FastAPI.

## Features

- Blog, tweet, and YouTube script generation via Gemini AI
- Bearer-token authentication
- Per-token daily rate limiting
- Prompt-level response caching
- CORS-protected frontend integration

## Setup

### Backend

```bash
cd backend
pip install -r requirements.txt

# Copy and edit environment variables
cp ../.env.example ../.env
# Edit .env with your GEMINI_API_KEY and a secret API_TOKEN
```

### Frontend

```bash
cd frontend
npm install
npm start
```

The React app runs on `http://localhost:3000` by default.

## Running

```bash
cd backend
uvicorn app.main:app --reload --port 8000
```

## API Usage

### `POST /generate`

Requires a valid Bearer token in the `Authorization` header.

```bash
curl -X POST http://127.0.0.1:8000/generate \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"topic": "AI tools for students"}'
```

**Response:**

```json
{
  "result": "...",
  "source": "ai"
}
```

### `GET /health`

```bash
curl http://127.0.0.1:8000/health
```

## License

MIT
