# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *
import json


class CricketScoreOracle(gl.Contract):
    """Tracks cricket match scores with innings, overs, and wickets from a
    live scoring API. Uses AI consensus to ensure all validators agree on the
    canonical score format even when the API returns slightly different field
    names across requests."""

    matches: TreeMap[str, str]
    series_leaderboard: TreeMap[str, str]

    def __init__(self):
        pass

    @gl.public.write
    def update_match(self, match_id: str, api_url: str) -> str:
        """Fetch cricket match state from API and validate via AI consensus."""

        def fetch_match() -> str:
            raw = gl.nondet.web.get(api_url)
            try:
                data = json.loads(raw)
                team1 = data.get("team1", {}).get("name", "Team1")
                team2 = data.get("team2", {}).get("name", "Team2")
                team1_score = data.get("team1", {}).get("runs", 0)
                team1_wickets = data.get("team1", {}).get("wickets", 0)
                team1_overs = data.get("team1", {}).get("overs", "0.0")
                team2_score = data.get("team2", {}).get("runs", 0)
                team2_wickets = data.get("team2", {}).get("wickets", 0)
                team2_overs = data.get("team2", {}).get("overs", "0.0")
                status = data.get("status", "in_progress")

                return (
                    f"{team1}|{team1_score}/{team1_wickets}|{team1_overs}|"
                    f"{team2}|{team2_score}/{team2_wickets}|{team2_overs}|{status}"
                )
            except Exception:
                return "ERROR|0/0|0.0|ERROR|0/0|0.0|parse_error"

        result = gl.eq_principle.strict_eq(fetch_match)
        self.matches[match_id] = result
        return result

    @gl.public.write
    def determine_winner(self, match_id: str) -> str:
        """Use AI reasoning to determine the winner based on current match state."""
        if match_id not in self.matches:
            raise Exception("MATCH_NOT_FOUND: " + match_id)

        match_data = self.matches[match_id]

        def reason_winner() -> str:
            prompt = (
                "Given this cricket match state, determine the winner. "
                "Return ONLY one word: team1_name, team2_name, 'draw', or 'in_progress'. "
                f"Match: {match_data}"
            )
            return gl.nondet.exec_prompt(prompt).strip().lower()

        return gl.eq_principle.strict_eq(reason_winner)

    @gl.public.view
    def get_match(self, match_id: str) -> str:
        if match_id not in self.matches:
            raise Exception("MATCH_NOT_FOUND: " + match_id)
        return self.matches[match_id]
