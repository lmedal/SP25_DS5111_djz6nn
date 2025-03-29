# Lab 08: ERD Design for Gainers Data Pipeline

## Purpose
This ERD models the pipeline that transforms raw gainer data (collected via cron jobs from Yahoo and WSJ) into structured tables. The purpose is to enable financial analysts to identify repeat gainers and gain insight into pricing behavior and trends throughout the week.

---

## Use Cases

1. **Recurring Symbols**  
   Track which stock symbols appear multiple times during the week and whether they repeat across sources (Yahoo or WSJ).

2. **Price Distribution**  
   Provide insights into the overall distribution of stock prices across the week’s gainer lists.

---

## Methods
- Raw timestamped CSVs are stored in `data/raw/` (e.g., `yahoo_gainers_2025-03-29_14-07.csv`)
- These files are ingested into a raw Snowflake table: `raw_gainers`
- SQL in DBT will:
  - Normalize the source and timestamp formats
  - Aggregate repeated symbols across dates
  - Bucket price values into ranges for histogram visualizations

---

## Summary
The ERD below defines how raw CSVs evolve into intermediate and final tables through DBT. These tables support core analytics: tracking recurring gainers and summarizing weekly price distribution. Future iterations could extend this with candlestick data or volatility scores.

---

## ER Diagram (Mermaid.js)

```mermaid
erDiagram
    raw_gainers {
        string symbol
        float price
        string source
        datetime scrape_time
    }

    gainers_summary {
        string symbol
        int appearances
        datetime first_seen
        datetime last_seen
        string sources
    }

    price_distribution {
        string price_range
        int count
    }

    raw_gainers ||--o{ gainers_summary : aggregates
    raw_gainers ||--o{ price_distribution : buckets
