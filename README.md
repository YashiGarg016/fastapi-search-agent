# FastAPI Search Agent

A modern FastAPI-based backend and React frontend application that enables smart search aggregation from multiple search providers (Google, DuckDuckGo, Bing, Brave, etc.) and displays unified results in a clean web interface.

> **Note:** This project is ongoing and under active development. Features and APIs may change.

## Features

- **Unified Search API**: Query multiple search engines with a single API call.
- **Pluggable Providers**: Easily extend to support more search engines.
- **LLM Integration**: Summarize or answer questions based on search results using OpenAI, Cohere, or HuggingFace models.
- **Frontend**: React-based UI for instant search and result display.
- **Async & Fast**: Built with FastAPI and httpx for high performance.

## Project Structure

```
.
├── app/                # FastAPI backend
│   ├── main.py         # FastAPI app entrypoint
│   ├── routes/         # API route definitions
│   ├── services/       # Search provider logic
│   └── utils/          # LLM and chain utilities
├── frontend/           # React frontend
│   ├── src/            # React source code
│   └── public/         # Static assets
├── .env                # API keys and secrets
├── requirements.txt    # Python dependencies
```

## Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/fastapi-search-agent.git
cd fastapi-search-agent
```

### 2. Backend Setup

1. **Install Python dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

2. **Configure Environment Variables:**

    Copy `.env.example` to `.env` and fill in your API keys for Google, Bing, Brave, OpenAI, Cohere, etc.

3. **Run FastAPI server:**

    ```sh
    uvicorn app.main:app --reload
    ```

    The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 3. Frontend Setup

1. **Install Node dependencies:**

    ```sh
    cd frontend
    npm install
    ```

2. **Start the React app:**

    ```sh
    npm start
    ```

    The frontend will be available at [http://localhost:3000](http://localhost:3000).

## API Usage

- **Search Endpoint:**  
  `GET /search?query=your+search+term`  
  Returns aggregated results from available providers.

- **LLM Endpoint (optional):**  
  `POST /llm`  
  Use for summarization or Q&A over search results (requires LLM setup).

## Adding New Search Providers

Extend `app/services/search_providers.py` with new async functions for each provider and update the `perform_search` logic.

## Environment Variables

See `.env` for required API keys:

- `GOOGLE_API_KEY`, `GOOGLE_CSE_ID`
- `BING_API_KEY`
- `BRAVE_API_KEY`
- `OPENAI_API_KEY`
- `COHERE_API_KEY`
- `HF_API_KEY`


