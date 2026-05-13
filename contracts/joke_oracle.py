# { "Depends": "py-genlayer:test" }
from genlayer import *
import json

class JokeOracle(gl.Contract):
    """
    GenLayer Joke Oracle
    Fetches deterministic jokes for NPC dialogue.
    """
    last_joke: str

    def __init__(self):
        self.last_joke = ""

    @gl.public.write
    def fetch_joke(self, joke_id: str) -> str:
        if joke_id == "": joke_id = "1"
        url = "https://official-joke-api.appspot.com/jokes/" + joke_id

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.body.decode("utf-8"))
            setup = data["setup"]
            punchline = data["punchline"]
            return setup + "|" + punchline

        result = gl.eq_principle.strict_eq(_fetch)
        parts = result.split("|")
        self.last_joke = parts[0] + " " + parts[1]
        return "NPC Joke: " + self.last_joke

    @gl.public.view
    def get_last_joke(self) -> str:
        return self.last_joke

