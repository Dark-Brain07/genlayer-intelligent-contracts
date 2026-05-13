# { "Depends": "py-genlayer:test" }
from genlayer import *
import json

class ExchangeRateOracle(gl.Contract):
    """
    GenLayer Exchange Rate Oracle
    Fetches latest USD/EUR exchange rates.
    """
    last_rate: str

    def __init__(self):
        self.last_rate = "0"

    @gl.public.write
    def fetch_exchange_rate(self) -> str:
        url = "https://open.er-api.com/v6/latest/USD"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.body.decode("utf-8"))
            rate = str(data["rates"]["EUR"])
            return rate

        result = gl.eq_principle.strict_eq(_fetch)
        self.last_rate = result
        return "Current USD/EUR Rate: " + result

    @gl.public.view
    def get_last_rate(self) -> str:
        return self.last_rate

