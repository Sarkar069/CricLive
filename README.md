# crickbuzz-live-score-scrapper


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
2. Ensure you have the required dependencies installed (see Requirements).
3. Open the script file and edit the match_id in the example usage section to the match you want to track.
4. Run the script using the following command:
```bash
python3 scrapper.py
```

## Example usage
```python
print(fetch_score('12345'))  # Replace '12345' with a valid match ID
```
## Output Example
```json
{
  "title": "India vs Australia, 1st Test, Day 3",
  "liveScore": "India 250/3",
  "runRate": "3.85",
  "batsmanOne": "Virat Kohli",
  "batsmanOneRun": "75",
  "batsmanOneBall": "(120)",
  "batsmanTwo": "Cheteshwar Pujara",
  "batsmanTwoRun": "50",
  "batsmanTwoBall": "(100)",
  "bowlerOne": "Pat Cummins",
  "bowlerOneOver": "12",
  "bowlerOneRun": "45",
  "bowlerOneWickets": "2",
  "bowlerOneEconomy": "3.75",
  "bowlerTwo": "Mitchell Starc",
  "bowlerTwoOver": "10",
  "bowlerTwoRun": "40",
  "bowlerTwoWickets": "1",
  "bowlerTwoEconomy": "4.00"
}
```
## Random User-Agent
The script randomly selects a User-Agent from a predefined list to avoid being flagged or blocked by the website. You can modify the list of User-Agents by editing the `USER_AGENTS` variable.
```python
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
]
```
## Error Handling
If something goes wrong (e.g., invalid match ID, network issues, or changes to the website), the script will return an error message in the following format:
``` json
{
  "error": "Something went wrong: [error details]"
}
```
## License
This project is licensed under the MIT [License](https://github.com/Sarkar069/crickbuzz-live-score-scrapper/tree/main?tab=MIT-1-ov-file#readme).See the LICENSE file for details.







