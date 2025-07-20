from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.search import router as search_router
# from app.routes.llm import router as llm_router  # Uncomment if using LLM

app = FastAPI(title="Search Agent API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(search_router, prefix="/search", tags=["Search"])
# app.include_router(llm_router, prefix="/llm", tags=["LLM"])  # Optional

@app.get("/")
def read_root():
    return {"message": "Welcome to the Search Agent API"}