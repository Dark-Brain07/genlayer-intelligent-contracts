# { "Depends": "py-genlayer:test" }
from genlayer import *
import json

class HolidayOracle(gl.Contract):
    """
    GenLayer Holiday Oracle
    Fetches the next public holiday in a country.
    """
    last_holiday: str

    def __init__(self):
        self.last_holiday = ""

    @gl.public.write
    def fetch_next_holiday(self, country_code: str) -> str:
        if country_code == "": country_code = "US"
        url = "https://date.nager.at/api/v3/NextPublicHolidays/" + country_code

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.body.decode("utf-8"))
            holiday = data[0]["name"]
            date = data[0]["date"]
            return holiday + "|" + date

        result = gl.eq_principle.strict_eq(_fetch)
        parts = result.split("|")
        self.last_holiday = parts[0]
        return "Next Holiday in " + country_code + ": " + parts[0] + " on " + parts[1]

    @gl.public.view
    def get_last_holiday(self) -> str:
        return self.last_holiday

