# { "Depends": "py-genlayer:test" }
from genlayer import *
import json

class AirQualityOracle(gl.Contract):
    """
    GenLayer Air Quality Oracle
    Fetches Air Quality Index (AQI) for any city.
    """
    last_aqi: str

    def __init__(self):
        self.last_aqi = "0"

    @gl.public.write
    def fetch_city_aqi(self, city: str) -> str:
        if city == "": city = "London"
        url = "https://api.waqi.info/feed/" + city + "/?token=demo"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.body.decode("utf-8"))
            aqi = str(data["data"]["aqi"])
            return aqi

        result = gl.eq_principle.strict_eq(_fetch)
        self.last_aqi = result
        return "Air Quality Index for " + city + ": " + result

    @gl.public.view
    def get_last_aqi(self) -> str:
        return self.last_aqi

