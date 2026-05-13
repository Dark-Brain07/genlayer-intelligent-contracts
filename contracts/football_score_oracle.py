# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *
import json


class FootballScoreOracle(gl.Contract):
    """Fetches live football match scores from a public API and stores them
    on-chain via AI consensus. Demonstrates web scraping with gl.nondet.web.get()
    and deterministic agreement across validators."""

    match_scores: TreeMap[str, str]
    last_update: TreeMap[str, u32]

    def __init__(self):
        pass

    @gl.public.write
    def fetch_score(self, match_id: str, api_url: str) -> str:
        """Fetch a match score from an external API.

        Args:
            match_id: Unique identifier for the match (e.g. "premier-league-2026-03-15")
            api_url: Public API endpoint returning JSON with score info
        """
        def fetch_and_parse() -> str:
            response = gl.nondet.web.get(api_url)
            # Parse JSON response and extract score in a canonical format
            try:
                data = json.loads(response)
                home_team = data.get("home_team", "Unknown")
                away_team = data.get("away_team", "Unknown")
                home_score = data.get("home_score", 0)
                away_score = data.get("away_score", 0)
                status = data.get("status", "unknown")
                # Pipe-delimited for clean consensus
                return f"{home_team}|{home_score}|{away_team}|{away_score}|{status}"
            except Exception:
                return "ERROR|0|ERROR|0|failed_to_parse"

        result = gl.eq_principle.strict_eq(fetch_and_parse)
        self.match_scores[match_id] = result
        return result

    @gl.public.view
    def get_score(self, match_id: str) -> str:
        if match_id not in self.match_scores:
            raise Exception("MATCH_NOT_FOUND: " + match_id)
        return self.match_scores[match_id]

    @gl.public.view
    def get_all_scores(self) -> str:
        scores = {}
        for key in self.match_scores:
            scores[key] = self.match_scores[key]
        return json.dumps(scores)
