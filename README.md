# Google News RSS Crawler

This is a general-purpose news crawler designed to collect event-related articles from Google News RSS feeds. It is part of the [WebSensors Project](https://websensors.icmc.usp.br), which aims to build automated pipelines for news monitoring, event extraction, and social impact analysis.

## Installation

You can install the package directly from GitHub:

```bash
pip install git+https://github.com/LABIC-ICMC-USP/google_news_rss_crawler.git
```

## Project Structure

```
google_news_rss_crawler/
├── cities.py         # Load and validate city data from CSV
├── queries.py        # Load queries from TXT
├── crawler.py        # Main module that performs the RSS crawling
├── utils.py          # Auxiliary functions (e.g., datetime extraction)

scripts/
└── run_crawler.py    # Command-line runner to collect and save data

data/
├── example_cities.csv        # Sample file with cities and coordinates
└── example_queries.txt       # Sample file with textual search queries
```

## How it Works

For each combination of query, city, and year, the crawler builds a search string and fetches results using Google News RSS. It extracts structured metadata such as:

* Article title and summary
* Publication date
* Source and URL
* Geo-location (based on input city)
* Original query used

The final output is saved as a `.parquet` file for further processing or analysis.

## Example Usage (Python API)

```python
import pandas as pd
from google_news_rss_crawler.crawler import crawl_news
from google_news_rss_crawler.cities import load_cities
from google_news_rss_crawler.queries import load_queries

# Load input files
cities_df = load_cities("data/example_cities.csv")
queries = load_queries("data/example_queries.txt")

# Run the crawler
df = crawl_news(cities_df, queries, start_year=2022, end_year=2024)

# Save to output file
df.to_parquet("data/news.parquet", index=False)
```

## Input File Format

### Cities CSV

The CSV file must include at least the following columns:

```
City,State,Country,LATITUDE,LONGITUDE
```

### Queries TXT

The TXT file must contain one query per line, for example:

```
gender violence
domestic violence
feminicide
```

## License

MIT License — developed and maintained by [LABIC - ICMC/USP](https://labic.icmc.usp.br)
