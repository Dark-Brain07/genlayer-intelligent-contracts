# { "Depends": "py-genlayer:test" }
from genlayer import *
import json

class NewsOracle(gl.Contract):
    """
    GenLayer News Oracle
    Fetches latest world news headlines to drive dynamic world events.
    """
    last_headline: str

    def __init__(self):
        self.last_headline = ""

    @gl.public.write
    def fetch_latest_news(self) -> str:
        url = "https://ok.surf/api/v1/cors/news-feed"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.body.decode("utf-8"))
            headline = data["US"][0]["title"]
            return headline

        result = gl.eq_principle.strict_eq(_fetch)
        self.last_headline = result
        return "Breaking News: " + result

    @gl.public.view
    def get_last_headline(self) -> str:
        return self.last_headline

