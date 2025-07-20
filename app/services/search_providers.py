import httpx
import os
from dotenv import load_dotenv

load_dotenv()

async def google_search(query: str):
    key = os.getenv("GOOGLE_API_KEY")
    cx = os.getenv("GOOGLE_CSE_ID")
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={key}&cx={cx}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json().get("items", [])

async def duckduckgo_search(query: str):
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json().get("RelatedTopics", [])

async def perform_search(query: str):
    try:
        return await google_search(query)
    except Exception:
        return await duckduckgo_search(query)