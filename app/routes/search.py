from fastapi import APIRouter, Query
from app.services.search_providers import perform_search

router = APIRouter()

@router.get("/")
async def search(query: str = Query(...)):
    results = await perform_search(query)
    return {"results": results}