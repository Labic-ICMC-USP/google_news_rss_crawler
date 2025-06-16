import feedparser
import pandas as pd
import urllib.parse
from .utils import extract_datetime

try:
    # Use notebook-friendly tqdm if running in Jupyter/Colab
    from tqdm.notebook import tqdm
except ImportError:
    from tqdm import tqdm
except:
    from tqdm import tqdm  # Fallback for non-standard environments

def crawl_news(cities_df, queries, start_year=2015, end_year=2025):
    """
    Crawl Google News RSS for all city-query combinations.
    """
    results = []
    for _, row in tqdm(cities_df.iterrows(), total=len(cities_df), desc="Cities"):
        for query in tqdm(queries, desc="Queries", leave=False):
            search_term = f"{query} in {row['City']}, {row['State']}, {row['Country']}"
            safe_query = urllib.parse.quote_plus(search_term)
            for year in range(start_year, end_year):
                after = f"{year}-01-01"
                before = f"{year+1}-01-01"
                rss_url = f"https://news.google.com/rss/search?q={safe_query}+after:{after}+before:{before}&hl=pt-BR&gl=BR"
                feed = feedparser.parse(rss_url)
                for entry in feed.entries:
                    record = {
                        "SOURCEURL": entry.get("link"),
                        "title": entry.get("title"),
                        "text": entry.get("summary"),
                        "media": str(entry.get("source", "")),
                        "query": query,
                        "event_main_location": f"{row['LATITUDE']},{row['LONGITUDE']}",
                        "event_places": f"{row['City']}, {row['State']}, {row['Country']}",
                        "event_main_date_str": entry.get("published", ""),
                        "event_main_date": None
                    }
                    dt = extract_datetime(entry.get("published", ""))
                    if dt:
                        record["event_main_date"] = dt.date().isoformat()
                    results.append(record)
    return pd.DataFrame(results)
