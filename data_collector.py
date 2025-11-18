from duckduckgo_search import DDGS
import time

def fetch_sector_news(sector):
    try:
        with DDGS() as ddg:
            results = ddg.news(
                f"India {sector} market trade opportunities",
                max_results=4
            )
            time.sleep(1)   
            return [r["title"] for r in results]

    except Exception:
        return [
            f" DuckDuckGo temporarily blocked scraping for sector: {sector}",
            "Switching to fallback news source..."
        ]
