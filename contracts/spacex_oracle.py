# { "Depends": "py-genlayer:test" }
from genlayer import *
import json

class SpaceXOracle(gl.Contract):
    """
    GenLayer SpaceX Oracle
    Fetches the latest SpaceX launch information.
    """
    last_launch_name: str

    def __init__(self):
        self.last_launch_name = ""

    @gl.public.write
    def fetch_latest_launch(self) -> str:
        url = "https://api.spacexdata.com/v4/launches/latest"

        def _fetch() -> str:
            response = gl.nondet.web.get(url)
            data = json.loads(response.body.decode("utf-8"))
            name = data["name"]
            date = data["date_utc"]
            return name + "|" + date

        result = gl.eq_principle.strict_eq(_fetch)
        parts = result.split("|")
        self.last_launch_name = parts[0]
        return "Latest Launch: " + parts[0] + " on " + parts[1]

    @gl.public.view
    def get_last_launch(self) -> str:
        return self.last_launch_name

