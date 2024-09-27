import requests
from bs4 import BeautifulSoup
import random

CRICBUZZ_URL = "https://www.cricbuzz.com"

# List of common User-Agents
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
]

def fetch_score(match_id):
    try:
        headers = {
            'User-Agent': random.choice(USER_AGENTS)  # Randomly select a User-Agent
        }

        response = requests.get(f"{CRICBUZZ_URL}/live-cricket-scores/{match_id}", headers=headers)
        response.raise_for_status()  # Raise exception for any HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')

        # Helper function to safely get text content
        def safe_get_text(selector, index=0, default="Not Available"):
            element = soup.select(selector)
            if element and len(element) > index:
                return element[index].get_text(strip=True)
            return default

        # Match status handling
        update = safe_get_text('.cb-col.cb-col-100.cb-min-stts.cb-text-complete')
        process = safe_get_text('.cb-text-inprogress')
        noresult = safe_get_text('.cb-col.cb-col-100.cb-font-18.cb-toss-sts.cb-text-abandon')
        stumps = safe_get_text('.cb-text-stumps')
        lunch = safe_get_text('.cb-text-lunch')
        inningsbreak = safe_get_text('.cb-text-inningsbreak')
        tea = safe_get_text('.cb-text-tea')
        rain_break = safe_get_text('.cb-text-rain')
        wet_outfield = safe_get_text('.cb-text-wetoutfield')

        update_message = update or process or noresult or stumps or lunch or inningsbreak or tea or rain_break or wet_outfield or "Match stats will updated soon"


        return {
            'title': safe_get_text('.cb-nav-hdr.cb-font-18.line-ht24').replace(', Commentary', ''),
            'update': update_message
            'liveScore': safe_get_text('.cb-font-20.text-bold', default='Score not available'),
            'runRate': safe_get_text('.cb-font-12.cb-text-gray',1, default='Run rate not available').replace('CRR:\u00a0', ''),
            'batsmanOne': safe_get_text('.cb-col.cb-col-50', 1),
            'batsmanOneRun': safe_get_text('.cb-col.cb-col-10.ab.text-right', 0),
            'batsmanOneBall': f"({safe_get_text('.cb-col.cb-col-10.ab.text-right', 1)})",
            'batsmanOneSR': safe_get_text('.cb-col.cb-col-14.ab.text-right', 0),
            'batsmanTwo': safe_get_text('.cb-col.cb-col-50', 2),
            'batsmanTwoRun': safe_get_text('.cb-col.cb-col-10.ab.text-right', 2),
            'batsmanTwoBall': f"({safe_get_text('.cb-col.cb-col-10.ab.text-right', 3)})",
            'batsmanTwoSR': safe_get_text('.cb-col.cb-col-14.ab.text-right', 1),
            'bowlerOne': safe_get_text('.cb-col.cb-col-50', 4),
            'bowlerOneOver': f"({safe_get_text('.cb-col.cb-col-10.text-right', 8)})",
            'bowlerOneRun': safe_get_text('.cb-col.cb-col-10.text-right', 9),
            'bowlerOneWickets': safe_get_text('.cb-col.cb-col-8.text-right', 8),
            'bowlerOneEconomy': safe_get_text('.cb-col.cb-col-14.text-right', 4),
            'bowlerTwo': safe_get_text('.cb-col.cb-col-50', 5),
            'bowlerTwoOver': safe_get_text('.cb-col.cb-col-10.text-right', 10),
            'bowlerTwoRun': safe_get_text('.cb-col.cb-col-10.text-right', 11),
            'bowlerTwoWicket': safe_get_text('.cb-col.cb-col-8.text-right', 9),
            'bowlerTwoEconomy': safe_get_text('.cb-col.cb-col-14.text-right', 5),
        }

    except Exception as e:
        return {"error": f"Something went wrong: {e}"}

# Example usage:
# Replace '76563' with an actual match ID to get live score data
print(fetch_score('76563'))
