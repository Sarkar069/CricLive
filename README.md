# crickbuzz-live-score-scrapper

# Cricket Score Fetcher

This is a Python script to fetch live cricket match scores from Cricbuzz using web scraping techniques. It uses the `requests` library to make HTTP requests and `BeautifulSoup` from `bs4` to parse the HTML. The script also incorporates random User-Agent selection to mimic requests from different browsers.

## Features

- Fetches live match scores for a specific cricket match using its match ID.
- Retrieves detailed match information including:
  - Match title
  - Live score
  - Current run rate
  - Batsman statistics (runs and balls faced)
  - Bowler statistics (overs, runs conceded, wickets, and economy rate)
- Uses random User-Agent headers for each request to avoid being blocked by the website.

## Requirements

- Python 3.6+
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `random` (part of the Python standard library)

You can install the required libraries using the following command:
```bash
pip install requests beautifulsoup4
```
## How to Use
1. Clone or download this repository.
2.Ensure you have the required dependencies installed (see Requirements).
3. Open the script file and edit the match_id in the example usage section to the match you want to track.
4. Run the script using the following command:
```bash
   python cricket_score_fetcher.py
```

