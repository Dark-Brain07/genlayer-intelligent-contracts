# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *
import json


class WeatherOracle(gl.Contract):
    """Fetches real-time weather data for any city via a public weather API.
    Useful for parametric insurance, agricultural contracts, or event
    postponement triggers. Multiple validators agree on the canonical
    weather state via equivalence principle."""

    weather_data: TreeMap[str, str]

    def __init__(self):
        pass

    @gl.public.write
    def fetch_weather(self, city: str, api_url: str) -> str:
        """Fetch current weather for a city from a weather API.

        Args:
            city: City name key for storage (e.g. "london", "mumbai")
            api_url: Full API URL including auth key if required
        """

        def fetch_and_canonicalize() -> str:
            raw = gl.nondet.web.get(api_url)
            try:
                data = json.loads(raw)
                # Try common weather API field names (Open-Meteo, OpenWeatherMap)
                temp_c = None
                if "current" in data:
                    temp_c = data["current"].get("temperature_2m") or data["current"].get("temp_c")
                elif "main" in data:
                    temp_c = data["main"].get("temp")

                condition = "unknown"
                if "current" in data:
                    condition = data["current"].get("condition", {}).get("text", "unknown")
                elif "weather" in data and len(data["weather"]) > 0:
                    condition = data["weather"][0].get("main", "unknown")

                humidity = 0
                if "current" in data:
                    humidity = data["current"].get("humidity") or data["current"].get("relative_humidity_2m", 0)
                elif "main" in data:
                    humidity = data["main"].get("humidity", 0)

                return f"{city}|{temp_c}|{condition}|{humidity}"
            except Exception:
                return f"{city}|error|error|0"

        result = gl.eq_principle.strict_eq(fetch_and_canonicalize)
        self.weather_data[city] = result
        return result

    @gl.public.write
    def check_rain_threshold(self, city: str, threshold_condition: str) -> str:
        """Use AI to check if a city's weather matches a rain/storm threshold."""
        if city not in self.weather_data:
            raise Exception("CITY_NOT_FOUND: " + city)

        current = self.weather_data[city]

        def reason() -> str:
            prompt = (
                f"Given this weather data: '{current}', does it match the "
                f"condition '{threshold_condition}'? "
                "Return ONLY 'yes' or 'no'."
            )
            return gl.nondet.exec_prompt(prompt).strip().lower()

        return gl.eq_principle.strict_eq(reason)

    @gl.public.view
    def get_weather(self, city: str) -> str:
        if city not in self.weather_data:
            raise Exception("CITY_NOT_FOUND: " + city)
        return self.weather_data[city]
