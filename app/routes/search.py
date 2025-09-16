# from fastapi import APIRouter, Query
# from app.services.search_providers import google_search, duckduckgo_search

# router = APIRouter()

# @router.get("/")
# async def search(query: str = Query(...)):
#     google_raw = await google_search(query)
#     duck_raw = await duckduckgo_search(query)

#     # ✅ Tag and format Google results
#     google_results = [
#         {
#             "title": item.get("title"),
#             "link": item.get("link"),
#             "displayLink": item.get("displayLink"),
#             "snippet": item.get("snippet"),
#             "source": "google"
#         }
#         for item in google_raw
#     ] if google_raw else []

#     # ✅ Tag and format DuckDuckGo results
#     duck_results = [
#         {
#             "title": topic.get("Text"),
#             "link": topic.get("FirstURL"),
#             "displayLink": topic.get("FirstURL"),
#             "snippet": "",  # DuckDuckGo doesn't provide snippets
#             "source": "duckduckgo"
#         }
#         for topic in duck_raw
#         if "Text" in topic and "FirstURL" in topic
#     ] if duck_raw else []

#     return {
#         "google": google_results,
#         "duckduckgo": duck_results
#     }

# from fastapi import APIRouter, Query
# from app.services.search_providers import perform_search

# router = APIRouter()

# @router.get("/")
# async def search(query: str = Query(...)):
#     results = await perform_search(query)
#     return {"results": results}

from fastapi import APIRouter, Query
from services.search_providers import perform_search

router = APIRouter()

@router.get("/")
async def search(query: str = Query(...)):
    results = await perform_search(query)
    return {"results": results}
