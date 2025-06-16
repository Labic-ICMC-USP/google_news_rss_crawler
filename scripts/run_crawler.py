import argparse
import pandas as pd
from google_news_rss_crawler.cities import load_cities
from google_news_rss_crawler.queries import load_queries
from google_news_rss_crawler.crawler import crawl_news

def main():
    parser = argparse.ArgumentParser(description="Run Google News RSS crawler.")
    parser.add_argument("--cities", required=True, help="Path to CSV with cities.")
    parser.add_argument("--queries", required=True, help="Path to TXT file with queries.")
    parser.add_argument("--output", required=True, help="Path to output Parquet file.")
    args = parser.parse_args()

    cities_df = load_cities(args.cities)
    queries = load_queries(args.queries)

    df = crawl_news(cities_df, queries)
    df.to_parquet(args.output, index=False)
    print(f"Saved {len(df)} records to {args.output}")

if __name__ == "__main__":
    main()
