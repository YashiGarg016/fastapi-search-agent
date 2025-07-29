import httpx
import os
from dotenv import load_dotenv

load_dotenv()

# 🌐 Google Search
async def google_search(query: str):
    key = os.getenv("GOOGLE_API_KEY")
    cx = os.getenv("GOOGLE_CSE_ID")
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={key}&cx={cx}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            return response.json().get("items", [])
        except Exception as e:
            print(f"Google search failed: {e}")
            return []

# 🦆 DuckDuckGo Search — now with nested topic support
async def duckduckgo_search(query: str):
    url = f"https://api.duckduckgo.com/?q={query}&format=json"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            return response.json().get("RelatedTopics", [])
        except Exception as e:
            print(f"DuckDuckGo search failed: {e}")
            return []

# 🔍 Perform search using both providers
async def perform_search(query: str):
    google_results = await google_search(query)
    duck_raw = await duckduckgo_search(query)

    duck_results = []

    for topic in duck_raw:
        if "Text" in topic and "FirstURL" in topic:
            duck_results.append({
                "title": topic["Text"],
                "link": topic["FirstURL"],
                "displayLink": topic["FirstURL"],
                "snippet": topic["Text"],
                "source": "duckduckgo"
            })
        elif "Topics" in topic:
            for subtopic in topic["Topics"]:
                if "Text" in subtopic and "FirstURL" in subtopic:
                    duck_results.append({
                        "title": subtopic["Text"],
                        "link": subtopic["FirstURL"],
                        "displayLink": subtopic["FirstURL"],
                        "snippet": subtopic["Text"],
                        "source": "duckduckgo"
                    })

    return {
        "google": google_results,
        "duckduckgo": duck_results
    }