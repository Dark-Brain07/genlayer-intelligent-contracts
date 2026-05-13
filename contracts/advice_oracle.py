# { "Depends": "py-genlayer:test" }
from genlayer import *
import json

class AdviceOracle(gl.Contract):
    """
    GenLayer Advice Oracle
    Fetches deterministic life advice for RPG NPC dialogue.
    """
    last_advice: str

    def __init__(self):
        self.last_advice = ""

    @gl.public.write
    def fetch_advice(self, advice_id: str) -> str:
        if advice_id == "": advice_id = "1"
        url = "https://api.adviceslip.com/advice/" + advice_id

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.body.decode("utf-8"))
            advice = data["slip"]["advice"]
            return advice

        result = gl.eq_principle.strict_eq(_fetch)
        self.last_advice = result
        return "NPC Advice: " + result

    @gl.public.view
    def get_last_advice(self) -> str:
        return self.last_advice

